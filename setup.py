from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-lumberjack-client",
    version="1.0.0",
    author="Ed Chapman",
    author_email="ed@edwardchapman.co.uk",
    description="Django Lumberjack client app.",
    long_description=long_description,
    url="https://github.com/edjchapman/django-lumberjack-client",
    packages=find_packages(exclude=["tests*"]),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: Log Analysis",
        "Topic :: System :: Logging",
    ],
    python_requires=">=3.8",
    install_requires=["Django>=4" "requests>=2", "djangorestframework>=3"],
)
