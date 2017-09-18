"""Module provides functionalty for a menu item."""
from __future__ import absolute_import, print_function, division

from .common.constants import *


class MenuItem(object):
    """Class provides functionality for a menu item."""

    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.type = None
        self.label = None
        self.children = []
        self.command = None

        try:
            self.type = kwargs['type']
            self.label = kwargs['label']
            if self.is_cascade(**kwargs):
                self.children = kwargs['children']
            elif self.is_command(**kwargs) or self.is_radio(**kwargs):
                self.command = kwargs['command']
        except KeyError:
            raise RuntimeError('KeyError in MenuItem instantiation.')

    @staticmethod
    def is_command(**item):
        """Summary

        Args:
            **item (Dict): Description

        Returns:
            Boolean: Description
        """
        if item and item['type'].upper() in COMMAND_KEY:
            return True
        return False

    @staticmethod
    def is_cascade(**item):
        """Summary

        Args:
            **item (Dict): Description

        Returns:
            Boolean: Description
        """
        if item and item['type'].upper() in CASCADE_KEY:
            return True
        return False

    @staticmethod
    def is_radio(**item):
        """Summary

        Args:
            **item (Dict): Description

        Returns:
            Boolean: Description
        """
        if item and item['type'].upper() in RADIOBUTTON_KEY:
            return True
        return False

    def __str__(self):
        extra_val = None
        extra_key = None
        if self.command:
            extra_val = self.command
            extra_key = 'Command'
        elif self.children:
            extra_val = self.children
            extra_key = 'Children'
        msg = ('\nType:\t\t{t}\nLabel:\t\t{l}\n{k}:\t{v}'.format(
            t=self.type, l=self.label, k=extra_key, v=extra_val))
        return msg
