import setuptools

import io
import os
import re

with io.open('throttle/version.py', 'rt', encoding='utf-8') as f:
    version = re.search(r"__version__ = '(.*?)'", f.read()).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-throttle",
    version=version,
    author="Andi Gortz",
    # author_email=set email here,
    description="django packages for used to control rate limiting based on throttle method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/django-repo/django-throttle",
    # license='MIT',
    zip_safe=False,
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.5',
)
