from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hls-downloader",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool to download videos from .m3u8 URLs using yt-dlp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hls-downloader",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "yt-dlp>=2024.1.1",
        "click>=8.1.3"
    ],
    entry_points={
        "console_scripts": [
            "hls-downloader=hls_downloader.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
