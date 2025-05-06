import React from 'react'
import { Link } from 'react-router-dom'
import ThreeScene from './ThreeScene'

const Landing = () => {
  return (
    <section className="min-h-screen bg-[#0f172a] w-full flex flex-col items-center md:flex-row justify-between px-6 md:px-20 py-10">
      <div className="flex flex-col gap-6 justify-center items-center text-center max-w-xl px-4 md:px-0 ">
        <h1 className="text-3xl md:text-7xl text-white text-center">
          Smart Resume Screening with <span className="text-[#38bdf8]">AI</span>
        </h1>
        <p className="text-base md:text-lg lg:text-2xl text-[#d0dbdf61] text-center">
          Find the perfect candidate faster with our advanced AI-powered resume screening tool. Upload job descriptions and resumes to instantly get ranked matches.
        </p>
        <Link to="/upload" className="rounded-lg cursor-pointer bg-[#38bdf8] px-4 py-2 text-black mt-4">
          Try now
        </Link>
      </div>
      <ThreeScene />
    </section>
  );
};

export default Landing;
