"""Module provides functionality for a labeled entry box."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk

from .common import funcs
from .common.constants import *


class LabeledRadios(tk.Frame):
    """Custom labeled entry contained by a frame.

    Class Extensions:
        Tkinter.Frame (python 2.X)
        tkinter.Frame (python 3.X)

    Tkinter Widget Codes:
        Frame: ['f']
        Label: ['l']
        Entry: ['e']
    """

    def __init__(self, parent, radio_config, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.input_list = []

        frame_ops = funcs.extract_args(kwargs, FRAME_KEYS, FRAME_KEY)
        frame = tk.Frame(self, frame_ops)
        frame.pack(fill='both', expand=True)

        label_ops = funcs.extract_args(kwargs, LABEL_KEYS, LABEL_KEY)
        label = tk.Label(frame, label_ops)

        tvar = tk.StringVar()

        label.pack(side='top', fill='x', expand=True)

        for radio_kwargs in radio_config:
            radio_ops = funcs.extract_args(
                radio_kwargs, RADIOBUTTON_KEYS, RADIOBUTTON_KEY)
            radio_ops['variable'] = tvar
            this_radio = tk.Radiobutton(frame, radio_ops)
            this_radio.pack(side='left', fill='x', expand=True)
            self.input_list.append(this_radio)

        self.parent.columnconfigure(0, weight=1)
        self.get = tvar.get
        self.set = tvar.set
        # self.state = lambda: change_state(self.entry)
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
