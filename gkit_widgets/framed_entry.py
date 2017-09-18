"""Module provides functionality for a framed entry box."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk

from .common import funcs
from .common.constants import *


class FramedEntry(tk.Frame):
    """Class provides a widget for an embedded entry box in a frame.
    """

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        frame_ops = funcs.extract_args(kwargs, FRAME_KEYS, 'f')
        entry_ops = funcs.extract_args(kwargs, ENTRY_KEYS, 'e')
        button_ops = funcs.extract_args(kwargs, BUTTON_KEYS, 'b')

        frame = tk.Frame(self, **frame_ops)
        frame.pack(expand=1, fill=tk.BOTH)
        tvar = tk.StringVar()
        if 'text' in kwargs:
            tvar.set(kwargs['text'])
        entry = tk.Entry(frame, textvariable=tvar, **entry_ops)
        button = tk.Button(frame, command=frame.destroy, **button_ops)
        entry.pack(expand=1, side='left', fill=tk.X)
        button.pack(expand=1, side='right', fill=tk.X)

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
