from setuptools import setup, find_packages


setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    url="{{cookiecutter.github_page}}",
    packages=find_packages(),
    cliassfiers=[
        "Programming Language :: Python :: {{cookiecutter.python_version.split('.')[0]}}",
        {% if cookiecutter.license == "MIT" -%}
        "License :: OSI Approved :: MIT License",
        {%- elif cookiecutter.license == "Apache Software License 2.0" -%}
        "License :: OSI Approved :: License :: OSI Approved :: Apache Software License",
        {%- endif %}
        "Operating System :: OS Independent",
    ],
    python_requires=">={{'.'.join(cookiecutter.python_version.split('.')[:2])}}"
)