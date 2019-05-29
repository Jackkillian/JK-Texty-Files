"""
Name:    Python_GUI_App
Version: 1.0.0-alpha
License: MIT License
Author:  Jack Freund a.k.a. R.D. Junkface
"""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import font
from tkinter import filedialog as fd
import sys

class JKTextyExtraText(scrolledtext.ScrolledText):
    '''A customized version of tkinter.scrolledtext.ScrolledText'''
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

    def highlight_pattern(self, pattern, tag, start="1.0", end="end",
                          regexp=False):
        '''Apply the given tag to all text that matches the given pattern

        If 'regexp' is set to True, pattern will be treated as a regular
        expression according to Tcl's regular expression syntax.
        '''

        start = self.index(start)
        end = self.index(end)
        self.mark_set("matchStart", start)
        self.mark_set("matchEnd", start)
        self.mark_set("searchLimit", end)

        count = tk.IntVar()
        while True:
            index = self.search(pattern, "matchEnd","searchLimit",
                                count=count, regexp=regexp)
            if index == "": break
            if count.get() == 0: break # degenerate pattern which matches zero-length strings
            self.mark_set("matchStart", index)
            self.mark_set("matchEnd", "%s+%sc" % (index, count.get()))
            self.tag_add(tag, "matchStart", "matchEnd")
            
