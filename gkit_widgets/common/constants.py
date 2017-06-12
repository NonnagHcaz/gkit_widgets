"""Summary

Attributes:
    BUTTON_KEYS (TYPE): Description
    CANVAS_KEYS (TYPE): Description
    CHECKBUTTON_KEYS (TYPE): Description
    ENTRY_KEYS (TYPE): Description
    FRAME_KEYS (TYPE): Description
    LABEL_KEYS (TYPE): Description
    LABELFRAME_KEYS (TYPE): Description
    LISTBOX_KEYS (TYPE): Description
    MENU_KEYS (TYPE): Description
    MENUBUTTON_KEYS (list): Description
    MESSAGE_KEYS (list): Description
    OPTIONMENU_KEYS (TYPE): Description
    PANEDWINDOW_KEYS (list): Description
    RADIOBUTTON_KEYS (TYPE): Description
    SCALE_KEYS (list): Description
    SCROLLBAR_KEYS (TYPE): Description
    SPINBOX_KEYS (list): Description
    TEXT_KEYS (TYPE): Description
    TOPLEVEL_KEYS (TYPE): Description
"""

# from gkit.attachment_frame import AttachmentFrame
# from gkit.console_window import ConsoleWindow
# from gkit.framed_entry import FramedEntry
# from gkit.labeled_entry import LabeledEntry
# from gkit.menu_item import MenuItem
# from gkit.menu_bar import MenuBar

COMMAND_KEY = 'COMMAND'
CASCADE_KEY = 'CASCADE'
RADIOBUTTON_KEY = 'RADIOBUTTON'

# Button
# http://effbot.org/tkinterbook/button.htm
BUTTON_KEYS = [
    'activebackground', 'activeforeground', 'anchor', 'background', 'bg',
    'bitmap', 'borderwidth', 'bd', 'command', 'compound', 'cursor', 'default',
    'disabledforeground', 'font', 'foreground', 'fg', 'height',
    'highlightbackground', 'highlightcolor', 'highlightthickness', 'image',
    'justify', 'overrelief', 'padx', 'pady', 'relief', 'repeatdelay',
    'repeatinterval', 'state', 'takefocus', 'text', 'textvariable',
    'underline', 'width', 'wraplength'
]

# Canvas
# http://effbot.org/tkinterbook/canvas.htm
CANVAS_KEYS = [
    'background', 'bg', 'borderwidth', 'bd', 'closeenough', 'confine',
    'cursor', 'height'
    'highlightbackground', 'highlightcolor', 'highlightthickness',
    'insertbackground', 'insertborderwidth', 'insertofftime', 'insertontime',
    'insertwidth', 'offset', 'relief', 'scrollregion', 'selectbackground',
    'selectborderwidth', 'selectforeground', 'state', 'takefocus', 'width',
    'xscrollcommand', 'xscrollincrement', 'yscrollcommand', 'yscrollincrement'
]

# Checkbutton
# http://effbot.org/tkinterbook/checkbutton.htm
CHECKBUTTON_KEYS = [
    'activebackground', 'activeforeground', 'anchor', 'background', 'bg',
    'bitmap', 'borderwidth', 'bd', 'command', 'compound', 'cursor',
    'disabledforeground', 'font', 'foreground', 'fg', 'height',
    'highlightbackground', 'highlightcolor', 'highlightthickness', 'image',
    'indicatoron', 'justify', 'offrelief', 'offvalue', 'onvalue', 'overrelief',
    'padx', 'pady', 'relief', 'selectcolor', 'selectimage', 'state',
    'takefocus', 'text', 'textvariable', 'underline', 'variable', 'width',
    'wraplength'
]

# Entry
# http://effbot.org/tkinterbook/entry.htm
ENTRY_KEYS = [
    'background', 'bg', 'borderwidth', 'bd', 'cursor', 'diabledbackground',
    'disabledforeground', 'exportselection', 'font', 'foreground', 'fg',
    'highlightbackground', 'highlightcolor', 'highlightthickness',
    'insertbackground', 'insertborderwidth', 'insertofftime', 'insertontime',
    'insertwidth', 'justify', 'readonlybackground', 'relief',
    'selectbackground', 'selectborderwidth', 'selectforeground', 'show',
    'state', 'takefocus', 'textvariable', 'validate', 'validatecommand',
    'vcmd', 'width', 'xscrollcommand'
]

# Frame
# http://effbot.org/tkinterbook/frame.htm
FRAME_KEYS = [
    'background', 'bg', 'borderwidth', 'bd', 'colormap', 'container', 'cursor',
    'height', 'highlightbackground', 'highlightcolor', 'highlightthickness',
    'padx', 'pady', 'relief', 'takefocus', 'visual', 'width'
]

