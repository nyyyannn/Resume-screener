# 🧠 Resume Screener

An intelligent resume screening tool designed to automate and enhance candidate shortlisting for recruiters. This project leverages natural language processing (NLP) to extract key insights from resumes and evaluate them against job descriptions with precision and speed.

## 🚀 Features

- 📄 Upload and parse PDF resumes  
- 🧠 NLP-based keyword extraction  
- ⚖️ Match scoring against job descriptions  
- 📊 Dashboard to view candidate fit scores  
- 🗂️ Filter and rank applicants automatically  
- 🛡️ Basic input validation and error handling  

## 🔧 Tech Stack

- **Frontend**: React, Tailwind CSS  
- **Backend**: Node.js, Express.js  
- **ML/NLP**: Python (spaCy, scikit-learn)  
- **Database**: MongoDB  
- **Auth**: JWT (optional)  
- **Parsing**: PDF.js or PyMuPDF  

## 💡 How It Works

1. **Resume Upload**: User uploads one or multiple PDF resumes.  
2. **Parsing**: PDFs are parsed and cleaned for text data.  
3. **NLP Analysis**: Extracts skills, education, experience, etc.  
4. **Job Description Matching**: Compares resume content with job role requirements using keyword and semantic similarity.  
5. **Score Generation**: Each resume is assigned a match percentage.  
6. **Display**: Sorted list of candidates shown on a UI dashboard.  

## 📦 Setup

> Clone the repository
> git clone https://github.com/yourusername/resume-screener.git
> cd resume-screener
