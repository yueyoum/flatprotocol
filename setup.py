from setuptools import setup

setup(
    name='flatprotocol',
    version='0.1',
    packages=['flatprotocol', 'flatprotocol.templates'],
    url='',
    license='',
    author='Yueyoum',
    author_email='yueyoum@gmail.com',
    description='',
    entry_points={
        'console_scripts': [
            'flatprotocol = flatprotocol.command:generate'
        ]
    }
)
