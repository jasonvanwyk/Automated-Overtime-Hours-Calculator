from setuptools import setup, find_packages

setup(
    name="automated_overtime_calculator",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'overtime-calculator=src.automated_overtime_calculator:main',
        ],
    },
    author="Precept Systems (Pty) Ltd",
    author_email="info@precept.co.za",
    description="Automated Overtime Hours Calculator",
    keywords="overtime, calculator, csv",
    url="https://www.precept.co.za",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Topic :: Office/Business :: Financial",
    ],
)
