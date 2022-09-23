from setuptools import setup, find_packages


setup(
    name='peerberryapi',
    version='1.0.0',
    license='MIT',
    author='Tomás Perestrelo',
    author_email='tomasperestrelo21@gmail.com',
    packages=find_packages('peerberry'),
    package_dir={'': 'peerberry'},
    url='https://github.com/thicccat688/peerberryapi',
    keywords='peerberry, python, api, api-wrapper',
    install_requires=[
        'pandas',
        'pyotp',
        'requests',
        'openpyxl',
      ],
)
