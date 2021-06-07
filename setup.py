from setuptools import setup

setup(
    setup(
        name='my_python_package',
        packages=['Test_Data'],
        version='0.0.1',  # Ideally should be same as your GitHub release tag varsion
        description='description',
        author='Gyanaranjan Mahapatra',
        author_email='gyanaranjan.mahapatra@gmail.com',
        url='https://github.com/Gyana15/PythonPackaging',
        download_url='https://github.com/Gyana15/PythonPackaging',
        keywords=['tag1', 'tag2'],
        classifiers=[],
        install_requires=[
            "Django >= 1.1.1",
            "pytest",
            ],
    )
)