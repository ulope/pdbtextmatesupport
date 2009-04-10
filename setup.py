from setuptools import setup, find_packages

setup(name = 'PdbTextMateSupport',
      version = '0.3',
      description = 'Display source code in TextMate while debugging with pdb.',
      keywords = 'textmate pdb',
      author = 'Andreas Zeidler',
      author_email = 'az@zitc.de',
      url = 'https://svn.zitc.de/trac/pdbtextmatesupport',
      download_url = 'http://cheeseshop.python.org/pypi/PdbTextMateSupport/',
      license = 'GPL',
      py_modules = ['PdbTextMateSupport'],
      scripts = ['pdbtmsupport'],
      include_package_data = False,
      platforms = 'Mac OS X',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Environment :: MacOS X',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Text Editors',
      ],
      long_description = """\
          This module is used to hook up pdb_, the python debugger, with TextMate_, an
          advanced text and programming editor for Mac OS, enabling it to display the
          debugged source code during a pdb_ session.

            .. _pdb: http://docs.python.org/lib/module-pdb.html
            .. _TextMate: http://macromates.com/

          After downloading and unpacking the package, you should install the helper
          module using::

              $ python setup.py install

          Next you need to hook up pdb_ with this module by add the following to your
          ``.pdbrc``::

              from PdbTextMateSupport import preloop, precmd
              pdb.Pdb.preloop = preloop
              pdb.Pdb.precmd = precmd

          The easiest way to do this is to use the provided script::

              $ pdbtmsupport enable

          Alternatively you can also do it manually.  The ``.pdbrc`` is located in your
          home folder and possibly needs to be created first.  You may also use the
          supplied sample configuration file for pdb_ to enable the hook like::

              $ cp pdbrc.sample ~/.pdbrc

          Afterwards TextMate_ should get started automatically whenever you enter a
          debug session.  The current source line will be displayed simultaneously while
          stepping through the code.  However, having the cursor moved automatically
          within that source file is not always very obvious, so you might want to use
          the "Highlight current line" feature, which can be enabled in the "General"
          tab in TextMate's preferences. """,
)

