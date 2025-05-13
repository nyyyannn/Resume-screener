import React, { useState, useRef } from "react";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import { ClipLoader } from "react-spinners";

const UploadPage = () => {

  const API_BASE_URL = import.meta.env.VITE_APP_URL;
  
  const [resumes, setResumes] = useState([]);
  const [jd, setJd] = useState(null);
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);
  const [limit, setLimit] = useState("");

  const resultRef = useRef(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!jd || resumes.length === 0) {
      toast.warn("Please upload both resumes and job description.");
      return;
    }

    const formData = new FormData();
    formData.append("jd", jd);
    resumes.forEach((resume) => formData.append("resumes", resume));

    setLoading(true);
    setResults(null);

    try {
      console.log("API BASE URL is", API_BASE_URL);
      const response = await axios.post(`${API_BASE_URL}/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      const ranked = response.data.ranked;
      const displayLimit = parseInt(limit);

      const finalResults =
        !isNaN(displayLimit) && displayLimit > 0
          ? ranked.slice(0, displayLimit)
          : ranked;

      setResults(finalResults);

      setTimeout(() => {
        resultRef.current?.scrollIntoView({ behavior: "smooth", block: "start" });
      }, 300); 
    } catch (err) {
      console.error("Upload failed", err);
      toast.error("Something went wrong while uploading!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="min-h-screen bg-[#0f172a] text-white flex flex-col items-center justify-center px-4 py-10">
      <h1 className="text-3xl md:text-5xl mb-8 text-center">Upload Resumes & Job Description</h1>
      <div className="flex flex-col md:flex-row items-center justify-center w-full max-w-4xl gap-6">
        <form onSubmit={handleSubmit} className="flex flex-col gap-6 items-center w-full max-w-md">
          <div className="flex flex-col items-center w-full md:items-start">
            <label className="mb-2 text-white">Job Description:</label>
            <label className="cursor-pointer px-4 py-2 bg-[#38bdf8] text-black rounded hover:bg-[#0ea5e9] transition duration-200">
              Choose Job Description
              <input
                type="file"
                onChange={(e) => setJd(e.target.files[0])}
                className="hidden"
              />
            </label>
            {jd && (
              <p className="text-sm text-gray-300 mt-2">
                Selected: <span className="text-white">{jd.name}</span>
              </p>
            )}
          </div>

          <div className="flex flex-col items-center w-full md:items-start">
            <label className="mb-2 text-white">Resumes:</label>
            <label className="cursor-pointer px-4 py-2 bg-[#38bdf8] text-black rounded hover:bg-[#0ea5e9] transition duration-200">
              Upload Resumes
              <input
                type="file"
                multiple
                onChange={(e) => setResumes(Array.from(e.target.files))}
                className="hidden"
              />
            </label>
            {resumes.length > 0 && (
              <ul className="text-sm text-gray-300 mt-2 list-disc list-inside space-y-1">
                {resumes.map((file, idx) => (
                  <li key={idx} className="text-white">{file.name}</li>
                ))}
              </ul>
            )}
          </div>

          <div className="flex flex-col items-center w-fit md:items-start md:w-full">
            <label className="mb-2 text-white">Number of Candidates to Shortlist:</label>
            <input
              type="number"
              min="1"
              max={resumes.length || 10}
              value={limit}
              onChange={(e) => setLimit(e.target.value)}
              className="w-full p-2 bg-[#1e293b] border border-[#38bdf8] rounded text-white"
              placeholder="e.g., 5"
            />
          </div>

          <button
            type="submit"
            className="bg-[#38bdf8] text-black px-6 py-2 rounded-lg hover:bg-[#0ea5e9] transition-all flex cursor-pointer"
            disabled={loading}
          >
            {loading ? <ClipLoader size={20} color="#000" /> : "Submit"}
          </button>
        </form>

        {results&& (
          <div
            ref={resultRef}
            className="mt-10 md:-mt-40 md:ml-10 w-full max-w-md bg-[#1e293b] p-4 rounded-lg"
          >
            <h2 className="text-xl mb-4 text-[#38bdf8]">Ranked Resumes</h2>
            <ul className="list-decimal list-inside">
              {results.map(([file, score], i) => (
                <li key={i}>
                  <strong>{file.replace(/\.(pdf|txt|docx)$/i, "")}</strong>: {Math.round(score * 100) + " % match"}
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>

      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop
        closeOnClick
        pauseOnFocusLoss
        closeButton={false}
        draggable
        pauseOnHover
        theme="dark"
      />
    </section>
  );
};

export default UploadPage;
