<<<<<<< HEAD
# RedRecruiter

RedRecruiter is a web application that helps users create, edit, and improve their resumes with the assistance of an AI-powered recruiter chatbot.

## Features

- User registration and login
- Resume creation and editing
- PDF resume generation
- Integrated AI chatbot (Gemini, flash2.0-experimental) with recruiter persona
- Chatbot analyzes uploaded PDF resumes and provides personalized feedback
- Modern red and black themed interface
- User data connected across all features

## Setup

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd projeto_estudos_chatbot
   ```

2. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add your Gemini API key to a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Register a new account.
- Create and edit your resume.
- Generate a PDF version of your resume.
- Chat with the AI recruiter and upload your PDF for analysis and feedback.

## License

This project is for educational purposes.
=======
# SmartResume
RedRecruiter is a web application where users can register, create and edit their resume, and generate a PDF version. 
>>>>>>> ce5a84152137f72f96e7a9cef3bb0a2a6faaa2ec
