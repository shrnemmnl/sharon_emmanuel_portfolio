# Sharon Emmanuel - Personal Portfolio

A minimal, clean, and dynamic personal portfolio website built to showcase my transition into web development, professional experience in healthcare IT, and selected projects. 

🔗 **Live Website**: [sharonemmanuel.vercel.app](https://your-vercel-domain.vercel.app) *(Update with your actual Vercel link!)*

---

## 🛠 Tech Stack

- **Backend**: Python, Django 6.0
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **Animations**: GSAP (GreenSock) for smooth scroll reveals
- **Database**: SQLite / PostgreSQL
- **Deployment**: Vercel

---

## ✨ Features

- **Dynamic Content Management**: Fully database-driven template rendering. All profile details, job experiences, and projects are securely managed via the Django ORM.
- **Minimalist Aesthetic**: Architected for modern UX styling, featuring generous whitespace, highly readable typography, and monochromatic elegance.
- **Interactive UI Elements**: Custom smooth JS cursor integration, diffused edge image-masking, and seamless scroll-triggered component reveals.
- **Fully Responsive Navigation**: A polished layout that behaves flawlessly across mobile, tablet, and desktop viewports.

---

## 🚀 Local Development Setup

To run this project locally, execute the following commands in your terminal:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shrnemmnl/sharon_emmanuel_portfolio.git
   cd sharon_emmanuel_portfolio
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database:**
   ```bash
   python manage.py migrate
   ```

5. **Populate the initial database with default profile data:**
   *(Optional script created during development)*
   ```bash
   python populate_db.py
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   *Visit `http://localhost:8000` in your web browser!*

---

## 📫 Contact & Reach Out

I am constantly looking for exciting Python & Django web development opportunities, and love discussing IT infrastructure optimization. Let's connect!

- **Email**: [shrnemmnl@gmail.com](mailto:shrnemmnl@gmail.com)
- **LinkedIn**: [linkedin.com/in/shrnemmnl](https://linkedin.com/in/shrnemmnl)
- **GitHub**: [github.com/shrnemmnl](https://github.com/shrnemmnl)
