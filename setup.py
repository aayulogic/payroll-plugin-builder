from setuptools import setup

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
        "Operating System :: OS Independent"
    ],
    py_modules=["build"],
    python_requires=">=3.6",
)