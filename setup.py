import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="hpman",
    version="0.0.1",
    author="EMTF",
    author_email="emtf@megvii.com",
    description="A hyperparameter manager for deep learning experiments and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/megvii/hpman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)