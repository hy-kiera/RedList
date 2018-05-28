from setuptools import setup, find_packages

setup(
    name             = 'RedList',
    version          = '0.1',
    description      = 'The Open Source CLI Todo List',
    author           = 'Hayeong Lee',
    author_email     = 'bb.kiera@gmail.com',
    url              = 'https://github.com/Ramenseller/B4_OS18',
    download_url     = 'https://github.com/Ramenseller/B4_OS18/archive/master.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = [ ]),
    keywords         = ['todo list'],
    python_requires  = '>=3',
    package_data     =  {'RedList' : [ 'LICENSE' ]},
    zip_safe = False,
    classifiers      = [
        'Environment :: Consol',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)