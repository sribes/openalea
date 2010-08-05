# This file has been generated at Fri Aug  1 14:49:09 2008

from openalea.core import *


__name__ = 'Demo.Forestry_Stand'

__editable__ = True
__description__ = 'tools for forestry stands'
__license__ = 'Cecill-c'
__url__ = ''
__alias__ = []
__version__ = '0.1'
__authors__ = 'VPlants'
__institutes__ = 'INRIA - CIRAD'
__icon__ = 'icon.png'
 

__all__ = ['_149001708', '_149000780']



_149001708 = CompositeNodeFactory(name='Stand_Reconstruction', 
                             description='', 
                             category='Demo',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('openalea.spatial', 'Basic Distribution'),
   3: ('openalea.spatial', 'Aggregative Distribution'),
   4: ('openalea.spatial', 'Random 2D'),
   5: ('openalea.spatial', 'Domain'),
   6: ('openalea.plottools', 'Iterables to Sequence'),
   7: ('openalea.plottools', 'VS Plot'),
   8: ('openalea.file', 'read'),
   9: ('openalea.csv', 'csv2objs'),
   10: ('vplants.plantgl.dresser', 'PGL Dresser'),
   11: ('vplants.stand', 'Stand Positioner'),
   12: ('openalea.functional', 'map'),
   13: ('openalea.python', 'flatten'),
   14: ('vplants.plantgl.visualization', 'plot3D'),
   15: ('vplants.plantgl.objects', 'Scene'),
   16: ('openalea.python', 'len'),
   17: ('system', 'annotation'),
   18: ('system', 'annotation'),
   19: ('system', 'annotation'),
   20: ('system', 'annotation'),
   21: ('system', 'annotation'),
   22: ('system', 'annotation'),
   23: ('system', 'annotation'),
   24: ('system', 'annotation'),
   25: ('system', 'annotation'),
   26: ('system', 'annotation'),
   27: ('system', 'annotation'),
   28: ('system', 'annotation'),
   29: ('system', 'annotation'),
   30: ('system', 'annotation'),
   31: ('system', 'annotation'),
   32: ('system', 'annotation'),
   33: ('system', 'annotation'),
   34: ('system', 'annotation'),
   35: ('Demo.Forestry_Stand', 'stand_data.csv')},
                             elt_connections={  135720668: (10, 0, 12, 0),
   135720680: (4, 1, 11, 2),
   135720692: (6, 0, 7, 0),
   135720704: (9, 0, 11, 0),
   135720716: (13, 0, 15, 0),
   135720728: (35, 0, 8, 0),
   135720740: (16, 0, 4, 0),
   135720752: (11, 0, 12, 1),
   135720764: (4, 0, 11, 1),
   135720776: (2, 0, 4, 1),
   135720788: (4, 1, 6, 1),
   135720800: (4, 0, 6, 0),
   135720812: (8, 0, 9, 0),
   135720824: (5, 0, 4, 2),
   135720836: (15, 0, 14, 0),
   135720848: (9, 0, 16, 0),
   135720860: (12, 0, 13, 0)},
                             elt_data={  2: {  'block': False,
         'caption': 'Random',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 742.35212046893719,
         'posy': 351.25604650971184,
         'priority': 0,
         'user_application': None},
   3: {  'block': False,
         'caption': 'NemanScott',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 602.28111171573607,
         'posy': 313.31737848619622,
         'priority': 0,
         'user_application': None},
   4: {  'block': False,
         'caption': 'Random 2D',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 777.21323158004805,
         'posy': 475.30436551573848,
         'priority': 0,
         'user_application': None},
   5: {  'block': False,
         'caption': 'Domain',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 1031.9022750651445,
         'posy': 381.10365908400979,
         'priority': 0,
         'user_application': None},
   6: {  'block': False,
         'caption': 'Iterables to Sequence',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 733.60212046893719,
         'posy': 643.22103218240522,
         'priority': 0,
         'user_application': None},
   7: {  'block': False,
         'caption': 'VS Plot',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 851.10212046893719,
         'posy': 725.72103218240522,
         'priority': 0,
         'user_application': True},
   8: {  'block': False,
         'caption': 'read',
         'hide': True,
         'lazy': False,
         'port_hide_changed': set([]),
         'posx': 323.50316369616075,
         'posy': 252.27310930434552,
         'priority': 0,
         'user_application': None},
   9: {  'block': False,
         'caption': 'csv2objs',
         'hide': True,
         'lazy': False,
         'minimal': False,
         'port_hide_changed': set([]),
         'posx': 342.57805325987141,
         'posy': 368.40105601469236,
         'priority': 0,
         'user_application': None},
   10: {  'block': False,
          'caption': 'Cones',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 143.12569424403921,
          'posy': 496.5585310507484,
          'priority': 0,
          'user_application': None},
   11: {  'block': False,
          'caption': 'Stand Positioner',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 490.73888882709309,
          'posy': 569.50524150671004,
          'priority': 0,
          'user_application': None},
   12: {  'block': False,
          'caption': 'map',
          'hide': True,
          'lazy': False,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 333.82805325987141,
          'posy': 602.15105601469236,
          'priority': 0,
          'user_application': None},
   13: {  'block': False,
          'caption': 'flatten',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 251.32805325987141,
          'posy': 767.15105601469236,
          'priority': 0,
          'user_application': None},
   14: {  'block': False,
          'caption': 'plot3D',
          'hide': True,
          'lazy': False,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 324.36306758717802,
          'posy': 919.65105601469236,
          'priority': 0,
          'user_application': True},
   15: {  'block': False,
          'caption': 'Scene',
          'hide': True,
          'lazy': False,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 253.82805325987141,
          'posy': 828.40105601469236,
          'priority': 0,
          'user_application': None},
   16: {  'block': False,
          'caption': 'len',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set([]),
          'posx': 565.71435978855027,
          'posy': 465.30890176857861,
          'priority': 0,
          'user_application': None},
   17: {  'posx': 383.2911040823501,
          'posy': 20.324543287973938,
          'txt': 'Stand reconstruction from dendrometric data'},
   18: {  'posx': 697.64115938031057,
          'posy': 236.55014259064012,
          'txt': 'Distribution types'},
   19: {  'posx': 1008.6021204689371,
          'posy': 321.97103218240522,
          'txt': 'Working domain'},
   20: {  'posx': 946.10212046893719,
          'posy': 464.47103218240522,
          'txt': 'Generating random distribution\naccording to desired points number,\ndistribution type and domain'},
   21: {  'posx': 1118.3865922600494,
          'posy': 669.1464888944314,
          'txt': 'Plotting 2D distribution'},
   22: {  'posx': 407.0411040823501,
          'posy': 692.82454328797394,
          'txt': 'Linking spatial distribution\nto stand reconstruction'},
   23: {  'posx': 703.42169197902501,
          'posy': 168.8882968606126,
          'txt': 'Random Spatial Distribution'},
   24: {  'posx': 10.07805325987141,
          'posy': 225.90105601469236,
          'txt': 'Reading data file'},
   25: {  'posx': 15.07805325987141,
          'posy': 325.90105601469236,
          'txt': 'Generating list of objects \nfrom data file lines'},
   26: {  'posx': 22.57805325987141,
          'posy': 602.15105601469236,
          'txt': 'Associating geometry\nto each object of the list'},
   27: {  'posx': 23.82805325987141,
          'posy': 468.40105601469236,
          'txt': 'Generating object\ngeometry'},
   28: {  'posx': 15.07805325987141,
          'posy': 797.15105601469236,
          'txt': 'Scene generation'},
   29: {  'posx': 23.82805325987141,
          'posy': 919.65105601469236,
          'txt': 'Scene visualization'},
   30: {  'posx': 8.7616335976661048,
          'posy': 57.298344493435934,
          'txt': 'Stand reconstruction'},
   31: {  'posx': 970.5175602514737,
          'posy': 9.098424386022657,
          'txt': 'Packages : stand, spatial, plantGL, plotools'},
   32: {  'posx': 973.0175602514737,
          'posy': 49.098424386022657,
          'txt': 'Authors : Da SILVA D.'},
   33: {  'posx': 973.0175602514737,
          'posy': 86.598424386022614,
          'txt': 'Team : Virtual Plants'},
   34: {  'posx': 976.7675602514737,
          'posy': 124.0984243860226,
          'txt': 'Credits : \n    dendrometric data : INRA - UMR Piaf'},
   35: {  'block': False,
          'caption': 'stand_data.csv',
          'hide': True,
          'lazy': True,
          'port_hide_changed': set([2]),
          'posx': 236.18149319608347,
          'posy': 152.73069893346729,
          'priority': 0,
          'user_application': None},
   '__in__': {  'caption': 'In',
                'hide': True,
                'lazy': True,
                'minimal': False,
                'port_hide_changed': set([]),
                'posx': 20.0,
                'posy': 5.0,
                'priority': 0},
   '__out__': {  'caption': 'Out',
                 'hide': True,
                 'lazy': True,
                 'minimal': False,
                 'port_hide_changed': set([]),
                 'posx': 20.0,
                 'posy': 250.0,
                 'priority': 0}},
                             elt_value={  2: [(0, "'Random'")],
   3: [(0, "'NemanScott'"), (1, '2'), (2, '0.20000000000000001')],
   4: [],
   5: [(0, '-1675'), (1, '1977'), (2, '-2094'), (3, '1617'), (4, '1')],
   6: [],
   7: [  (1, "'PointLine'"),
         (2, "'MyPlot'"),
         (3, "'x-axis-label'"),
         (4, "'y-axis-label'"),
         (5, '0')],
   8: [],
   9: [(1, "','"), (2, "'\\n'")],
   10: [(0, "'Cones'"), (1, "{'X_attr': 'X', 'Y_attr': 'Y'}")],
   11: [(3, "'Position mapping (PM)'"), (4, '{}')],
   12: [],
   13: [],
   14: [],
   15: [],
   16: [],
   17: [],
   18: [],
   19: [],
   20: [],
   21: [],
   22: [],
   23: [],
   24: [],
   25: [],
   26: [],
   27: [],
   28: [],
   29: [],
   30: [],
   31: [],
   32: [],
   33: [],
   34: [],
   35: [  (0, 'PackageData(Demo.Forestry_Stand, stand_data.csv)'),
          (1, 'None'),
          (2, 'None')],
   '__in__': [],
   '__out__': []},
                             lazy=True,
                             )



_149000780 = DataFactory(name='stand_data.csv', 
                    description='', 
                    editors=None,
                    includes=None,
                    )


