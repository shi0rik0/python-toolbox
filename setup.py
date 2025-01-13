from setuptools import setup, find_packages
from pathlib import Path


def get_package_name() -> str:
    p = Path(__file__).parent.resolve() / 'src'
    directories = [
        x.name for x in p.iterdir()
        if x.is_dir() and not x.name.endswith('.egg-info')
    ]
    if len(directories) != 1:
        raise ValueError(
            f'Expected exactly one package directory in {p}, found {directories}'
        )
    return directories[0].replace('_', '-')


setup(
    version='0.0.0',
    install_requires=[],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'example-hello = example_package:hello',
        ],
    },
    # You don't need to change the arguments below
    name=get_package_name(),
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
