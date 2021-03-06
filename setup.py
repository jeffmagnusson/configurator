from distutils.core import setup

setup(
    name = 'pyconfigurator',
    packages = ['configurator'], # this must be the same as the name above
    version = '0.3',
    description = 'A library for easy configuration',
    author = 'Charles Smith, Jeff Magnusson',
    author_email = 'charles.s.smith@gmail.com, magnussj@gmail.com',
    url = 'https://github.com/charsmith/configurator', # use the URL to the github repo
    keywords = ['configuration', 'ini'], # arbitrary keywords
    license = 'Apache Software License',
    classifiers = [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
    ],
)
