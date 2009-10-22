""" 
>>> python setup.py sphinx_build

"""

import os, sys
from setuptools import setup, find_packages

__revision__ = "$Id$"

# just an alias
pj = os.path.join

name = 'OpenAlea.Misc'
namespace = 'misc'
version = '0.7.1'
description = 'OpenAlea documentation.' 
long_description = ''
author = 'OpenAlea consortium'
author_email = 'Thomas.Cokelaer@inria.fr, Christophe.Pradal@cirar.fr'
url = 'http://openalea.gforge.inria.fr'
license= 'Cecill-C' 
keywords = ['sphinx', 'multisetup']

setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    url=url,
    license=license,
    keywords=keywords,

    namespace_packages = ['openalea'],
    packages = find_packages('src'),

    package_dir = { '' : 'src'},


    entry_points = {
        "console_scripts": [
                 "alea_init_sphinx = openalea.misc.sphinx_tools:init",
                 "upload_dist = openalea.misc.upload_dist:main",
                 "gforge_upload = openalea.misc.gforge_upload:main",
                 ],
    },
    
    install_requires = ['soappy'],
    pylint_packages = ['src/openalea/misc/'],
    )


