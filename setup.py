Skip to content
Search or jump to…
Pulls
Issues
Marketplace
Explore
 
@FullteaR 
FullteaR
/
factorizer
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
More
factorizer/setup.py /
@FullteaR
FullteaR edit: src/utils.cpp
Latest commit 66851a0 on 25 Mar
 History
 1 contributor
40 lines (34 sloc)  1.14 KB
   
from setuptools import setup, Extension, find_packages
import os
import glob

sources = [] 
sources += glob.glob("src/*.cpp")
sources += glob.glob("src/*.pyx")

root_dir = os.path.abspath(os.path.dirname(__file__))
    
ext = Extension("fastmodinv-py", 
    sources = sources,
    language = "c++",
    extra_compile_args = ["-v", "-std=c++14", "-Wall", "-O3"],
    extra_link_args = ["-std=c++14"]
)

with open(os.path.join(root_dir, 'README.md'), "r") as fp:
    long_description = fp.read()

setup(
    name = "fastmodinv-py",
    version = "0.0.1",
    author = "Fulltea",
    author_email = "rikuta@furutan.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/FullteaR/fastmodinv-py",
    packages = find_packages(where="src"),
    package_dir = {
        "fastmodinv-py": "src"
    },
    install_requires = install_requires,
    ext_modules = [ext]
)