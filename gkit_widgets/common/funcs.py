from __future__ import print_function

from __future__ import absolute_import
import os
import re
import json
from collections import OrderedDict

import six.moves.tkinter as tk

###############################################################################
# Credit to: http://code.activestate.com/recipes/580768-tkinter-entry-with-placeholder/
###############################################################################


class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'


def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg=state.normal_color, font=state.normal_font)

            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state

###############################################################################

def read_json(file_path, encoding='UTF-8', ordered=True):
    kwargs = {}
    return_dict = {}
    if os.path.exists(file_path):
        kwargs['encoding'] = encoding
        if ordered:
            kwargs['object_pairs_hook'] = OrderedDict
        with open(file_path, 'r') as fp:
            return_dict = json.load(fp, **kwargs)
    return return_dict


def clear(self, start=0, end=tk.END):
    """Method removes the contents of the object associated.

    Args:
        start (int, optional): Beginning index (inclusive)
        end (TYPE, optional): Terminating index (exclusive)

    Returns:

    """
    if start >= 0 and end <= tk.END:
        self.delete(start, end)
    else:
        output = ''.join(['ERROR: Index out of bounds', os.linesep])
        if start < 0:
            output = ''.join([output, '\t- Start: ', start])
        if end > tk.END:
            output = ''.join([output, '\t- End:', end])
        print(output)


def empty(self, start=0, end=tk.END):
    """Method wraps the clear method for the object associated.

    Args:
        start (int, optional): Beginning index (inclusive)
        end (TYPE, optional): Terminating index (exclusive)

    Returns:

    """
    self.clear(start, end)


def change_state(self, state):
    """Method changes the state of an object.


    Args:
        state (string): 'normal'/'enabled' or 'disabled'
    """
    if state is 'normal' or state is 'enabled':
        self.set_state_normal()
    elif state is 'disabled':
        self.set_state_disabled()


def set_state_normal(self):
    """Changes the state of the console window to normal.
    """
    try:
        self.configure(state=tk.NORMAL)
    except AttributeError:
        pass


def set_state_disabled(self):
    """Changes the state of the console window to disabled.
    """
    try:
        self.configure(state=tk.DISABLED)
    except AttributeError:
        pass


def split_entry(instr, pattern=r"[-?\w']+"):
    """Splits the contents of the entry widget.

    Args:
        instr (TYPE): Description
        pattern (string): Regex pattern used to find entries

    Returns:

    """
    return re.findall(pattern, instr)


###############################################################################


def extract_args(all_args, valid_keys, prefix=''):
    """Method performs matches for the validity of keys provided.

    Args:
        all_args (TYPE): Description
        valid_keys (TYPE): Description
        prefix (String, optional): Description

    Returns:
        TYPE: Description
    """
    kwargs = {}
    for k, v in all_args.items():
        if prefix is not None:
            tokens = v[1]
            if prefix in tokens and k.lower() in valid_keys:
                kwargs[k] = v[0]
    return kwargs


###############################################################################


def dummy():
    """<FRESHLY_INSERTED>"""
    pass