# Label
# http://effbot.org/tkinterbook/label.htm
LABEL_KEYS = [
    'activebackground', 'activeforeground', 'anchor', 'background', 'bg',
    'bitmap', 'borderwidth', 'bd', 'compound', 'cursor', 'disabledforeground',
    'font', 'foreground', 'fg', 'height', 'highlightbackground',
    'highlightcolor', 'highlightthickness', 'image', 'justify', 'padx', 'pady',
    'relief', 'state', 'takefocus', 'text', 'textvariable', 'underline',
    'width', 'wraplength'
]

# LabelFrame
# http://effbot.org/tkinterbook/labelframe.htm
LABELFRAME_KEYS = []

# Listbox
# http://effbot.org/tkinterbook/listbox.htm
LISTBOX_KEYS = []

# Menu
# http://effbot.org/tkinterbook/menu.htm
MENU_KEYS = [
    'activebackground', 'activeborderwidth', 'activeforeground', 'background',
    'bg', 'borderwidth', 'bd', 'cursor', 'font', 'foreground', 'fg',
    'postcommand', 'relief', 'selectcolor', 'takefocus', 'tearoff',
    'tearoffcommand', 'title', 'type'
]

# Menubutton
# http://effbot.org/tkinterbook/menubutton.htm
MENUBUTTON_KEYS = []

# Message
# http://effbot.org/tkinterbook/message.htm
MESSAGE_KEYS = []

# OptionMenu
# http://effbot.org/tkinterbook/optionmenu.htm
OPTIONMENU_KEYS = ['choices'] + MENU_KEYS

# PanedWindow
# http://effbot.org/tkinterbook/panedwindow.htm
PANEDWINDOW_KEYS = []

# Radiobutton
# http://effbot.org/tkinterbook/radiobutton.htm
RADIOBUTTON_KEYS = [
    'activebackground', 'activeforeground', 'anchor', 'background', 'bg',
    'bitmap', 'borderwidth', 'bd', 'command', 'compound', 'cursor',
    'disabledforeground', 'font', 'foreground', 'fg', 'height',
    'highlightbackground', 'highlightcolor', 'highlightthickness', 'image',
    'indicatoron', 'justify', 'offrelief', 'overrelief', 'padx', 'pady',
    'relief', 'selectcolor', 'selectimage', 'state', 'takefocus', 'text',
    'textvariable', 'underline', 'value', 'variable', 'width', 'wraplength'
]

# Scale
# http://effbot.org/tkinterbook/scale.htm
SCALE_KEYS = []

# Scrollbar
# http://effbot.org/tkinterbook/scrollbar.htm
SCROLLBAR_KEYS = [
    'activebackground', 'activerelief', 'background', 'bg', 'borderwidth',
    'bd', 'command', 'cursor', 'elementborderwidth', 'highlightbackground',
    'highlightcolor', 'highlightthickness', 'jump', 'orient', 'relief',
    'repeatdelay', 'repeatinterval', 'takefocus', 'troughcolor', 'width'
]

# Spinbox
# http://effbot.org/tkinterbook/spinbox.htm
SPINBOX_KEYS = []

# Text
# http://effbot.org/tkinterbook/text.htm
TEXT_KEYS = [
    'autoseparators', 'background', 'bg', 'borderwidth', 'bd', 'cursor',
    'exportselection', 'font', 'foreground', 'fg', 'height',
    'highlightbackground', 'highlightcolor', 'highlightthickness',
    'insertbackground', 'insertborderwidth', 'insertofftime', 'insertontime',
    'insertwidth', 'maxundo', 'padx', 'pady', 'relief', 'selectbackground',
    'selectborderwidth', 'selectforeground', 'setgrid', 'spacing1', 'spacing2',
    'spacing3', 'state', 'tabs', 'takefocus', 'undo', 'width', 'wrap',
    'xscrollcommand', 'yscrollcommand'
]

# Toplevel
# http://effbot.org/tkinterbook/toplevel.htm
TOPLEVEL_KEYS = [
    'background', 'bg', 'borderwidth', 'bd', 'class', 'colormap', 'container',
    'cursor', 'height', 'highlightbackground', 'highlightcolor',
    'highlightthickness', 'menu', 'padx', 'pady', 'relief', 'screen',
    'takefocus', 'use', 'visual', 'width'
]

# __all__ = [
#     'CASCADE_KEY', 'COMMAND_KEY', 'RADIOBUTTON_KEY',
#     'BUTTON_KEYS', 'CANVAS_KEYS', 'CHECKBUTTON_KEYS', 'ENTRY_KEYS',
#     'FRAME_KEYS', 'LABEL_KEYS', 'LABELFRAME_KEYS', 'LISTBOX_KEYS',
#     'MENU_KEYS', 'MENUBUTTON_KEYS', 'MESSAGE_KEYS', 'OPTIONMENU_KEYS',
#     'PANEDWINDOW_KEYS', 'RADIOBUTTON_KEYS', 'SCALE_KEYS',
#     'SCROLLBAR_KEYS', 'SPINBOX_KEYS', 'TEXT_KEYS', 'TOPLEVEL_KEYS'
# ]
