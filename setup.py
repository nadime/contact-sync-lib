
from distutils.core import setup
setup(
  name = 'contactssync',         # How you named your package folder (MyLib)
  packages = ['contactssync'],   # Chose the same as "name"
  version = '0.1.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Some useful code for connecting to contact services and objectifying/normalizing contact records, especially for the purpose of synchronizing information between multiple services.',   # Give a short description about your library
  author = 'Scott Asher',                   # Type in your name
  author_email = 'scottpriceasher@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/nadime',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/nadime/contact-sync-lib/archive/refs/tags/v0.1.2-alpha.tar.gz',    # I explain this later on
  keywords = ['people', 'contacts', 'contactssync'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'airtable',
          'google_auth_oauthlib',
          'google',
          'pandas',
          'phonenumbers',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Users',      # Define that your audience are developers
    'Topic :: Software Development :: Contacts',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
