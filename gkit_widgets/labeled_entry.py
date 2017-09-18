"""Module provides functionality for a labeled entry box."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk

from .common import funcs
from .common.constants import *


class LabeledEntry(tk.Frame):
    """Custom labeled entry contained by a frame.

    Class Extensions:
        Tkinter.Frame (python 2.X)
        tkinter.Frame (python 3.X)

    Tkinter Widget Codes:
        Frame: ['f']
        Label: ['l']
        Entry: ['e']
    """

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        frame_ops = funcs.extract_args(kwargs, FRAME_KEYS, 'f')
        frame = tk.Frame(self, frame_ops)
        frame.pack(fill='both', expand=True)

        label_ops = funcs.extract_args(kwargs, LABEL_KEYS, 'l')
        label = tk.Label(frame, label_ops)
        tvar = tk.StringVar()
        entry_ops = funcs.extract_args(kwargs, ENTRY_KEYS, 'e')
        entry_ops['textvariable'] = tvar
        entry = tk.Entry(frame, entry_ops)

        label.pack(side='top', fill='x', expand=True)
        entry.pack(side='bottom', fill='x', expand=True)
        entry.focus_force()
        self.parent.columnconfigure(0, weight=1)
        self.insert = entry.insert
        self.delete = entry.delete
        self.get = entry.get
        self.set = tvar.set
        self.index = entry.index
        self.bind = entry.bind
        # self.state = lambda: change_state(self.entry)
        self.enable = lambda: funcs.set_state_normal(entry)
        self.normal = lambda: funcs.set_state_normal(entry)
        self.disable = lambda: funcs.set_state_disabled(entry)
        self.clear = lambda: funcs.clear(entry)
