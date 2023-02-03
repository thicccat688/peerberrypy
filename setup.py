from setuptools import setup, find_packages


setup(
    name='peerberrypy',
    version='1.5.3',
    license='MIT',
    author='Tomás Perestrelo',
    author_email='tomasperestrelo21@gmail.com',
    packages=find_packages(exclude=('tests*', 'testing*')),
    url='https://github.com/thicccat688/peerberrypy',
    download_url='https://pypi.org/project/peerberrypy/',
    keywords='python, api, api-wrapper, peerberrypy',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'pandas',
        'pyotp',
        'requests',
        'openpyxl',
        'cloudscraper',
      ],
)
