from setuptools import setup

setup(
    name='snsd',
    version='1.39',
    description='Example app for building Python project with JFrog',
    author='SSG',
    author_email='ssg@exxonmobil.com',
    url='https://github.com/ExxonMobil-DEV/jfrog-testapp',
    packages=['google'],
    install_requires=['beautifulsoup4', 'requests', 'orjson'],
)
