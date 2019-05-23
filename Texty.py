"""
Name:    JK Texty
Version: 1.0.0
Author:  Jackkillian a.k.a. Jack Freund
License: MIT License
Website: https://github.com/Jackkillian/JK-Texty
O.S.:    Source Code (Any O.S.)
"""

"""
Whew! This was fun to code.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog as fd
from tkinter.scrolledtext import ScrolledText as scrolledtext
from webbrowser import open as open_url
from urllib.request import urlretrieve as download
from random import randint
import urllib
from os.path import dirname
import os
import sys

__texty_version__ = '1.0.0'

class Texty_Updater():
    """Open the Texty Updater"""
    
    def __init__(self):
        """Open the Texty Updater"""
        self.setup()
        self.root.mainloop()

    def setup(self):
        """Setup the GUI"""
        self.root = tk.Tk()
        self.root.title('Texty | Updating')
        self.root.geometry('+500+500')
        self.theme = ttk.Style(self.root)
        self.theme.theme_use(Texty.root_theme)
        self.download_version()

    def def_gui(self):
        """Define the GUI"""
        import version
        if version.version > __texty_version__:
            self.descrp_label = ttk.Label(self.root, text=version.description)
            self.install_button = ttk.Button(self.root, text='Update', command=lambda: self.install())
            self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self.quit())
        elif version.version == __texty_version__:
            mbox.showinfo('Texty Up-to-date', 'There is no update available. Check back soon!', parent=self.root)
            self.quit()
        else:
            print('Error: version=' + version.version)
            
    def quit(self):
        """Quit the Store"""
        self.root.quit()
        self.root.destroy()
        os.remove('version.py')
                                      
    def download_version(self):
        """Download version file"""
        
        def download_and_quit(self):
            """Download (and import) version and close the window"""
            version_url = 'https://raw.githubusercontent.com/Jackkillian/JK-Texty/master/Newest-Version/Code/version.py'
            download(version_url, filename='version.py')
            root.quit()
            root.destroy()
            self.def_gui()
            
        root = tk.Tk()
        root.title('Texty | Checking For Updates')
        dscrp = tk.Label(root, text='Checking for updates...')
        dscrp.grid(row=1, column=0)
        prbar = ttk.Progressbar(root, mode='indeterminate', value=1, maximum=1)
        prbar.start()
        prbar.grid(row=2, column=0)
        root.after(5000, func=lambda:download_and_quit(self))
        root.mainloop()

    def grid_gui(self):
        """Grid the GUI"""
        self.descrp_box.grid(row=1, column=0)
        self.install_button.grid(row=2, column=0)
        self.quit_button.grid(row=3, column=0)

    def install(self):
        """Install the new update"""
        import version
        url = version.url
        filename = dirname(__file__) + 'Updating Texty.py'
        self.descrp_label.config(text='Donwloading update...')
        try:
            download(url, filename=filename)
            nf = open('Updating Texty.py', 'r')
            of = open('Texty.py', 'w')
            of.write(nf.read())
            of.close()
            nf.close()
            os.remove('Updating Texty.py')
            mbox.showinfo('Texty Updated', 'Texty has been updated. Please restart Texty now.', parent=self.root)
        except urllib.error.HTTPError:
            mbox.showerror('File Not Found', 'The update file was not found, or you may not have an internet connection. We are sorry for the inconvience.', parent=self.root)
        except:
            mbox.showerror('Unknown Error', 'There was an unknown error. Please try again later.', parent=self.root)
    
class Texty_Store():
    """Open the Texty Store"""
    
    def __init__(self):
        """Open the Texty Store"""
        self.setup()
        self.root.mainloop()

    def setup(self):
        """Setup the GUI"""
        self.root = tk.Tk()
        self.root.title('Texty | Store')
        self.root.geometry('+500+500')
        self.theme = ttk.Style(self.root)
        self.theme.theme_use(Texty.root_theme)
        self.download_index()

    def def_gui(self):
        """Define the GUI"""
        self.update_descrp_button = ttk.Button(self.root, text='Get Description', command=lambda: self._update_description())
        self.descrp_label = ttk.Label(self.root, text='You have not selected a add-on yet.')
        self.install_button = ttk.Button(self.root, text='Install Add-On', command=lambda: self.install())
        self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self.quit())
        import index
        if index.store_status == 'True':
            self.store_list = ttk.Treeview(self.root)
            for catagory in index.index_list:
                if catagory == 'all_index':
                    self.store_list.insert('', 'end', catagory, text=index.index_list[catagory])
            for add_on in index.all_index:
                self.store_list.insert('all_index', 'end', add_on, text=add_on)
            self.grid_gui()
        elif index.store_status == 'Empty':
            mbox.showerror('Store is empty', 'The JK Texty Store has no add-ons yet. Please check again soon!', parent=self.root)
            self.quit()
        elif index.store_status == 'False':
            mbox.showerror('Error', index.false_description, parent=self.root)
            self.quit()
        elif index.store_status == 'Discontinued':
            # This will probaly not ever happen
            mbox.showerror('Store Discontinued', index.discontinued_description, parent=self.root)
            self.quit()
        else:
            mbox.showerror('Unknown Store Status', 'JK Texty Store has recieved an unknown store staus. Here it is:\n'+index.store_status, parent=self.root)
            self.quit()
            
    def quit(self):
        """Quit the Store"""
        self.root.quit()
        self.root.destroy()
        os.remove('index.py')
                                      
    def download_index(self):
        """Download the store index with a GUI"""
        
        def download_and_quit(self):
            """Download (and import) index and close the window"""
            index_url = 'https://raw.githubusercontent.com/Jackkillian/JK-Texty/master/Store/Code/index.py'
            download(index_url, filename='index.py')
            root.quit()
            root.destroy()
            self.def_gui()
            
        root = tk.Tk()
        root.title('Texty | Store')
        dscrp = tk.Label(root, text='Downloading Store Index...')
        dscrp.grid(row=1, column=0)
        prbar = ttk.Progressbar(root, mode='indeterminate', value=1, maximum=1)
        prbar.start()
        prbar.grid(row=2, column=0)
        root.after(5000, func=lambda:download_and_quit(self))
        root.mainloop()

    def grid_gui(self):
        """Grid the GUI"""
        self.store_list.grid(row=3, column=0)
        self.update_descrp_button.grid(row=2, column=0)
        self.descrp_label.grid(row=1, column=0)
        self.install_button.grid(row=4, column=0)
        self.quit_button.grid(row=5, column=0)

    def install(self):
        """Install the selected add-on"""
        url = 'https://raw.githubusercontent.com/Jackkillian/JK-Texty/master/Store/Code/' + self.store_list.focus() + '.py'
        filename = dirname(__file__) + '/Add_Ons/' + self.store_list.focus() + '.py'
        try:
            download(url, filename=filename)
            with open("Texty.py") as f_old, open("Texty (writing for add-ons).py", "w") as f_new:
                for line in f_old:
                    f_new.write(line)
                    if '        #-# ADD-ONS #-#' in line:
                        f_new.write("   import Add_Ons." + self.store_list.focus() + " as " + self.store_list.focus() +"\n")
                    if '        #-# RUN ADD-ONS #-#' in line:
                        f_new.write("   if mode == '" + self.store_list.focus() + "\n            " + self.store_list.focus() + ".main()")
                f_new.close()
                f_new = open('Texty (writing for add-ons).py', 'r')
                texty_file = open('Texty.py', mode='w')
                for line in f_new:
                    texty_file.write(line)
                texty_file.close()
                os.remove(dirname(__file__) + 'Texty (writing for add-ons).py')
            mbox.showinfo('Installed', 'The selected add-on was installed.', parent=self.root)
        except urllib.error.HTTPError:
            mbox.showerror('File Not Found', 'The add-on file was not found, or you may not have an internet connection. We are sorry for the inconvience.', parent=self.root)
        except:
            mbox.showerror('Unknown Error', 'There was an unknown error. Please try again later.', parent=self.root)
            
    def _update_description(self):
        """Update the add-on description"""
        import index
        add_on = self.store_list.focus()
        if not add_on == '':
            try:
                self.descrp_label.configure(text=index.all_index[add_on])
            except KeyError:
                pass
        else:
            self.descrp_label.configure(text='No add-on selected')

class Texty():
    """Run Texty"""

    def __init__(self):
        """Run Texty"""
        self.setup()
        self.def_gui('all')
        self.grid_gui()
        self.root.mainloop()

    ############################
    # Definitions for __init__ #
    ############################
    
    def setup(self):
        """Setup Texty"""
        # Setup the main window
        self.root = tk.Tk()
        self.root.title('Texty | New File')
        # Setup the theme for the main window
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        Texty.root_theme = 'clam'
        # Define needed variables
        self.Texty_version = '1.0.0'
        self.Texty_author = 'Jackkillian, a.k.a. Jack Freund'
        self.Texty_license = 'MIT License'
        self.Texty_website = 'https://sites.google.com/view/jk-texty-website/home'
        self.Texty_os = 'Source Code'
        self.toolbar_status = 'same'
        self.open_filetypes=(('All Files', '.*'),
                             ('AppleScript', '.scpt'),
                             ('C', '.c'),
                             ('C++', '.cc'),
                             ('HTML', '.html'),
                             ('JK Dashboard Extension', '.jkbdext'),
                             ('JK PyApp', '.py'),
                             ('JavaScript', '.js'),
                             ('Markdown', '.md'),
                             ('Python', '.py'),
                             ('Python GUI App', '.py'),
                             ('Plain Text', '.txt'),
                             ('Rich Text', '.rtf'),
                             ('Ruby', '.rb'))
        self.save_filetypes=(('AppleScript', '.scpt'),
                             ('C', '.c'),
                             ('C++', '.cc'),
                             ('HTML', '.html'),
                             ('JK Dashboard Extension', '.jkbdext'),
                             ('JK PyApp', '.py'),
                             ('JavaScript', '.js'),
                             ('Markdown', '.md'),
                             ('Python', '.py'),
                             ('Python GUI App', '.py'),
                             ('Plain Text', '.txt'),
                             ('Rich Text', '.rtf'),
                             ('Ruby', '.rb'))

        self.mode_list=['AppleScript',
                        'C',
                        'C++',
                        'HTML',
                        'JK Dashboard Extension',
                        'JK PyApp',
                        'JavaScript',
                        'Markdown',
                        'Python',
                        'Python GUI App',
                        'Plain Text',
                        'Rich Text',
                        'Ruby']
        
    def def_gui(self, mode):
        """Define the GUI"""
        if mode == 'all':
            self.main_text_input = scrolledtext(self.root)
            self.main_text_input.insert(1.0, self._Texty_info())
            self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
            self.open_button = ttk.Button(self.root, text='Open', command=lambda: self._open())
            self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
            self.toggle_toolbar_button = ttk.Button(self.root, text='Toggle Toolbar', command=lambda: self._toggle_toolbar())
            self.store_button = ttk.Button(self.root, text='Store', command=lambda: self._store())
            self.mode_label = ttk.Label(self.root, text='Mode:')
            self.mode_combo = ttk.Combobox(self.root, values=self.mode_list)
            self.change_mode_button = ttk.Button(self.root, text='Change Mode', command=lambda: self._change_mode())
            self.check_for_updates_button = ttk.Button(self.root, text='Check For Updates', command=lambda: self._check_for_updates())
            self.settings_button = ttk.Button(self.root, text='Settings', command=lambda: self._settings())
            self.mode_creator_button = ttk.Button(self.root, text='Mode Creator', command=lambda: self._mode_creator())
        elif mode == 'toolbar':
            self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
            self.open_button = ttk.Button(self.root, text='Open', command=lambda: self._open())
            self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
            self.toggle_toolbar_button = ttk.Button(self.root, text='Toggle Toolbar', command=lambda: self._toggle_toolbar())
            self.store_button = ttk.Button(self.root, text='Store', command=lambda: self._store())
            self.mode_label = ttk.Label(self.root, text='Mode:')
            self.mode_combo = ttk.Combobox(self.root, values=self.mode_list)
            self.change_mode_button = ttk.Button(self.root, text='Change Mode', command=lambda: self._change_mode())
            self.check_for_updates_button = ttk.Button(self.root, text='Check For Updates', command=lambda: self._check_for_updates())
            self.settings_button = ttk.Button(self.root, text='Settings', command=lambda: self._settings())
            self.mode_creator_button = ttk.Button(self.root, text='Mode Creator', command=lambda: self._mode_creator())

    def grid_gui(self):
        """Grid the GUI"""
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=1, column=1)
        self.toggle_toolbar_button.grid(row=1, column=2)
        self.store_button.grid(row=1, column=3)
        self.quit_button.grid(row=1, column=4)
        self.main_text_input.grid(row=2, column=0, columnspan=6, rowspan=10)
        self.mode_label.grid(row=1, column=5)
        self.mode_combo.grid(row=1, column=7, columnspan=2)
        self.change_mode_button.grid(row=2, column=7)
        self.check_for_updates_button.grid(row=4, column=7)
        self.settings_button.grid(row=5, column=7)
        self.mode_creator_button.grid(row=3, column=7)
        
    ###########################
    # Definitions for def_gui #
    ###########################

    def _Texty_info(self):
        """Return Texty info"""
        info="JK Texty\nVersion: 1.0.0\nAuthor:  Jackkillian\nLicense: MIT License\nHave fun!\n(you can type in this box)"
        
        return info

    def _change_mode(self):
        """Change the Texty mode"""
        mode = self.mode_combo.get()
        # DO NOT CHANGE THE FOLLOWING LINES,
        # AS THEN YOUR ADD-ONS WILL NOT WORK.
        #-# ADD-ONS #-#
        import Add_Ons.AppleScript as AppleScript
        import Add_Ons.C as C
        #-# RUN ADD-ONS #-#
        if mode in self.mode_list:
            if mode == 'AppleScript':
                AppleScript.main()
            elif mode == 'C':
                C.main()
            #-# RUN ADD-ONS #-#
        else:
            mbox.showerror('Add-On not found', 'Please make sure the add-on you selected is intalled.', parent=self.root)
    def _toggle_toolbar(self):
        """Toggle the toolbar"""
        # I KNOW 'seperate' is mispelled
        if self.toolbar_status == 'same':
            self.ungrid_gui()
            self.redef_gui()
            self.regrid_gui()
            self.toolbar_status = 'seperate'
        elif self.toolbar_status == 'seperate':
            self.reungrid_gui()
            self.def_gui('toolbar')
            self.grid_gui()
            self.toolbar_root.destroy()
            self.toolbar_status = 'same'
            
    def _settings(self):
        """Launch Texty Settings"""
        self._Texty_settings()

    def _store(self):
        """Launch Texty Store"""
        Texty_Store()
    
    def _save(self):
        """Save a file"""
        path = fd.asksaveasfilename(title='Save as', parent=self.root, filetypes=self.save_filetypes)
        
        try:
            file = open(path, mode='w')
            file.write(self.main_text_input.get(1.0, tk.END))
            file.close()
            self.root.title('Texty | ' + path)
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
            self.root.title('Texty | '+ path)
        except:
            mbox.showerror('Error Opening File', 'There was an error opening your file. Please make sure you selected a file, not a folder.', parent=self.root)
        
    def _quit(self):
        """Quit Texty"""
        self.root.quit()
        self.root.destroy()
        try:
            self.toolbar_root.destroy()
            self.set_root.destroy()
        except:
            pass

    def _check_for_updates(self):
        """Text Updater"""
        Texty_Updater()

    def _mode_creator(self):
        """Texty Mode Creator"""
        Texty_mode_creator()

    def save_changes(self):
            """Save Texty Settings Changes"""
            self.root_theme.theme_use(self.tc.get())
            Texty.root_theme = self.tc.get()
            self.set_root.quit()
            self.set_root.destroy()

    def _Texty_settings(self):
        """Texty Settings"""
        self.set_root = tk.Tk()
        self.set_root.title('Texty | Settings')
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
        self.c_l = ttk.Label(self.set_root, text='———Credits———')
        self.c_l.pack()
        self.v_l = ttk.Label(self.set_root, text='JK Texty Version: ' + self.Texty_version)
        self.v_l.pack()
        self.a_l = ttk.Label(self.set_root, text='JK Texty Author: ' + self.Texty_author)
        self.a_l.pack()
        self.l_l = ttk.Label(self.set_root, text='JK Texty License: ' + self.Texty_license)
        self.l_l.pack()
        self.w_l = ttk.Label(self.set_root, text='JK Texty Website: ')
        self.w_l.pack()
        self.w_b = ttk.Button(self.set_root, text='JK Texty Website', command=lambda: open_url(self.Texty_website))
        self.w_b.pack()
        self.o_l = ttk.Label(self.set_root, text='JK Texty O.S. version: ' + self.Texty_os)
        self.o_l.pack()
        self.s_b = ttk.Button(self.set_root, text='Save Changes', command=lambda: self.save_changes())
        self.s_b.pack()
            
    ###################################
    # Definitions for _toggle_toolbar #
    ###################################

    def redef_gui(self):
        self.toolbar_root = tk.Tk()
        self.toolbar_root.title('Texty Toolbar')
        self.toolbar_theme = ttk.Style(self.toolbar_root)
        self.toolbar_theme.theme_use('clam')
        self.save_button = ttk.Button(self.toolbar_root, text='Save', command=lambda: self._save())
        self.open_button = ttk.Button(self.toolbar_root, text='Open', command=lambda: self._open())
        self.quit_button = ttk.Button(self.toolbar_root, text='Quit', command=lambda: self._quit())
        self.toggle_toolbar_button = ttk.Button(self.toolbar_root, text='Toggle Toolbar', command=lambda: self._toggle_toolbar())
        self.store_button = ttk.Button(self.toolbar_root, text='Store', command=lambda: self._store())
        self.mode_label = ttk.Label(self.toolbar_root, text='Mode:')
        self.mode_combo = ttk.Combobox(self.toolbar_root, values=self.mode_list)
        self.change_mode_button = ttk.Button(self.toolbar_root, text='Change Mode', command=lambda: self._change_mode())
        self.check_for_updates_button = ttk.Button(self.toolbar_root, text='Check For Updates', command=lambda: self._check_for_updates())
        self.settings_button = ttk.Button(self.toolbar_root, text='Settings', command=lambda: self._settings())
        self.mode_creator_button = ttk.Button(self.toolbar_root, text='Mode Creator', command=lambda: self._mode_creator())

    def regrid_gui(self):
        self.save_button.grid(row=1, column=0)
        self.open_button.grid(row=2, column=0)
        self.toggle_toolbar_button.grid(row=3, column=0)
        self.store_button.grid(row=4, column=0)
        self.quit_button.grid(row=5, column=0)
        self.mode_label.grid(row=6, column=0)
        self.mode_combo.grid(row=7, column=0)
        self.change_mode_button.grid(row=8, column=0)
        self.mode_creator_button.grid(row=9, column=0)
        self.check_for_updates_button.grid(row=10, column=0)
        self.settings_button.grid(row=11, column=0)
    
    def reungrid_gui(self):
        self.save_button.grid_forget()
        self.open_button.grid_forget()
        self.toggle_toolbar_button.grid_forget()
        self.store_button.grid_forget()
        self.quit_button.grid_forget()
        self.mode_label.grid_forget()
        self.mode_combo.grid_forget()
        self.change_mode_button.grid_forget()
        self.check_for_updates_button.grid_forget()
        self.settings_button.grid_forget()
        self.mode_creator_button.grid_forget()

    def ungrid_gui(self):
        self.save_button.grid_forget()
        self.open_button.grid_forget()
        self.toggle_toolbar_button.grid_forget()
        self.store_button.grid_forget()
        self.quit_button.grid_forget()
        self.mode_label.grid_forget()
        self.mode_combo.grid_forget()
        self.change_mode_button.grid_forget()
        self.check_for_updates_button.grid_forget()
        self.settings_button.grid_forget()
        self.mode_creator_button.grid_forget()

class Texty_mode_creator():
    """Run Texty Mode Creator"""

    def __init__(self):
        """Run Texty Mode Creator"""
        self.setup()
        self.def_gui()
        self.grid_gui()
        self.root.mainloop()

    ############################
    # Definitions for __init__ #
    ############################
    
    def setup(self):
        """Setup Texty Mode Creator"""
        # Setup the main window
        self.root = tk.Tk()
        self.root.title('Texty Mode Creator | New File')
        # Setup the theme for the main window
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use(Texty.root_theme)
        self.save_filetypes=(('JK Texty Add-On', '.py'),
                             ('Unverified JK Texty Add-On', '.unvpy'))
        self.mode_text_file = open('Add_Ons/template.py', mode='r')
        self.mode_text = self.mode_text_file.read()
        self.mode_text_file.close()

        
    def def_gui(self):
        """Define the GUI"""
        self.main_text_input = scrolledtext(self.root)
        self.main_text_input.insert(1.0, self.mode_text)
        self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save())
        self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit())
        self.docs_button = ttk.Button(self.root, text='Mode Creating Documentation', command=lambda: self._docs())

    def grid_gui(self):
        """Grid the GUI"""
        self.save_button.grid(row=1, column=0)
        self.quit_button.grid(row=1, column=1)
        self.main_text_input.grid(row=2, column=0, columnspan=6, rowspan=10)
        self.docs_button.grid(row=1, column=2)
        
    ###########################
    # Definitions for def_gui #
    ###########################
    
    def _save(self):
        """Save a file"""
        path = fd.asksaveasfilename(title='Save as', parent=self.root, filetypes=self.save_filetypes)
        def generate_key():
            key = ''
            for i in range(10):
                new_int = str(randint(0, 9))
                key += new_int
            return key

        try:
            file = open(path, mode='w')
            self.main_text_input.insert(8.0, 'JK Texty Verification Key: ' + str(generate_key()) + '\n' + 'JK Texty Verification Path: ' + str(path) + '\n')
            file.write(self.main_text_input.get(1.0, tk.END))
            file.close()
            self.root.title('Texty Mode Creator | ' + path)
        except:
            mbox.showerror('Error Saving File', 'There was an error saving your file. Please try a different directory.', parent=self.root)
       
    def _quit(self):
        """Quit Texty Mode Creator"""
        self.root.quit()
        self.root.destroy()

    def _docs(self):
        open_url('file://' + dirname(__file__) + '/Docs/Making an add-on.html')
                
if __name__ == '__main__':
    Texty()
