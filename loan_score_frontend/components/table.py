import customtkinter as ctk
from tkinter import ttk
from config.settings import COLOR_SCHEME
from config.styling import FONTS

class ResultsTable:
    def __init__(self, parent):
        self.parent = parent
        self.table_frame = ctk.CTkFrame(parent)
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.table_frame.grid_rowconfigure(0, weight=1)
        
        self.create_table()
        self.setup_style()
        
    def create_table(self):
        # Create tkinter frame for Treeview
        self.tk_table_frame = ttk.Frame(self.table_frame)
        self.tk_table_frame.grid(row=0, column=0, sticky="nsew")
        self.table_frame.grid_rowconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)
        
        # Create Treeview
        columns = ("Metric", "Value")
        self.treeview = ttk.Treeview(
            self.tk_table_frame, 
            columns=columns, 
            show="headings", 
            height=25
        )
        
        # Configure headings and columns
        self.treeview.heading("Metric", text="Metric", anchor="w")
        self.treeview.heading("Value", text="Value", anchor="w")
        self.treeview.column("Metric", width=300, anchor="w")
        self.treeview.column("Value", width=500, anchor="w")
        
        # Scrollbar
        self.scrollbar = ttk.Scrollbar(
            self.tk_table_frame, 
            orient="vertical", 
            command=self.treeview.yview
        )
        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        
        # Grid layout
        self.treeview.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        self.tk_table_frame.grid_rowconfigure(0, weight=1)
        self.tk_table_frame.grid_columnconfigure(0, weight=1)
        
    def setup_style(self):
        """Configure Treeview styling based on theme"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Get current theme
        if ctk.get_appearance_mode() == "Dark":
            bg_color = "#2b2b2b"
            fg_color = "white"
            heading_bg = "#3b3b3b"
        else:
            bg_color = "white"
            fg_color = "black"
            heading_bg = "#f0f0f0"
        
        # Configure styles
        style.configure("Treeview", 
                       background=bg_color,
                       foreground=fg_color,
                       fieldbackground=bg_color,
                       borderwidth=0)
        
        style.configure("Treeview.Heading", 
                       background=heading_bg,
                       foreground=fg_color,
                       relief="flat")
        
        style.map("Treeview", background=[('selected', '#4CAF50')])
        
        # Configure tags for color coding
        for section, color in COLOR_SCHEME.items():
            if section == "section_header":
                self.treeview.tag_configure(
                    section, 
                    background="", 
                    foreground=color, 
                    font=("Arial", 10, "bold")
                )
            elif section == "duration_warning":
                self.treeview.tag_configure(
                    section, 
                    background=color, 
                    foreground="#B71C1C", 
                    font=("Arial", 9, "bold")
                )
            else:
                self.treeview.tag_configure(section, background=color)
    
    def grid(self, **kwargs):
        """Delegate grid to table frame"""
        return self.table_frame.grid(**kwargs)
    
    def clear(self):
        """Clear all rows from table"""
        for row in self.treeview.get_children():
            self.treeview.delete(row)
    
    def update_data(self, data):
        """Update table with new data"""
        self.clear()
        
        for row in data:
            item_id = self.treeview.insert("", "end", values=(row[0], row[1]))
            if len(row) > 2 and row[2]:
                section = row[2]
                if section in COLOR_SCHEME:
                    self.treeview.item(item_id, tags=(section,))
    
    def get_children(self):
        """Delegate to treeview"""
        return self.treeview.get_children()
    
    def delete(self, item):
        """Delegate delete to treeview"""
        return self.treeview.delete(item)