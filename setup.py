from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='basic-image-processing',
    version='0.0.1',
    author='Josevpc',
    author_email='josevictorpiccin@gmail.com',
    description='This is an Basic Image Processing Package',
    long_description=page_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Josevpc/basic-image-processing-package',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.11',
)