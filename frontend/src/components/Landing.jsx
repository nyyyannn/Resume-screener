import React, { useState } from 'react';

const Landing = () => {
  const [jdFile, setJdFile] = useState(null);
  const [resumeFiles, setResumeFiles] = useState([]);

  const handleJdUpload = (e) => setJdFile(e.target.files[0]);
  const handleResumeUpload = (e) => setResumeFiles([...e.target.files]);

  const handleSubmit = () => {
    // Placeholder: Hook up backend later
    console.log("JD File:", jdFile);
    console.log("Resumes:", resumeFiles);
  };

  return (
    <div className="p-8 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Resume Screener</h1>

      <div className="mb-4">
        <label className="block font-medium">Upload Job Description</label>
        <input type="file" accept=".txt,.pdf" onChange={handleJdUpload} />
      </div>

      <div className="mb-4">
        <label className="block font-medium">Upload Resumes</label>
        <input type="file" multiple accept=".txt,.pdf" onChange={handleResumeUpload} />
      </div>

      <button 
        className="px-4 py-2 bg-blue-600 text-white rounded"
        onClick={handleSubmit}
      >
        Submit
      </button>
    </div>
  );
};

export default Landing;
