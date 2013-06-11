try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name':'Shadowrun Reddit Die Roller Bot',
    'description': 'A project to roll the dice associated with the game Shadowrun in reddit',
    'author': 'George Barton',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'gbarton@uwo.ca',
    'version': '0.1',
    'install_requires': ['nose', 'praw'],
    'packages': ['NAME'],
    'scripts': [],
}

setup(**config)