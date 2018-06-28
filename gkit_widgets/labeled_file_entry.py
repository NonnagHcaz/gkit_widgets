"""Module provides functionality for a labeled entry box."""
from __future__ import absolute_import, print_function, division

import os

import six.moves.tkinter as tk
import six.moves.tkinter_tkfiledialog as tkFile

from .common import funcs
from .common.constants import *


class LabeledFileEntry(tk.Frame):
    """Custom labeled entry contained by a frame.

    Class Extensions:
        Tkinter.Frame (python 2.X)
        tkinter.Frame (python 3.X)

    Tkinter Widget Codes:
        Frame: ['f']
        Label: ['l']
        Entry: ['e']
    """

    def __init__(self, parent, image=None, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.input_list = []

        if not image:
            image = os.path.join('static', 'fileicon.png')
        self.photo = tk.PhotoImage(
            file=image)
        self.photo = self.photo.subsample(8)

        frame_ops = funcs.extract_args(kwargs, FRAME_KEYS, FRAME_KEY)
        frame = tk.Frame(self, frame_ops)
        frame.pack(fill='both', expand=True)

        label_ops = funcs.extract_args(kwargs, LABEL_KEYS, LABEL_KEY)
        label = tk.Label(frame, label_ops)
        tvar = tk.StringVar()
        entry_ops = funcs.extract_args(kwargs, ENTRY_KEYS, ENTRY_KEY)
        entry_ops['textvariable'] = tvar
        entry = tk.Entry(frame, entry_ops)
        self.input_list.append(entry)

        button_ops = funcs.extract_args(kwargs, BUTTON_KEYS, BUTTON_KEY)
        button_ops['command'] = self._open
        button_ops['image'] = self.photo
        file_button = tk.Button(frame, button_ops)
        self.input_list.append(file_button)

        label.pack(side='top', fill='x', expand=True)
        entry.pack(side='left', fill='x', expand=True)
        file_button.pack(side='right', expand=False)
        entry.focus_force()
        self.parent.columnconfigure(0, weight=1)
        self.insert = entry.insert
        self.delete = entry.delete
        self.get = entry.get
        self.set = tvar.set
        self.index = entry.index
        self.bind = entry.bind
        self.enable = self._enable
        self.normal = self._enable
        self.disable = self._disable
        self.clear = lambda: funcs.clear(entry)

    def _enable(self):
        for widget in self.input_list:
            funcs.set_state_normal(widget)

    def _disable(self):
        for widget in self.input_list:
            funcs.set_state_disabled(widget)

    def _open(self):
        filename = tkFile.askopenfilename()
        if os.path.exists(filename):
            self.set(filename)
            return filename
        else:
            return ''
