from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import uuid

from scripts.rank_resumes import rank_resumes_against_jd

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_files():
    jd_file = request.files.get('jd')
    resumes = request.files.getlist('resumes')

    if not jd_file or not resumes:
        return jsonify({'error': 'Missing JD or resumes'}), 400

    # Save JD file
    jd_filename = secure_filename(jd_file.filename)
    jd_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4()}_{jd_filename}")
    jd_file.save(jd_path)

    # Save resumes to a folder
    resume_folder = os.path.join(UPLOAD_FOLDER, str(uuid.uuid4()))
    os.makedirs(resume_folder, exist_ok=True)
    for file in resumes:
        filename = secure_filename(file.filename)
        file.save(os.path.join(resume_folder, filename))

    # Run ranking logic
    results = rank_resumes_against_jd(jd_path, resume_folder)

    return jsonify({'ranked': results})

if __name__ == '__main__':
    app.run(debug=True)
