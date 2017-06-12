"""Module provides functionality for a menu bar."""
from __future__ import absolute_import, print_function, division
try:
    import Tkinter as tk
    import tkFileDialog as tkFile
except ImportError:
    import tkinter as tk
    import tkinter.filedialog as tkFile
from collections import deque

from .common import funcs
from .common.constants import *

from .menu_item import MenuItem


class MenuBar(tk.Menu):
    """Class provides a menubar widget common to most Windows
    applications. Utilizes a JSON file with the desired architecture
    based on the schema in `/templates/menubar_template.json` .

    """

    FIRST_RADIO = True

    def __init__(self, parent, **kwargs):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.mops = {'tearoff': 0}
        self.menubar = tk.Menu(self.parent, **self.mops)
        self.commands = kwargs['commands']

        path = None
        if 'path' in kwargs:
            path = kwargs['path']
        self.build_menubar(path)
        self.parent.config(menu=self.menubar)

    def build_menubar(self, path=None):
        """Summary

        Args:
            path (None, optional): Description

        Returns:
            TYPE: Description
        """
        if path is None:
            path = self.get_path()
        menutree = funcs.read_json(path)

        for elem in menutree:
            menuitem = MenuItem(parent=self.menubar, **elem)

            if menuitem.type.upper() in 'CASCADE':
                new_menu = self.build_cascade(menuitem)
                self.menubar.add_cascade(label=menuitem.label, menu=new_menu)
            elif menuitem.type.upper() in 'COMMAND':
                self.menubar.add_command(
                    label=menuitem.label,
                    command=self.commands[menuitem.command])

    def build_cascade(self, menuitem):
        """Summary

        Args:
            menuitem (TYPE): Description

        Returns:
            TYPE: Description
        """
        children = deque(menuitem.children)
        cascitem = tk.Menu(self, **self.mops)
        done = False

        var = tk.StringVar()
        var.set(1)

        while not done:
            if children:
                child = MenuItem(parent=cascitem, **children.popleft())
                if child.children:
                    new_menu = self.build_cascade(child)
                    cascitem.add_cascade(label=child.label, menu=new_menu)
                elif child.type.upper() in 'COMMAND':
                    cascitem.add_command(
                        label=child.label,
                        command=self.commands[child.command])
                elif child.type.upper() in 'RADIOBUTTON':
                    cascitem.add(
                        itemType='radiobutton',
                        label=child.label,
                        command=self.commands[child.command],
                        variable=var)
            else:
                done = True
        return cascitem

    def get_path(self):
        """Summary

        Returns:
            TYPE: Description
        """
        filename = tkFile.askopenfilename()
        self.parent.lift()
        if not filename:
            filename = '.'
        return filename
