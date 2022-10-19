from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="odoo-bin", # This is the name of your PyPI-package.
        license="MIT",
        url="https://github.com/josenoguera-94/odoo-bin",
        version="0.0.1",
        author="Jose Noguera",
        author_email="josenoguera1994@gmail.com",
        long_description=open("README.md").read(),
        packages=find_packages(), # exclude=["tests", "tests.*"]),
        zip_safe=False, # the package can run out of an .egg file
        install_requires=[
            "Babel==2.10.3",
            "certifi==2022.9.24",
            "charset-normalizer==2.1.1",
            "decorator==5.1.1",
            "idna==3.4",
            "Jinja2==3.1.2",
            "lxml==4.9.1",
            "MarkupSafe==2.1.1",
            "passlib==1.7.4",
            "Pillow==9.2.0",
            "polib==1.1.1",
            "psutil==5.9.3",
            "psycopg2==2.9.4",
            "PyPDF2==2.11.1",
            "python-dateutil==2.8.2",
            "pytz==2022.5",
            "pywin32==304",
            "requests==2.28.1",
            "six==1.16.0",
            "typing_extensions==4.4.0",
            "urllib3==1.26.12",
            "Werkzeug==1.0.1"
        ], # external packages as dependencies,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.8"]
        )