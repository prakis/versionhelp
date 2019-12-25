
from distutils.core import setup
setup(
  name = 'versionhelp',
  packages = ['versionhelp', 'versionhelp.base'], # this must be the same as the name above

  version = '0.3',
  description = 'A Simple Version Command', 
  author = 'Kishore',
  author_email = 'prakis@gmail.com',

  license='MIT',
  url = 'https://github.com/prakis/versionhelp', # use the URL to the github repo
  download_url = 'https://prakis.github.io/versionhelp/archive/versionhelp-0.3.tar.gz',
  keywords = ['version', 'versionhelp'], # arbitrary keywords
  classifiers = [],
)