class Python_GUI_App():
    """Run Python_GUI_App"""

    def __init__(self):
        """Run Python_GUI_App"""
        self.setup()
        self.def_gui()
        self.grid_gui()
        self.root.mainloop()

    ############################
    # Definitions for __init__ #
    ############################
    
    def setup(self):
        """Setup Python_GUI_App"""
        # Setup the main window
        self.root = tk.Tk()
        self.root.title('Python GUI App | New File')
        # Setup the theme for the main window
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        self.open_filetypes=(('All Files', '.*'), ('Python script', '.py'))
        self.save_filetypes=(('Python script', '.py'),
                             ('Text', '.txt'))
        self.Python_GUI_App_keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
                                        'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
                                        'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while',
                                        'with', 'yield']
                                     
    def def_gui(self):
        """Define the GUI"""
        self.main_text_input = JKTextyExtraText(self.root)
        self.main_text_input.config(font=("Helvetica", 12, "normal"))
        bold_font = font.Font(self.main_text_input, self.main_text_input.cget("font"))
        bold_font.configure(weight="bold")
        self.main_text_input.tag_configure("keywords", foreground='purple', font=bold_font)
        self.main_text_input.bind("<space>", self._highlight_keywords)
        self.main_text_input.insert(1.0, self._ASAO_info())
        self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
        self.open_button = ttk.Button(self.root, text='Open', command=lambda: self._open())
        self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
        self.settings_button = ttk.Button(self.root, text='Settings', command=lambda: self._settings())
        self.settings_button = ttk.Button(self.root, text='Settings', command=lambda: self._settings())
        self.font_frame = ttk.Labelframe(self.root, text='Font Options')
        self.font_combo = ttk.Combobox(self.font_frame, values=font.families())
        self.font_button = ttk.Button(self.font_frame, text='Change Font', command=lambda: self._change_font())
        self.font_size = ttk.Spinbox(self.font_frame, from_=1, to=100)
        self.font_opt = ttk.Combobox(self.font_frame, values=('normal', 'bold', 'italic', 'bold italic'))
        
    def grid_gui(self):
        """Grid the GUI"""
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=1, column=1)
        self.quit_button.grid(row=1, column=2)
        self.main_text_input.grid(row=2, column=0, columnspan=6, rowspan=10)
        self.settings_button.grid(row=1, column=3)
        self.font_frame.grid(row=1, column=7, rowspan=3)
        self.font_combo.grid(row=1, column=0)
        self.font_button.grid(row=4, column=0)
        self.font_size.grid(row=2, column=0)
        self.font_opt.grid(row=3, column=0)
        
    ###########################
    # Definitions for def_gui #
    ###########################

    def _ASAO_info(self):
        """Return Python_GUI_App info"""
        file = open('Add_Ons/pythonguiapptemplate.py', mode='r')
        info = file.readlines()
        
        return info
            
    def _settings(self):
        """Launch Python_GUI_App Settings"""
        self._Python_GUI_App_settings()
    
    def _save(self):
        """Save a file"""
        path = fd.asksaveasfilename(title='Save as', parent=self.root, filetypes=self.save_filetypes)
        
        try:
            file = open(path, mode='w')
            file.write(self.main_text_input.get(1.0, tk.END))
            file.close()
            self.root.title('Python GUI App | ' + path)
        except:
            mbox.showerror('Error Saving File', 'There was an error saving your file. Please try a different directory.', parent=self.root)

    def _open(self):
        """Open a file"""
        path = fd.askopenfilename(title='Please select a file to open', parent=self.root, filetypes=self.open_filetypes)

        try:
            file = open(path, mode='r')
            self.main_text_input.delete(1.0, tk.END)
            self.main_text_input.insert(1.0, file.read())
            file.close()
            self.root.title('Python GUI App | '+ path)
        except:
            mbox.showerror('Error Opening File', 'There was an error opening your file. Please make sure you selected a file, not a folder.', parent=self.root)
        
    def _quit(self):
        """Quit Python_GUI_App"""
        self.root.quit()
        self.root.destroy()

    def save_changes(self):
        """Save Python_GUI_App Settings Changes"""
        self.root_theme.theme_use(self.tc.get())
        self.set_root.quit()
        self.set_root.destroy()

    def _Python_GUI_App_settings(self):
        """Python_GUI_App Settings"""
        self.set_root = tk.Tk()
        self.set_root.title('Python_GUI_App | Settings')
        self.sr_theme = ttk.Style(self.set_root)
        self.sr_theme.theme_use(self.root_theme.theme_use())
        os_values = ['clam', 'classic', 'default', 'alt']
        os_values.sort()
        win_values = ['clam', 'classic', 'default', 'alt', 'xpnative', 'winnative']
        win_values.sort()
        linux_values = ['clam', 'classic', 'default', 'alt']
        linux_values.sort()
        mac_values = ['clam', 'classic', 'default', 'alt', 'aqua']
        mac_values.sort()
            
        # Do some O.S. checking here
        if sys.platform == 'darwin':
            # mac OS
            self.tc = ttk.Combobox(self.set_root, values=mac_values)
        elif sys.platform == 'linux':
            # Linux
            self.tc = ttk.Combobox(self.set_root, values=linux_values)
        elif sys.platform == 'win32':
            # Windows
            self.tc = ttk.Combobox(self.set_root, values=win_values.sort())
        else:
            # O.S. not recognized
            self.tc = ttk.Combobox(self.set_root, values=os_values)

        self.tc_l = ttk.Label(self.set_root, text='App Theme: ')
        self.tc_l.pack()
        self.tc.pack()
        self.s_b = ttk.Button(self.set_root, text='Save Changes', command=lambda: self.save_changes())
        self.s_b.pack()

    def _highlight_keywords(self, event):
        """Highlight keywords"""
        if self.font_size.get() == '':
            self.font_size.set(12)
        bold_font = font.Font(self.main_text_input, self.main_text_input.cget("font"))
        bold_font.configure(weight="bold", size=self.font_size.get())
        self.main_text_input.tag_configure("keywords", foreground='red', font=bold_font)
        index = self.main_text_input.search(r'\s', "insert", backwards=True, regexp=True)
        if index == "":
            index ="1.0"
        else:
            index = self.main_text_input.index("%s+1c" % index)
        word = self.main_text_input.get(index, "insert")
        if word.lower() in self.Python_GUI_App_keywords:
             self.main_text_input.tag_add("keywords", index, "%s+%dc" % (index, len(word)))
        else:
                self.main_text_input.tag_remove("keywords", index, "%s+%dc" % (index, len(word)))

    def _change_font(self):
        """Change the font"""
        if self.font_size.get() == '':
            self.font_size.set(12)
        self.main_text_input.config(font=(self.font_combo.get(), self.font_size.get(), self.font_opt.get()))


def main():
    Python_GUI_App()
