from setuptools import setup, find_packages

setup(
    name='pyqueen',
    version='1.0.0',
    url='https://github.com/ts7ming/pyqueen.git',
    description='command your data',
    author='ts7ming',
    author_email='qiming.ma@outlook.com',
    packages=find_packages(),
    python_requires=">=3.4",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'importlib-metadata',
        'numpy',
        'pandas',
        'PyMySQL',
        'requests',
        'socket.engine',
        'SQLAlchemy',
        'xlrd==1.2.0',
        'XlsxWriter'
    ],
)