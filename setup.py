from setuptools import setup, find_packages

setup(
    name='polyeditor',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['polyeditor = main:run_editor']
        },
    install_requires=[
        'PyQt5==5.10',
        'gpxpy==1.3.4',
        'polyline==1.3.2'
    ]
)

