from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="your_project_name",
    version="0.1.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A brief description of your project",
    packages=find_packages(),
    install_requires=requirements,  
    python_requires=">=3.10",
)