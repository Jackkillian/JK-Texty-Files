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
from tkinter import font
from tkinter.scrolledtext import ScrolledText as scrolledtext
from webbrowser import open as open_url
from urllib.request import urlretrieve as download
from random import randint
import urllib
from os.path import dirname
import os
import sys
import smtplib as smtp
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

__texty_version__ = '1.0.1'

class About_Texty():

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('About Texty')
        self.credits = open('Add_Ons/credits.txt').read()
        self.license = open('Add_Ons/license.txt').read()
        ttk.Label(self.root, text='Credits:\n'+self.credits+'\nLicense:\n'+self.license).pack()
        ttk.Button(self.root, text='Close', command=lambda: self.quit()).pack()

    def quit(self):
        self.root.quit()
        self.root.destroy()
        
class Texty_Config():
    pass

class Setup_Texty():
    """Launch Texty"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Launching JK Texty...')
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        self.email_providers = {'Gmail' : 'smtp.gmail.com',
                                'Outlook.com/Hotmail.com' : 'smtp-mail.outlook.com',
                                'Yahoo! Mail' : 'smtp.mail.yahoo.com',
                                'AT&T' : 'smtp.mail.att.net',
                                'Comcast' : 'smtp.comcast.net',
                                'Verizon' : 'smtp.verizon.net'}
        
        self.email_providers_list = ['Gmail',
                                     'Outlook.com/Hotmail.com',
                                     'Yahoo! Mail',
                                     'AT&T',
                                     'Comcast',
                                     'Verizon']
        try:
            username = open(str(dirname(__file__)) + '/Texty_config/username.txt', mode='r')
            Texty_Config.username = username.read()
            username.close()
            email = open(str(dirname(__file__)) + '/Texty_config/email.txt', mode='r')
            Texty_Config.email = email.read()
            email.close()
            email_provider = open(str(dirname(__file__) + '/Texty_config/email_server.txt'), mode='r')
            Texty_Config.email_server = email_provider.read()
            email_provider.close()
            url = 'https://raw.githubusercontent.com/Jackkillian/JK-Texty/master/Code/users.py'
            filename = dirname(__file__) + '/Texty_config/users.py'
            download(url, filename)
            import Texty_config.users as users
            if Texty_Config.username == users.notify_user:
                mbox.showinfo('New Message', 'You have recieved a message from the JK Texty caretaker(s): ' + users.notify_msg, parent=self.root)
            self.quit()
            Texty()
                
        except FileNotFoundError:
            mbox.showerror('Texty not configured', 'You have not configured Texty yet. Let\'s configure it now.', parent=self.root)
            try:
                os.mkdir(dirname(__file__) + '/Texty_config')
            except:
                pass
            try:
                url = 'https://raw.githubusercontent.com/Jackkillian/JK-Texty/master/Code/users.py'
                filename = dirname(__file__) + '/Texty_config/users.py'
                download(url, filename)
                import Texty_config.users as users
                self.setup()
            except urllib.error.HTTPError:
                # Users not connected to internet, or server's down
                self.quit()
                Texty()

    def setup(self):
        self.root = tk.Tk()
        self.root.title('Setting Up JK Texty...')
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        usnm_label = ttk.Label(self.root, text='Create a JK Texty username:')
        usnm_label.pack()
        self.usnm = ttk.Entry(self.root)
        self.usnm.pack()
        email_label = ttk.Label(self.root, text='Enter your email: (when you create add-ons, this email will be used to notify you)')
        email_label.pack()
        self.email_ = ttk.Entry(self.root)
        self.email_.pack()
        self.e_s_c_l = ttk.Label(self.root, text='Choose your email server:')
        self.e_s_c_l.pack()
        self.e_s_c = ttk.Combobox(self.root, values=self.email_providers_list)
        self.e_s_c.pack()
        continue_b = ttk.Button(self.root, text='Save and Continue', command=lambda: self.continue_())
        continue_b.pack()
        self.root.mainloop()
        
    def continue_(self):
        import Texty_config.users as users
        try:
            self.email_server = self.email_providers[self.e_s_c.get()]
        except:
            self.email_server = self.e_s_c.get()
        self.emladdr = self.email_.get()
        self.usrnm = self.usnm.get()
        if self.usrnm in users.all_users:
            mbox.showerror('Username already taken', 'That username has already been taken. Please try a different one.', parent=self.root)
            self.root.destroy()
            self.setup()
        else:
            self.root.destroy()
            self.root = tk.Tk()
            self.root.title('Setting Up JK Texty...')
            self.root_theme = ttk.Style(self.root)
            self.root_theme.theme_use('clam')
            self.d_l = ttk.Label(self.root, text='Setting up and saving data...')
            self.d_l.pack()
            username = open(str(dirname(__file__)) + '/Texty_config/username.txt', mode='w')
            username.write(self.usrnm)
            Texty_Config.username = self.usrnm
            username.close()
            email = open(str(dirname(__file__)) + '/Texty_config/email.txt', mode='w')
            email.write(self.emladdr)
            Texty_Config.email = self.emladdr
            email.close()
            email_provider = open(str(dirname(__file__)) + '/Texty_config/email_server.txt', mode='w')
            email_provider.write(self.email_server)
            Texty_Config.email_server = self.email_server
            email_provider.close()
            self.d_l.config(text='You now need to enter your email password,\nso that JK Texty can verify your username.\n(Don\'t worry, it will not be saved. Check the code if you want!)')
            self.p_l = ttk.Entry(self.root, show='•')
            self.p_l.pack()
            c_b = ttk.Button(self.root, text='Continue', command=lambda: self.continue__())
            c_b.pack()
            self.root.mainloop()

    def continue__(self):
        psswd = self.p_l.get()
        Texty_Config.password = psswd
        self.root.destroy()
        self.root = tk.Tk()
        self.root.title('Setting Up JK Texty...')
        self.root_theme = ttk.Style(self.root)
        self.root_theme.theme_use('clam')
        self.d_l = ttk.Label(self.root, text='Sending username to JK Texty...')
        self.d_l.pack()
        try:
            self.d_l.config(text='Connecting to server...')
            server = smtp.SMTP(self.email_server)
            server.ehlo()
            self.d_l.config(text='Starting TLS...')
            server.starttls()
            self.d_l.config(text='Logging in to server...')
            try:
                server.login(self.emladdr, psswd)
                self.d_l.config(text='Sending new user message...')
                try:
                    msg = MIMEMultipart()
                    msg['From'] = self.usrnm + '@nowhere.com'
                    msg['To'] = 'jka.freund@gmail.com'
                    msg['Subject'] = 'JK Texty - New User! - ' + self.usrnm
                    body = 'New User\'s Username: ' + self.usrnm + '\nFrom JK Texty'
                    msg.attach(MIMEText(body, 'plain'))
                    server.sendmail(self.usrnm + '@nowhere.com', 'jka.freund@gmail.com', msg.as_string())
                    self.d_l.config(text='Closing server...')
                    server.quit()
                    mbox.showinfo('Success!', 'Everything is setup. You will be notified (on Texty, not on your email) when your username is added.', parent=self.root)
                    self.quit()
                    Texty()
                except:
                    mbox.showerror('Error', 'There was an error sending the message. Please make sure you have an internet connection.', parent=self.root)
            except smtp.SMTPAuthenticationError:
                mbox.showerror('Incorrect creditentails', 'Your email address or password was incorrect.', parent=self.root)
                self.setup()
        except socket.gaierror:
            mbox.showerror('Unknown Email Hoster', 'Sorry, but the email provider you selected is not known. Please make sure it is correct.', parent=self.root)

    def quit(self):
        self.root.quit()
        self.root.destroy()
        try:
            os.remove(dirname(__file__) + '/Texty_config/users.py')
        except:
            pass
        
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
                        f_new.write("   elif mode == '" + self.store_list.focus() + "':\n            " + self.store_list.focus() + ".main()")
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
        # Setup menubar
        self.menubar = tk.Menu(self.root)
        ### Texty menu
        self.Texty_menu = tk.Menu(self.menubar)
        self.Texty_menu.add_command(label="About", command=lambda:About_Texty())
        self.Texty_menu.add_command(label="Settings", command=lambda:self._Texty_settings())
        self.Texty_menu.add_command(label="Check for updates", command=lambda:self._check_for_updates())
        self.Texty_menu.add_command(label="Quit", command=lambda:self._quit())
        ### File menu
        self.file_menu = tk.Menu(self.menubar)
        self.file_menu.add_command(label="New", command=lambda:Texty())
        self.file_menu.add_command(label="Save", command=lambda:self._save())
        self.file_menu.add_command(label="Open", command=lambda:self._open())
        ### Edit menu
        self.edit_menu = tk.Menu(self.menubar)
        ### Mode menu
        self.mode_menu = tk.Menu(self.menubar)
        ### Help menu
        self.help_menu = tk.Menu(self.menubar)
        self.help_menu.add_command(label="What's new in 1.0.0", command=lambda:open_url("https://github.com/Jackkillian/JK-Texty/blob/master/Newest-Version/What's%20New.md"))
        self.help_menu.add_command(label="Texty Help", command=lambda:open_url('https://github.com/Jackkillian/JK-Texty/wiki'))
        ### Rest of menubar
        self.menubar.add_cascade(label='Texty', menu=self.Texty_menu)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menubar.add_cascade(label="Mode", menu=self.mode_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)
        self.root.config(menu=self.menubar)
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
                        'JavaScript',
                        'JK Dashboard Extension',
                        'JK PyApp',
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
            self.font_frame = ttk.Labelframe(self.root, text='Font Options')
            self.font_combo = ttk.Combobox(self.font_frame, values=font.families())
            self.font_button = ttk.Button(self.font_frame, text='Change Font', command=lambda: self._change_font())
            self.font_size = ttk.Spinbox(self.font_frame, from_=1, to=100)
            self.font_opt = ttk.Combobox(self.font_frame, values=('normal', 'bold', 'italic', 'bold italic'))
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
            self.font_frame = ttk.Labelframe(self.root, text='Font Options')
            self.font_combo = ttk.Combobox(self.font_frame, values=font.families())
            self.font_button = ttk.Button(self.font_frame, text='Change Font', command=lambda: self._change_font())
            self.font_size = ttk.Spinbox(self.font_frame, from_=1, to=100)
            self.font_opt = ttk.Combobox(self.font_frame, values=('normal', 'bold', 'italic', 'bold italic'))
        self._words=open( "Add_Ons/wordlist.txt").read().split("\n")
        self.main_text_input.bind("<space>", self.Spellcheck)
        self.main_text_input.tag_configure("misspelled", foreground="red", underline=True)

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
        self.font_frame.grid(row=6, column=7)
        self.font_combo.grid(row=1, column=0)
        self.font_button.grid(row=4, column=0)
        self.font_size.grid(row=2, column=0)
        self.font_opt.grid(row=3, column=0)
        
    ###########################
    # Definitions for def_gui #
    ###########################

    def Spellcheck(self, event):
        '''Spellcheck the word preceeding the insertion point'''
        index = self.main_text_input.search(r'\s', "insert", backwards=True, regexp=True)
        if index == "":
            index ="1.0"
        else:
            index = self.main_text_input.index("%s+1c" % index)
        word = self.main_text_input.get(index, "insert")
        if word.islower() and word.isalpha():
            if word in self._words:
                self.main_text_input.tag_remove("misspelled", index, "%s+%dc" % (index, len(word)))
            else:
                self.main_text_input.tag_add("misspelled", index, "%s+%dc" % (index, len(word)))

    def _change_font(self):
        """Change the font"""
        size = self.font_size.get()
        if self.font_size.get() == '':
            size = 12
        self.main_text_input.config(font=(self.font_combo.get(), size, self.font_opt.get()))
        
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
        import Add_Ons.CC as CC
        import Add_Ons.HTML as HTML
        import Add_Ons.JavaScript as JavaScript
        import Add_Ons.JK_Dashboard_Extension as JK_Dashboard_Extension
        import Add_Ons.JK_PyApp as JK_PyApp
        import Add_Ons.Markdown as Markdown
        import Add_Ons.Python as Python
        import Add_Ons.Python_GUI_App as Python_GUI_App
        import Add_Ons.Plain_Text as Plain_Text
        import Add_Ons.Rich_Text as Rich_Text
        import Add_Ons.Ruby as Ruby
        #-# RUN ADD-ONS #-#
        if mode == 'AppleScript':
            AppleScript.main()
        elif mode == 'C':
            C.main()
        elif mode == 'C++':
            CC.main()
        elif mode == 'HTML':
            HTML.main()
        elif mode == 'JavaScipt':
            JavaScript.main()
        elif mode == 'JK Dashboard Extension':
            JK_Dashboard_Extension.main()
        elif mode == 'JK PyApp':
            JK_PyApp.main()
        elif mode == 'Markdown':
            Markdown.main()
        elif mode == 'Python':
            Python.main()
        elif mode == 'Python GUI App':
            Python_GUI_App.main()
        elif mode == 'Plain Text':
            Plain_Text.main()
        elif mode == 'Rich Text':
            Rich_Text.main()
        elif mode == 'Ruby':
            Ruby.main()
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
        Texty_mode_creator.def_gui(Texty_mode_creator)

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
        self.font_frame = ttk.Labelframe(self.toolbar_root, text='Font Options')
        self.font_combo = ttk.Combobox(self.font_frame, values=font.families())
        self.font_button = ttk.Button(self.font_frame, text='Change Font', command=lambda: self._change_font())
        self.font_size = ttk.Spinbox(self.font_frame, from_=1, to=100)
        self.font_opt = ttk.Combobox(self.font_frame, values=('normal', 'bold', 'italic', 'bold italic'))

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
        self.font_frame.grid(row=12, column=0)
    
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
        self.font_frame.grid_forget()

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
        self.font_frame.grid_forget()
        
class Texty_mode_creator():
    """Run Texty Mode Creator"""

    def __init__(self):
        """Run Texty Mode Creator"""
        self.setup()
        self.def_gui()

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
        self.main_text_input = scrolledtext(self.root)
        self.main_text_input.insert(1.0, self.mode_text)
        self.save_button = ttk.Button(self.root, text='Save', command=lambda: self._save(self))
        self.quit_button = ttk.Button(self.root, text='Quit', command=lambda: self._quit(self))
        self.docs_button = ttk.Button(self.root, text='Mode Creating Documentation', command=lambda: self._docs(self))
        self.publish_button = ttk.Button(self.root, text='Publish', command=lambda: self._publish(self))
        self.font_combo = ttk.Combobox(self.root, values=font.families())
        self.font_button = ttk.Button(self.root, text='Change Font', command=lambda: self._change_font(self))
        self.font_size = ttk.Spinbox(self.root, from_=1, to=100)
        self.font_opt = ttk.Combobox(self.root, values=('normal', 'bold', 'italic', 'bold italic'))
        self.grid_gui(self)
        self.root.mainloop()

    def grid_gui(self):
        """Grid the GUI"""
        self.main_text_input.grid(row=2, column=0, columnspan=4, rowspan=10)
        self.save_button.grid(row=1, column=0)
        self.quit_button.grid(row=1, column=1)
        self.docs_button.grid(row=1, column=2)
        self.publish_button.grid(row=1, column=3)
        self.font_combo.grid(row=1, column=4)
        self.font_button.grid(row=2, column=4)
        self.font_size.grid(row=3, column=4)
        self.font_opt.grid(row=4, column=4)
        
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
            if path.endswith('.py'):
                self.main_text_input.insert(8.0, 'JK Texty Verification Key: ' + str(generate_key()))
            elif path.endswith('.unvpy'):
                self.main_text_input.insert(8.0, 'JK Texty Nonverification Key: ' + str(generate_key()))
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
        """Open some documentation"""
        open_url('file://' + dirname(__file__) + '/Docs/Making an add-on.html')

    def _change_font(self):
        """Change the font"""
        self.main_text_input.config(font=(self.font_combo.get(), self.font_size.get(), self.font_opt.get()))
        
    def _publish(self):
        """Publish the add-on"""
        self.setup(self)

    def setup(self):
        self.continue_(self)
        
    def continue_(self):
        self.nroot = tk.Tk()
        self.nroot.title('Publishing code...')
        self.nroot_theme = ttk.Style(self.nroot)
        self.nroot_theme.theme_use('clam')
        self.d_l = ttk.Label(self.nroot, text='You now need to enter your email password,\nso that JK Texty can send your code.\n(Don\'t worry, it will not be saved. Check the code if you want!)')
        self.d_l.pack()
        self.p_l = ttk.Entry(self.nroot, show='•')
        self.p_l.pack()
        c_b = ttk.Button(self.nroot, text='Continue', command=lambda: self.continue__(self))
        c_b.pack()
        self.root.mainloop()

    def continue__(self):
        psswd = self.p_l.get()
        emladdr = Texty_Config.email
        email_server = Texty_Config.email_server
        usrnm = Texty_Config.username
        self.usrnm = usrnm
        self.nroot.destroy()
        self.nroot = tk.Tk()
        self.nroot.title('Sending code...')
        self.nroot_theme = ttk.Style(self.nroot)
        self.nroot_theme.theme_use('clam')
        self.d_l = ttk.Label(self.nroot, text='')
        self.d_l.pack()
        try:
            self.d_l.config(text='Connecting to server...')
            server = smtp.SMTP(email_server)
            server.ehlo()
            self.d_l.config(text='Starting TLS...')
            server.starttls()
            self.d_l.config(text='Logging in to server...')
            try:
                server.login(emladdr, psswd)
                self.d_l.config(text='Sending code message...')
                try:
                    msg = MIMEMultipart()
                    msg['From'] = usrnm + '@nowhere.com'
                    msg['To'] = 'jka.freund@gmail.com'
                    msg['Subject'] = 'JK Texty - New Add-On Submission!'
                    body = usrnm + '\'s code: \n' + self.main_text_input.get(1.0, 'end') + '\nFrom JK Texty'
                    msg.attach(MIMEText(body, 'plain'))
                    server.sendmail(usrnm + '@nowhere.com', 'jka.freund@gmail.com', msg.as_string())
                    self.d_l.config(text='Closing server...')
                    server.quit()
                    mbox.showinfo('Success!', 'You will be notified (on Texty, not on your email) when your code is published.', parent=self.nroot)
                    self.quit()
                except:
                    mbox.showerror('Error', 'There was an error sending the message. Please make sure you have an internet connection.', parent=self.nroot)
            except smtp.SMTPAuthenticationError:
                mbox.showerror('Incorrect creditentails', 'Your email address or password was incorrect.', parent=self.nroot)
                self.setup()
        except socket.gaierror:
            mbox.showerror('Unknown Email Hoster', 'Sorry, but the email provider you selected is not known. Please make sure it is correct.', parent=self.nroot)

    def quit(self):
        self.nroot.quit()
        self.nroot.destroy()
        try:
            os.remove(dirname(__file__) + '/Texty_config/users.py')
        except:
            pass
                
if __name__ == '__main__':
    Setup_Texty()
