from setuptools import setup,find_packages


def get_requirements(file_path):
    requirements = [ ]
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [r.replace("\n", "" ) for r in requirements]
    return requirements

setup(
    name = "DSProject4",
    version = "0.0.1",
    description=" This is first version",
    author="Hafeez Babar",
    author_email="hafeezbabar76@gmail.com",
    packages= find_packages(),
    install_requirements = get_requirements('requirements.txt')
)