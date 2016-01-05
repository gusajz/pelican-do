
try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'pelican-do',
  'author': 'Commands to automate common pelican tasks',
  'url': '',
  'download_url': '',
  'author_email': 'gustavoajz@gmail.com',
  'version': '0.1',
  'install_requires': [
    'click==6.2',
    'Jinja2==2.8',
    'awesome-slugify==1.6.5',
    'testfixtures==4.7.0'
  ],
  'extras_require': {
    'development': [
    ],
  },
  'packages': ['pelican_do'],
  'scripts': [],
  'name': 'pelican-do',
  'entry_points': {
    'console_scripts': ['pelican-do=pelican_do.main:main']
  }
}

setup(**config)
