from setuptools import find_packages, setup

setup(
    name='gaproject',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask==1.0.2',
        'flask_debug',
        'Flask_WTF',
        'python-dateutil',
        'twilio'
    ],
)