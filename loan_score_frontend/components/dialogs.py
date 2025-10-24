import customtkinter as ctk
import sys
from config.styling import FONTS, PADDING

class CTkMessageBox(ctk.CTkToplevel):
    def __init__(self, title, message, parent=None, shutdown_on_ok=False):
        super().__init__()
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()
        self.grab_set()
        self.shutdown_on_ok = shutdown_on_ok
        self.parent = parent
        
        self.center_window()
        self.create_widgets(message)
        self.result = None
        
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self, message):
        # Message label
        message_label = ctk.CTkLabel(
            self, 
            text=message, 
            wraplength=380,
            font=FONTS["normal"]
        )
        message_label.pack(pady=20, padx=20, fill="both", expand=True)
        
        # OK button
        ok_button = ctk.CTkButton(
            self, 
            text="OK", 
            command=self.ok_click,
            **BUTTON_STYLES["primary"]
        )
        ok_button.pack(pady=10)
        
    def ok_click(self):
        if self.shutdown_on_ok and self.parent:
            self.parent.quit()
            self.parent.destroy()
            sys.exit(1)
        self.destroy()

class CTkInputDialog(ctk.CTkToplevel):
    def __init__(self, title, prompt, parent=None, initialvalue=None, minvalue=None):
        super().__init__()
        self.title(title)
        self.geometry("400x200")
        self.resizable(False, False)
        self.transient(parent)
        self.lift()
        self.grab_set()
        
        self.center_window()
        self.minvalue = minvalue
        self.result = None
        
        self.create_widgets(prompt, initialvalue)
        self.setup_bindings()
        
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self, prompt, initialvalue):
        # Prompt label
        prompt_label = ctk.CTkLabel(
            self, 
            text=prompt, 
            wraplength=380,
            font=FONTS["normal"]
        )
        prompt_label.pack(pady=10, padx=20)
        
        # Entry field
        self.entry_var = ctk.StringVar(value=str(initialvalue) if initialvalue else "")
        self.entry = ctk.CTkEntry(
            self, 
            textvariable=self.entry_var, 
            width=300,
            font=FONTS["normal"]
        )
        self.entry.pack(pady=10)
        self.entry.focus()
        
        # Button frame
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)
        
        ok_button = ctk.CTkButton(
            button_frame, 
            text="OK", 
            command=self.ok_click,
            width=120
        )
        ok_button.pack(side="left", padx=10)
        
        cancel_button = ctk.CTkButton(
            button_frame, 
            text="Cancel", 
            command=self.cancel_click,
            width=120
        )
        cancel_button.pack(side="left", padx=10)
        
    def setup_bindings(self):
        self.bind('<Return>', lambda e: self.ok_click())
        self.bind('<Escape>', lambda e: self.cancel_click())
        
    def ok_click(self):
        value = self.entry_var.get().strip()
        if value:
            try:
                if self.minvalue is not None:
                    float_value = float(value)
                    if float_value < self.minvalue:
                        self.show_error(f"Value must be at least {self.minvalue}")
                        return
                self.result = value
                self.destroy()
            except ValueError:
                self.show_error("Please enter a valid number")
                
    def cancel_click(self):
        self.result = None
        self.destroy()
        
    def show_error(self, message):
        error_label = ctk.CTkLabel(self, text=message, text_color="red")
        error_label.pack(pady=5)
        self.after(3000, error_label.destroy)

class PasswordDialog(ctk.CTkToplevel):
    def __init__(self, parent=None):
        super().__init__()
        self.title("Password Required")
        self.geometry("450x200")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        
        self.center_window()
        self.password_entered = None
        self.create_widgets()
        self.setup_bindings()
        
    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self):
        # Labels
        ctk.CTkLabel(self, text="This PDF is encrypted.", font=FONTS["subtitle"]).pack(pady=15)
        ctk.CTkLabel(self, text="Please enter the password:", font=FONTS["normal"]).pack()
        
        # Password entry
        self.password_var = ctk.StringVar()
        self.password_entry = ctk.CTkEntry(
            self, 
            textvariable=self.password_var, 
            show='*', 
            width=350,
            font=FONTS["normal"]
        )
        self.password_entry.pack(pady=15)
        self.password_entry.focus()
        
        # Buttons
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=15)
        
        ctk.CTkButton(
            button_frame, 
            text="OK", 
            command=self.on_ok, 
            width=130, 
            height=35
        ).pack(side="left", padx=15)
        
        ctk.CTkButton(
            button_frame, 
            text="Cancel", 
            command=self.on_cancel, 
            width=130, 
            height=35
        ).pack(side="left", padx=15)
        
    def setup_bindings(self):
        self.bind('<Return>', lambda e: self.on_ok())
        self.bind('<Escape>', lambda e: self.on_cancel())
        
    def on_ok(self):
        self.password_entered = self.password_var.get()
        self.destroy()
        
    def on_cancel(self):
        self.password_entered = None
        self.destroy()