"""Module provides functionality for an attachment frame in an email editor."""
from __future__ import absolute_import, print_function, division

import six.moves.tkinter as tk
import six.moves.tkinter_filedialog as tkFile

from .common import funcs
from .common.constants import *


class AttachmentFrame(tk.Frame):
    """Summary

    Attributes:
        button_add_row (TYPE): Description
        button_list_rows (TYPE): Description
        button_purge_rows (TYPE): Description
        frame (TYPE): Description
        ops (TYPE): Description
        parent (TYPE): Description
        row_num (int): Description
        wid_list (list): Description
    """

    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        frame_ops = funcs.extract_args(kwargs, FRAME_KEYS, 'f')
        entry_ops = funcs.extract_args(kwargs, ENTRY_KEYS, 'e')
        button_ops = funcs.extract_args(kwargs, BUTTON_KEYS, 'b')
        scrollbar_ops = funcs.extract_args(kwargs, SCROLLBAR_KEYS, 'sb')
        self.ops = {
            'frame': frame_ops,
            'entry': entry_ops,
            'button': button_ops,
            'scrollbar': scrollbar_ops
        }

        frame = tk.Frame(self, **frame_ops)
        frame.grid(sticky='NEWS')

        button_add_row = tk.Button(
            frame, command=self.add_row, text='Attach File', **button_ops)
        button_add_row.grid(row=0, column=0, sticky='NEWS')

        button_purge_rows = tk.Button(
            frame, command=self.purge_rows, text='Remove All', **button_ops)
        button_purge_rows.grid(row=0, column=1, sticky='NEWS')
        # button_list_rows = tk.Button(
        #     frame, command=self.list_rows, text='List All',
        #     **button_ops
        # )
        # self.button_list_rows.grid(
        #     row=0, column=2, sticky='NEWS'
        # )

        self.wid_list = []
        self.row_num = 1

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def add_row(self, filename=''):
        """Summary

        Args:
            filename (None, optional): Description

        Returns:
            TYPE: Description
        """
        if not filename:
            filename = tkFile.askopenfilename()
            self.parent.lift()
        if filename:
            button_ops = {}
            entry_ops = {}
            frame_ops = {}
            if self.ops:
                button_ops = self.ops['button']
                entry_ops = self.ops['entry']
                frame_ops = self.ops['frame']

            new_frame = tk.Frame(self, **frame_ops)
            new_frame.pack(expand=1, fill=tk.BOTH)
            new_tvar = tk.StringVar()
            new_tvar.set(filename)
            new_entry = tk.Entry(new_frame, textvariable=new_tvar, **entry_ops)
            new_button = tk.Button(
                new_frame,
                command=new_frame.destroy,
                text='Remove',
                **button_ops)
            new_entry.pack(expand=1, side='left', fill=tk.BOTH)
            new_button.pack(expand=1, side='right', fill=tk.X)

            new_frame.grid(row=self.row_num, column=0, sticky='NEWS')
            new_frame.get = new_entry.get
            new_frame.columnconfigure(0, weight=2)
            new_frame.columnconfigure(1, weight=1)

            self.wid_list.append(new_frame)
            self.row_num += 1

    @staticmethod
    def remove_row(frame):
        """Summary

        Args:
            frame (TYPE): Description

        Returns:
            TYPE: Description
        """
        frame.destroy()

    def purge_rows(self):
        """Summary

        Returns:
            TYPE: Description
        """
        for wid in self.wid_list:
            wid.destroy()

    def list_rows(self):
        """Summary

        Returns:
            TYPE: Description
        """
        att_arr = self.get_entry_list()
        att_str = ''
        if att_arr:
            att_str = '\r\n'.join(att_arr)
        print('\nCurrently attached documents:\n{}'.format(att_str))

    def get_entry_list(self):
        """Summary

        Returns:
            TYPE: Description
        """
        vals = []
        for index, wid in enumerate(self.wid_list):
            val = ''
            try:
                val = wid.get()
            except KeyError:
                self.wid_list[index] = None
            if val:
                vals.append(val)
        return vals
