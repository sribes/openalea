#!/usr/bin/python
# Bison configure environment
# Author: Christophe Pradal ( christophe.pradal@cirad.fr )
# Licence: GPL

import os, sys, re
from sconsx.config import *


class Bison:
   def __init__( self, config ):
      self.name= 'bison'
      self.config= config
      self._default= {}


   def default( self ):

         if isinstance( platform, Win32 ):
            self._default[ 'bin' ]= r'C:\Tools\Bin'
         elif isinstance( platform, Posix ):
            self._default[ 'bin' ]= '/usr/bin'


   def option(  self, opts ):

      self.default()

      opts.Add( 'bison_bin', 'Bison binary path', 
                self._default[ 'bin' ] )


   def update( self, env ):
      """ Update the environment with specific flags """
      t= Tool( 'yacc', toolpath=[ getLocalPath() ] )
      t( env )

      env.Append( YACCFLAGS=[ '-d', '-v' ])
      bison= env.WhereIs( 'bison', env[ 'bison_bin' ] )
      env.Replace( YACC= bison )

      if bison:
         f=os.popen(str(bison)+" --version")
         l=f.readline()
         l=l.split()
         version_text = re.compile(r"\d+.\d+").match(l[-1])
         if version_text is None:
            raise UserWarning, "Unable to retrieve bison version number"
         version= float( version_text.group(0) )
         f.close()

         if version >= 1.30:
            BISON_HPP=True
         else:
            BISON_HPP=False

         env.Append( BISON_HPP= BISON_HPP )
         if BISON_HPP:
            env.Append( CPPDEFINES=["BISON_HPP"] )



   def configure( self, config ):
      b= WhereIs( "bison", config.conf.env[ 'bison_bin' ] )

      if not b:
        s="""
        Warning !!! Bison not found !
        Please, install Bison and try again.
        """
        print s
        sys.exit( -1 )


def create( config ):
   " Create bison tool "
   bison= Bison( config )

   return bison

