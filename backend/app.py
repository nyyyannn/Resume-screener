from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import uuid
from flask_cors import CORS
from scripts.rank_resumes import rank_resumes_against_jd  # ✅ Corrected absolute import

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://resume-screener-teal.vercel.app"}}, supports_credentials=True)

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST', 'OPTIONS'])  # ✅ Include OPTIONS
def upload_files():
    jd_file = request.files.get('jd')
    resumes = request.files.getlist('resumes')

    if not jd_file or not resumes:
        return jsonify({'error': 'Missing JD or resumes'}), 400

    jd_filename = secure_filename(jd_file.filename)
    jd_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}_{jd_filename}")
    jd_file.save(jd_path)

    resume_folder = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()))
    os.makedirs(resume_folder, exist_ok=True)
    for file in resumes:
        filename = secure_filename(file.filename)
        file.save(os.path.join(resume_folder, filename))

    results = rank_resumes_against_jd(jd_path, resume_folder)
    serializable_results = convert_to_serializable(results)
    return jsonify({'ranked': serializable_results})

def convert_to_serializable(obj):
    import numpy as np
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, (np.generic,)):
        return obj.item()
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(convert_to_serializable(item) for item in obj)
    return obj

if __name__ == '__main__':
    app.run(debug=True)
