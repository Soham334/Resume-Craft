# 🧩 Resume Craft – Full-Stack Django + React Application

**Resume Craft** is a modern, full-stack resume builder designed to demonstrate seamless integration between a **secure Django REST backend** and a **dynamic React frontend**.  
It features elegant animations, robust CRUD functionality, and PDF-optimized layouts — perfect for developers learning full-stack application design and integration.

---

## 🚀 Features

- 🧠 **Full-Stack Integration** – Django REST Framework (DRF) + React + Axios  
- 💾 **CRUD Operations** – Create, Read, Update, Delete resumes with authentication  
- 🛡️ **Security** – CSRF protection, login-required decorators, safe API handling  
- 🎨 **Interactive UI** – GSAP and Locomotive Scroll for smooth animations  
- 🖨️ **PDF Export Ready** – Print-optimized resume templates with custom CSS  
- 🧩 **Bootstrap Styling** – Clean and responsive form designs using `django-widget-tweaks`  
- ⚙️ **Concurrent Setup** – Run both backend and frontend together with a single command  
- 🧪 **Testing** – Backend validation and API security testing using Django test client  

---

## 🧰 Tech Stack

**Frontend:** React, JavaScript, HTML5, CSS3, GSAP, Locomotive Scroll, Webpack  
**Backend:** Django, Django REST Framework, Python  
**Database:** SQLite (default, extendable to MySQL/PostgreSQL)  
**Tools:** Axios, Bootstrap 5, npm, Concurrently  
**Version Control:** Git, GitHub  

---

## ⚙️ Installation & Setup

### **Prerequisites**
Ensure you have the following installed:
- Python 3.10+  
- Node.js & npm  

---

### **Backend Setup (Django)**

```bash
# Clone the repository
git clone https://github.com/yourusername/resume-craft.git
cd resume_builder_project

# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate     # Windows
# OR
source venv/bin/activate    # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser
Frontend Setup (React)
bash
Copy code
cd frontend
npm install
To run both backend and frontend simultaneously:

bash
Copy code
npm run start-all
Then open your browser at:
👉 http://127.0.0.1:8000/

📄 Usage Guide
Access the animated landing page built with GSAP + Locomotive Scroll

Register or log in to manage resumes

Create, update, and delete resumes securely

Export printable, PDF-ready resume templates

Admin users can manage all resumes via the Django admin dashboard
```
🧪 Testing
Run backend unit tests to verify models, authentication, and API security:
python manage.py test resumesite


🖼️ Screenshots (Optional)
You can add screenshots of your app here for visual appeal:
/screenshots
  ├── homepage.png
  ├── dashboard.png
  └── resume_preview.png

Example:
![Resume Craft Dashboard](screenshots/dashboard.png)


🤝 Contributing
Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or fork the repository to enhance features, improve UI, or optimize code.
Steps:


Fork the repo


Create a new branch (feature-branch-name)


Commit your changes (git commit -m "Added new feature")


Push to the branch (git push origin feature-branch-name)


Open a Pull Request



📬 Contact
Author: [Your Name]
Email: your.email@example.com
LinkedIn: linkedin.com/in/yourprofile
GitHub: github.com/yourusername

🧾 License
This project is licensed under the MIT License – see the LICENSE file for details.
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...


🌟 Acknowledgements


Django REST Framework for backend API support


GSAP & Locomotive Scroll for animations


Bootstrap 5 for UI styling


Axios for smooth frontend-backend data flow



⭐ If you found this project helpful, please give it a star on GitHub!

---

Would you like me to tailor this README with your **actual GitHub username and LinkedIn link** so you can copy–paste it directly without editing placeholders?

