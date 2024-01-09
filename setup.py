from setuptools import setup

with open("README.md", 'r', encoding ="utf-8") as f:
    long_description = f.read()


SRC_REPO = "src"
AUTHOUR_USER_NAME = "VenkateshKarlpaudi"
REPO_NAME =  "project-template"
LIST_OF_REQUIREMENTS = []

setup( name = SRC_REPO,
      version= "0.0.1",
      author= AUTHOUR_USER_NAME,
      description= "This is our first project",
      long_description= long_description,
      url =f"https://github.com/{AUTHOUR_USER_NAME}/{REPO_NAME}",
      author_email= "venkykarthik1989@gmail.com",
      packages = [SRC_REPO],
      python_requires = ">3.11",
      install_requires = LIST_OF_REQUIREMENTS
)