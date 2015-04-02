from distutils.core import setup

setup(
    name='Lenddo',
    version='0.0.1',
    packages=['lenddo'],
    author='Marsel Mavletkulov',
    author_email='marselester@ya.ru',
    url='https://github.com/marselester/lenddo',
    description='Python API client for Lenddo.com',
    long_description=open('README.rst').read(),
    install_requires=[
        'requests>=2.4.2',
        'python-dateutil>=2.1',
        'six'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
