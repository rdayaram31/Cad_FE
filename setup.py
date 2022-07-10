from setuptools import setup, find_packages

classifiers = [

    'Development Status :: 5- Production/stable',
    'Intended Audience :: Education ',
    'Operating System :: Microsoft: windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programmimg Language :: Python :: 3'
]

setup(
    name='cadfe',
    version='0.0.1',
    description='this package is used to extraction the cad part volume, surface area and the box dimension',
    long_description=open('README.txt').read()+'\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Ravichandra Gupta',
    author_email='rdayaram31@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['Cad','FeatureExtraction','Volume Calculator','Box Dimesion'],
    packages=find_packages(),
    install_requires=['trimesh','gmsh','pyglet']

)