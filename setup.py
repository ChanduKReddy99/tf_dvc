from multiprocessing import AuthenticationError
from setuptools import setup

with open('README.md', 'r', encoding= 'utf-8') as f:
    long_description = f.read()

REPO_NAME = 'simple-dvc-tensorflow-CNN'
AUTHOR = 'ChanduKReddy99'
AUTHOR_EMAIL = 'chanduk.amical@gmail.com'
URL= 'https://github.com/ChanduKReddy99/tf_dvc'
SRC_REPO = 'src'
PYTHON_REQUIRES = '>=3.6'
INSTALL_REQUIREMENTS = [
    'dvc',
    'tensorflow',
    'tqdm',
    'scipy',
    'black',
    'pandas',
    'pyYAML'
]


setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='Simple DVC Tensorflow CNN',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url= URL,
    license= 'MIT',
    packages=['src'],
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIREMENTS
)

