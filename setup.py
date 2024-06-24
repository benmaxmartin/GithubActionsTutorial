from setuptools import setup, find_packages

setup(
    name='dummy_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your dependencies here, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            # if you have any scripts/commands to expose, add them here
            # 'my-command=my_package.module:function',
        ],
    },
    author='Sankhadip Mazumder',
    author_email='dummy_email@google.com',
    description='A dummy wheel package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
