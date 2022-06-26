from setuptools import setup

setup(
    name='mazesolver',
    author='Joan A. Pinol  (japinol)',
    version='0.0.3',
    license='MIT',
    description="Creates and solves mazes.",
    long_description="Creates and solves mazes of NxN cells with a start and a goal.",
    url='https://github.com/japinol7/maze-solver',
    packages=['mazesolver'],
    python_requires='>=3.9',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mazesolver=mazesolver.__main__:main',
            ],
    },
)
