# -*- python -*-
#
#       OpenAlea.Catalog
#
#       Copyright 2006 - 2007 INRIA - CIRAD - INRA  
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
################################################################################


__doc__=""" catalog.model """
__revision__=" $Id$ "


from openalea.core import *

__name__ = "openalea.model"
__alias__ = ["catalog.model"]

__version__ = '0.0.1'
__license__ = 'CECILL-C'
__authors__ = 'OpenAlea Consortium'
__institutes__ = 'INRIA/CIRAD'
__description__ = 'Models.'
__url__ = 'http://openalea.gforge.inria.fr'

__all__ = ['linear']

    
linear = Factory( name="linearmodel", 
                  description="Linear Model", 
                  category="Model", 
                  nodemodule="models",
                  nodeclass="linearmodel",
                  )




