# -*- python -*-
#
#       OpenAlea.OALab: Multi-Paradigm GUI
#
#       Copyright 2014 INRIA - CIRAD - INRA
#
#       File author(s): Julien Coste <julien.coste@inria.fr>
#
#       File contributor(s):
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
"""
--------------------------
How to use Project Manager
--------------------------
You can create load or save a project *project* thanks to the project manager *project_manager*.

When you create or load a *project*, the *project_manager* return a *project* like here:

.. code-block:: python

    # Instanciate ProjectManager
    project_manager = ProjectManager()
    # Discover available projects
    project_manager.discover()
    # Create project in default directory
    p1 = project_manager.create('project1')
    # Create project in specific directory
    p2 = project_manager.create('project2', '/path/to/project')
    # Load project from default directory
    p3 = project_manager.load('project3')
    # Load project from specific directory
    p4 = project_manager.load('project4', '/path/to/project')

To search projects that are not located inside default directories:

.. code-block:: python

    project_manager.find_links.append('path/to/search/projects')
    project_manager.discover()
    print project_manager.projects

You can then manipulate *proj* and these attributes (name, controls, scene, global_workflow)
.. code-block:: python

    p1.add("controls", "newcontrol", my_new_control)
    # or
    p1.controls['newcontrol'] = my_new_control

When you have finished, you can save the project:
By default, project are saved in ~/.openalea/projects
You can change default directly with

.. code-block:: python

    p1.save()

.. seealso:: :class:`openalea.vpltk.project.project.Project`_

"""
import os
import platform
from openalea.core.path import path as path_
from openalea.core import settings
from openalea.vpltk.project.project import Project
from openalea.core.singleton import Singleton


class ProjectManager(object):
    """
    Object which manage projects: creation, loading, saving, searching, ...

    It is a singleton.
    """
    __metaclass__ = Singleton

    def __init__(self):
        super(ProjectManager, self).__init__()
        self.projects = []
        self.cproject = self.default()
        self.find_links = [path_(settings.get_project_dir())]

        # TODO Move it into OALab ?
        if not "windows" in platform.system().lower():
            try:
                from openalea import oalab
                from openalea.deploy.shared_data import shared_data

                oalab_dir = shared_data(oalab)
                self.find_links.append(path_(oalab_dir))
            except ImportError:
                pass

        # TODO Search in preference file if user has path to append in self.find_links

    def discover(self):
        """
        Discover projects from your disk and put them in self.projects.

        Projects are not loaded, only metadata are.

        :use:
            >>> project_manager.discover()
            >>> print project_manager.projects

        To discover new projects, you can add path into *self.find_links*

        .. code-block:: python

            project_manager.find_links.append('path/to/search/projects')
            project_manager.discover()
        """
        self.clear()
        for project_path in self.find_links:
            for root, dirs, files in os.walk(project_path):
                if "oaproject.cfg" in files:
                    project_path = root
                    project_path, name = path_(project_path).splitpath()
                    if not ((project_path in [proj.path for proj in self.projects]) and (
                        name in [proj.name for proj in self.projects])):
                        project = Project(name, project_path)
                        project.load()
                        self.projects.append(project)

    def search(self, *args, **kwargs):
        """
        Search a specific project that match filters.

        :use:
            >>> project_manager.search(name="*mtg*", authors="*Godin*")

        :TODO: not implemented yet
        """
        pass

    def get_current(self):
        """
        :return: current active project

        :use:
            >>> project = project_manager.get_current()
        """
        return self.cproject

    def default(self):
        """
        :return: a default empty project
        """
        project_path = path_(settings.get_project_dir())
        proj = Project(project_name="temp", project_path=project_path)
        proj.centralized = False
        return proj

    def load_default(self):
        """
        Load default project if it exists, else create it.

        :return: the default loaded project
        """
        project_path = path_(settings.get_project_dir())
        proj = self.load(project_name="temp", project_path=project_path)

        if proj == -1:  # If can't load default project, create it
            proj = self.default()

        return proj

    def create(self, project_name, project_path=None):
        """
        Create new project and return it.

        :use:
            >>> project1 = project_manager.create('project1')
            >>> project2 = project_manager.create('project2', '/path/to/project')

        :param project_name: name of project to create (str)
        :param project_path: path where project will be saved. By default, project_path is the user path of all projects ($HOME/.openalea/projects/).
        :return: Project
        """
        if project_path is None:
            project_path = path_(settings.get_project_dir())

        self.cproject = Project(project_name, project_path)
        self.cproject.create()

        return self.get_current()

    def load(self, project_name, project_path=None):
        """
        Load existing project

        :use:
            >>> project1 = project_manager.load('project1')
            >>> project2 = project_manager.load('project2', '/path/to/project')

        :param project_name: name of project to load. Must be a string.
        :param project_path: path of project to load. Must be a path (see module path.py). By default, the path is the openaelea.core.settings.get_project_dir() ($HOME/.openalea/projects/).
        :return: Project
        """
        if not project_path:
            project_path = path_(settings.get_project_dir())

        full_path = path_(project_path) / project_name

        if full_path.exists():
            self.cproject = Project(project_name, project_path)
            self.cproject.load()

            return self.get_current()
        else:
            #raise IOError('Project %s in repository %s does not exist' %(project_name,project_path))
            #print 'Project %s in repository %s does not exist' %(project_name,project_path)
            return -1

    def close(self, project_name=None, project_path=None):
        """
        :TODO: not yet implemented
        """
        pass
        # del self.cproject
        # self.cproject = self.default()

    def __getitem__(self, project_name):
        try:
            self.cproject = self.load(project_name)
            return self.get_current()
        except:
            return self.default()

    def clear(self):
        """
        Clear the list of projects.
        """
        self.projects = []
        self.cproject = self.default()


def main():
    from openalea.vpltk.qt import QtGui
    from openalea.vpltk.shell.ipythoninterpreter import Interpreter
    from openalea.vpltk.shell.ipythonshell import ShellWidget
    import sys

    # Create Window with IPython shell
    app = QtGui.QApplication(sys.argv)
    interpreter = Interpreter()
    shellwdgt = ShellWidget(interpreter)
    mainWindow = QtGui.QMainWindow()
    mainWindow.setCentralWidget(shellwdgt)
    mainWindow.show()

    # Create Project Manager
    PM = ProjectManager()

    # Create or load project
    project_name = "project_test"
    proj = PM.load(project_name)
    proj.shell = shellwdgt

    app.exec_()


if ( __name__ == "__main__"):
    main()                  