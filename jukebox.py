import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky, rowspan=rowspan,
        #  **kwargs)  # Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


