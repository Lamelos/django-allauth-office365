from setuptools import setup, find_packages

setup(
    name = "django-allauth-office365",
    version = "0.0.1",
    author = "lamelos",
    author_email = "lamelos@gmail.com",
    description = "Office365 oAuth provider for django-allauth",
    url = "https://github.com/lamelos/django-allauth-office365",
    packages=find_packages(),
    install_requires=['django-allauth>=0.26.0'],
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
