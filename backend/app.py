from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import uuid
from flask_cors import CORS
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))


app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_files():
    from rank_resumes import rank_resumes_against_jd
    # Ensure the upload folder exists
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
    elif isinstance(obj, (np.intc, np.intp, np.int8, np.int16, np.int32,
                         np.int64, np.uint8, np.uint16, np.uint32, np.uint64)):
        return int(obj)
    elif isinstance(obj, (np.float16, np.float32, np.float64)):
        return float(obj)
    elif isinstance(obj, (np.bool_)):
        return bool(obj)
    elif isinstance(obj, dict):
        return {key: convert_to_serializable(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(convert_to_serializable(item) for item in obj)
    return obj

if __name__ == '__main__':
    app.run(debug=True)
    
