"""Module provides functionality for a menu bar."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk
import six.moves.tkinter_filedialog as tkFile

from collections import deque

from .common.constants import *

from .menu_item import MenuItem


class MenuBar(tk.Menu):
    """Class provides a menubar widget common to most Windows
    applications. Utilizes a JSON file with the desired architecture
    based on the schema in `/templates/menubar_template.json` .

    """

    FIRST_RADIO = True

    def __init__(self, parent, menutree, **kwargs):
        tk.Menu.__init__(self, parent)
        self.parent = parent
        self.input_list = []
        self.mops = {'tearoff': 0}
        self.menubar = tk.Menu(self.parent, **self.mops)
        self.commands = kwargs['commands']

        self.build_menubar(menutree)
        self.parent.config(menu=self.menubar)
        self.enable = self._enable
        self.normal = self._enable
        self.disable = self._disable

    def _enable(self):
        for widget in self.input_list:
            self.menubar.entryconfig(widget, state="normal")

    def _disable(self):
        for widget in self.input_list:
            self.menubar.entryconfig(widget, state="disabled")

    def build_menubar(self, menutree):
        """Summary

        Args:
            path (None, optional): Description

        Returns:
            TYPE: Description
        """

        for elem in menutree:
            menuitem = MenuItem(parent=self.menubar, **elem)

            if menuitem.type.upper() in CASCADE_KEY:
                self.input_list.append(menuitem.label)
                new_menu = self.build_cascade(menuitem)
                self.menubar.add_cascade(label=menuitem.label, menu=new_menu)
            elif menuitem.type.upper() in COMMAND_KEY:
                self.input_list.append(menuitem.label)
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

        tvar = tk.StringVar()
        tvar.set(1)

        while not done:
            if children:
                child = MenuItem(parent=cascitem, **children.popleft())
                if child.children:
                    new_menu = self.build_cascade(child)
                    cascitem.add_cascade(label=child.label, menu=new_menu)
                elif child.type.upper() in COMMAND_KEY:
                    cascitem.add_command(
                        label=child.label,
                        command=self.commands[child.command])
                elif child.type.upper() in RADIOBUTTON_KEY:
                    cascitem.add(
                        itemType='radiobutton',
                        label=child.label,
                        command=self.commands[child.command],
                        variable=tvar)
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
