try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name':'Shadowrun Reddit Die Roller Bot',
    'description': 'A project to roll the dice associated with the game Shadowrun in reddit',
    'author': 'George Barton',
    'url': 'https://github.com/Darkman94/ShadowrunDie',
    'author_email': 'gbarton@uwo.ca',
    'version': '1.0',
    'install_requires': ['nose', 'praw'],
    'packages': ['ShadowrunDie'],
    'scripts': [],
}

setup(**config)