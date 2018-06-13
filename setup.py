import setuptools
main_ns={}
exec(open('posts/version.py').read(), main_ns) 
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="posts",
    version=main_ns['__version__'],
    author="Ryan J Frizzell",
    author_email="ryan@frizzell.io",
    scripts = [ "pcli" ],
    description="Blog Poster utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanjfrizzell/posts",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
)
