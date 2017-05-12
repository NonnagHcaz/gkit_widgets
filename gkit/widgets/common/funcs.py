from __future__ import print_function

import os
import re
import json
from collections import OrderedDict

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


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
    if prefix:
        for attr, tuple_arr in all_args.items():
            for val_tuple in tuple_arr:
                attr_val = val_tuple[0]
                tokens = val_tuple[1]
                if prefix in tokens and attr.lower() in valid_keys:
                    kwargs[attr] = attr_val
    return kwargs

###############################################################################


def dummy():
    """<FRESHLY_INSERTED>"""
    pass

