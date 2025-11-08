Resume Craft: Full-Stack Django + React Application

This project is a modern, full-stack resume builder designed to demonstrate the integration of an aesthetic React/Webpack frontend with a secure, traditional Django backend and REST API.

The application features a dynamic, animated user interface built on GSAP and Locomotive Scroll, alongside robust CRUD functionality for resume management.

🚀 1. Setup and Installation

Follow these steps to set up and run the entire application environment.

Prerequisites

You must have Python 3.10+ (with pip) and Node.js (with npm) installed on your system.

A. Backend Setup (Python/Django)

Navigate to the project root (where manage.py is):

cd resume_builder_project


Activate the Python Virtual Environment:

.\venv\Scripts\activate  # For Windows PowerShell/CMD
# OR
source venv/bin/activate # For Linux/macOS


Install Python Dependencies:

pip install -r requirements.txt 
# NOTE: You must create a requirements.txt file listing Django, djangorestframework, and django-widget-tweaks


Apply Database Migrations:

python manage.py migrate


Create Superuser (for Admin access):

python manage.py createsuperuser


B. Frontend Setup (Node/React)

Navigate to the frontend directory:

cd frontend


Install Node Dependencies:

npm install


✨ 2. Running the Project (Single Command)

To run both the Django server and the React Webpack compiler simultaneously in a single terminal, use the start-all command (requires concurrently package installed via npm install).

Ensure you are in the frontend directory.

Run the combined launch script:

npm run start-all


Accessing the Application

The animated landing page will be available at:

URL: http://127.0.0.1:8000/

🔬 3. Academic Experiment Documentation (CO Mapping)

This project satisfies multiple requirements by integrating various architectural components:

CO1 & CO5: Full-Stack Integration & API Usage

Objective: Demonstrate using a modern JavaScript framework (React) with Django via a REST API.

Feature

Implementation Details

Frontend Rendering

React manages the dynamic BuilderDashboard and LandingPage.

Advanced Animation

The Landing Page uses GSAP and Locomotive Scroll for dramatic entrance effects, requiring conditional JS execution to run only after the React components have mounted.

API Data Flow

The dashboard uses axios and the ResumeViewSet (DRF) to fetch user data and handle secure Delete (D) operations without full page reloads.

Security

Custom JS ensures the CSRF token is read from the cookie and sent with all mutating API requests (POST/DELETE).

Experiment CO2 & CO3: Django Views and Forms

Objective: Demonstrate classical Django CRUD views and professional form rendering.

Feature

Implementation Details

Form Styling

The resume_form.html template uses the {% load widget_tweaks %} library to apply Bootstrap 5 classes to fields for a clean, sharp, and functional aesthetic.

CRUD Views

All core CRUD operations (Create, Edit, Delete) are handled via the create_resume, resume_detail, and delete_resume views, enforcing the login_required decorator for security.

Print Optimization

The Resume Detail View (resume_detail.html) is styled with a monochromatic theme and specific @media print CSS rules to ensure a perfect, high-quality, single-page PDF output.

🧪 4. Running Unit Tests

To verify the backend logic and API security (CO5), run the following command from the project root:

(venv) python manage.py test resumesite


This runs the tests verifying model validation, user authentication security (intruder exclusion), and successful CRUD operations via the Django test client.