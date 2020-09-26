from setuptools import setup, find_packages

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='robotkeywords',
    url='https://github.com/daniel270',
    author='daniel adewale',
    author_email='xdolomite@gmail.com',
    # Needed for dependencies
    install_requires=['selenium', 'robotframework', 'docker', 'pyvirtualdisplay', 'pyscreenshot', 'Pillow'],
    # directories
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # need to declare this entry point as a module or it will not find it at runtime.
    # py_modules=['SeleniumKeywords', 'FrameworkKeywords', 'AnnotationsListener'],
    entry_points={
        'console_scripts': [
            'RobotParallelRunner = RobotParallelRunner:main'
        ],
    },
    # *strongly* suggested for sharing
    version='0.12',
    # The license can be anything you like
    license='MIT',
    description='robot framework robotkeywords library',
    setup_requires=['wheel', 'twine'],
    include_package_data=True,
    zip_safe=True
)
