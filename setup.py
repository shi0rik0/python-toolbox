from setuptools import setup, find_packages
from pathlib import Path

COMMAND_PREFIX = 'my_'


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
    return directories[0]


package_name = get_package_name()
subpackages = find_packages('src')
subpackages = [i for i in subpackages if i.count('.') == 1]


def package_name_to_command_name(package_name: str) -> str:
    return COMMAND_PREFIX + package_name.split('.')[-1].replace('_', '-')


setup(
    version='0.0.0',
    install_requires=[],
    python_requires='>=3.6',
    entry_points={
        'console_scripts':
        [f'{package_name_to_command_name(i)} = {i}:main' for i in subpackages],
    },
    include_package_data=True,
    package_data={package_name: ['create_electron/data/*']},
    # You don't need to change the arguments below
    name=package_name.replace('_', '-'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
