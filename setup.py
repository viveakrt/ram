from setuptools import setup, find_packages

setup(
    name='ram',  
    version='0.1',  
    description='A short description of your package',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/viveakrt/ram.git',
    author='Vivek', 
    author_email='carbonvivek@gmail.com', 
    packages=find_packages(),  
    classifiers=[  
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',  
    entry_points={  
        'console_scripts': [
            'ram=ram.cli:main',
        ],
    },
)