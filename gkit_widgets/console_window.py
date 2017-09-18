"""Module provides functionality for a console window."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk

from .common import funcs
from .common.constants import *


class ConsoleWindow(tk.Frame):
    """Custom command console widget to emulate a terminal window/CLI.

    Class Extensions:
        Tkinter.Frame (python 2.X)
        tkinter.Frame (python 3.X)

    Tkinter Widget Codes:
        Frame: ['f']
        Text: ['t']
        Scrollbar: ['sb']

    """

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent)

        text_ops = funcs.extract_args(kwargs, TEXT_KEYS, 't')
        text = tk.Text(self, **text_ops)

        scrollbar_ops = funcs.extract_args(kwargs, SCROLLBAR_KEYS, 'sb')
        vsb = tk.Scrollbar(self, command=text.yview, **scrollbar_ops)
        text.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        text.pack(side="left", fill="both", expand=True)
        text.tag_configure('br', lmargin2=80, tabs=35)

        # expose some text methods as methods on this object
        self.insert = text.insert
        self.delete = text.delete
        self.get = text.get
        self.index = text.index
        self.search = text.search
        self.see = text.see
        # self.state = lambda: change_state(self.text)
        self.enable = lambda: funcs.set_state_normal(text)
        self.disable = lambda: funcs.set_state_disabled(text)
        self.clear = text.delete(1.0, tk.END)
