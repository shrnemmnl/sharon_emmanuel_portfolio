import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from core.models import Profile, Experience, Project, Skill

# Clear existing rows to prevent duplicates if run multiple times
Profile.objects.all().delete()
Experience.objects.all().delete()
Project.objects.all().delete()
Skill.objects.all().delete()

# Create Profile
Profile.objects.create(
    name="SHARON EMMANUEL",
    tagline="Python & Django Developer | System Analyst",
    about="Python and Django Developer with over 10 years of experience in healthcare IT, system analysis, and infrastructure management. Recently transitioned into full-time web development through a structured work-simulation environment. Experienced in building secure, production-ready web applications using Django’s server-side architecture. Strong foundation in Linux systems, networking, and real-world problem solving with a system-level mindset.",
    email="shrnemmnl@gmail.com",
    linkedin="https://linkedin.com/in/shrnemmnl",
    github="https://github.com/shrnemmnl"
)

# Create Experiences
experiences = [
    {
        "company": "Brototype, Kochi",
        "role": "Python & Django Web Developer",
        "duration": "Jul 2024 – Present",
        "description": "• Worked in a full-time, office-like development environment simulating real software teams.\n• Followed a self-research-driven learning model focused on independent problem solving.\n• Executed structured project tasks aligned with real-world development workflows.\n• Designed, developed, and deployed a production-level e-commerce platform using Django.",
        "order": 1
    },
    {
        "company": "Lisie Hospital, Ernakulam",
        "role": "System Analyst",
        "duration": "Nov 2018 – Jul 2024",
        "description": "• Managed networking infrastructure including VLANs and system upgrades.\n• Administered servers, databases, mail systems, and virtualization environments.\n• Analyzed hospital workflows to improve system usability.\n• Delivered high-availability support in mission-critical healthcare operations.\n• Conducted user training sessions for non-technical staff.",
        "order": 2
    },
    {
        "company": "Freelance IT Consultant",
        "role": "IT Consultant",
        "duration": "Oct 2016 – Oct 2018",
        "description": "• Delivered end-to-end IT solutions for individuals and small businesses.\n• Co-founded an IT services venture handling hardware, networking, CCTV, and recovery.\n• Managed client communication and complete solution delivery.",
        "order": 3
    },
    {
        "company": "Lourdes Hospital, Kochi",
        "role": "Information Technology Assistant",
        "duration": "Sep 2013 – Sep 2016",
        "description": "• Maintained network infrastructure and system administration operations.\n• Installed and supported hardware, software, printers, and security systems.\n• Provided troubleshooting and preventive maintenance.",
        "order": 4
    }
]

for exp in experiences:
    Experience.objects.create(**exp)

# Create Projects
Project.objects.create(
    title="Book Hive – Online Bookstore",
    description="Developed a full-stack e-commerce platform using Django. Implemented authentication, cart system, wishlist, search, filtering, and secure payment integration (Razorpay). Built admin dashboard for inventory, order, and user management. Deployed live production system.\n\nTech Stack: Python, Django, PostgreSQL, HTML, CSS, JavaScript, Razorpay",
    live_link="https://textbookhive.shop/",
    github_link="https://github.com/shrnemmnl",
    order=1
)

# Create Skills
skills = [
    "Python", "Django", "HTML", "CSS", "JavaScript",
    "PostgreSQL", "SQL", "Linux", "Networking", "VLANs",
    "Git", "GitHub", "System Analysis"
]

for i, skill in enumerate(skills):
    Skill.objects.create(name=skill, order=i)

print("Database successfully populated with user details!")
