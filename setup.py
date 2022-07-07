from setuptools import setup, Extension
import os


root_dir = os.path.abspath(os.path.dirname(__file__))
    
ext = Extension("modinv", 
    sources = ["src/modinv.pyx", "src/modinv_cpp.cpp"],
    language = "c++",
    extra_compile_args = ["-v", "-std=c++14", "-Wall", "-O3","-lboost_system"],
    extra_link_args = ["-std=c++14"]
)

with open(os.path.join(root_dir, 'README.md'), "r") as fp:
    long_description = fp.read()

setup(
    name = "modinv",
    version = "0.0.1",
    author = "Fulltea",
    author_email = "rikuta@furutan.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/FullteaR/fastmodinv-py",
    ext_modules = [ext]
)