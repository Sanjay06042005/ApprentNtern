# 🎓 AI-Powered Internship & Apprenticeship Portal  

An **AI-driven web portal** designed to streamline **internship and apprenticeship opportunities** for students using **Machine Learning (ML), Natural Language Processing (NLP), and MongoDB**.  

This portal enables **resume parsing, AI-based recommendations, email verification, and profile management**, with separate sections for **internships** and **apprenticeships**.  

---

## 🚀 Key Features  

- 🔑 **User Authentication & Profile Section** – Students can create and manage profiles  
- 📄 **Resume Parsing (PDF/DOCX)** – Extracts skills, education, and experience using **spaCy & pyresparser**  
- 🤖 **AI-Powered Matching** – Recommends best-fit internships/apprenticeships using:
  - TF-IDF Vectorization  
  - Cosine Similarity  
  - RapidFuzz for string similarity  
- 🏢 **Separate Pages** – Dedicated pages for **Internships** & **Apprenticeships**  
- 📧 **Email Verification** – Sends confirmation via SMTP after application  
- 🗄 **MongoDB Integration** – Stores student profiles, resumes, and opportunities in **MongoDB Atlas/Compass**  
- 🎨 **Streamlit Frontend** – Simple & interactive user interface  

---

## 🛠️ Tech Stack  

| Component     | Technology Used |
|---------------|-----------------|
| **Frontend**  | Streamlit |
| **Backend**   | Python, Flask (for APIs if needed) |
| **Database**  | MongoDB (Atlas/Compass) |
| **AI/NLP**    | scikit-learn, spaCy, pyresparser, rapidfuzz |
| **Email**     | smtplib, EmailMessage |
| **Libraries** | pandas, pymongo, fitz (PyMuPDF), docx |

---


