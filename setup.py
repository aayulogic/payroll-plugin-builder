from setuptools import setup, find_packages

setup(
    name='rhrs_payroll_calc_plugin_builder',
    version='0.9',    
    description='RealHRSoft payroll calculator plugin builder',
    url='https://github.com/aayulogic/payroll-plugin-builder.git',
    author='Rupesh Singh',
    author_email='rupesh.singh@aayulogic.com',
    install_requires=[
        'Cython>=0.29.23',
        'PGPy>=0.5.4'                     
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)