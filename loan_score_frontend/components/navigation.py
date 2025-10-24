import customtkinter as ctk
from datetime import datetime
from config.styling import FONTS, PADDING
from config.settings import COMPANY_NAME

class Header:
    def __init__(self, parent):
        self.parent = parent
        self.create_header()
        
    def create_header(self):
        """Create header with status and date"""
        self.header_frame = ctk.CTkFrame(self.parent)
        self.header_frame.grid_columnconfigure(1, weight=1)
        
        # Connection status (left)
        self.connection_status = ctk.CTkLabel(
            self.header_frame, 
            text="🔴 Checking...", 
            font=FONTS["subtitle"],
            text_color="orange"
        )
        self.connection_status.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        
        # Current date (right)
        current_date = datetime.now().strftime("%A, %d %B %Y")
        self.date_label = ctk.CTkLabel(
            self.header_frame,
            text=f"📅 {current_date}",
            font=FONTS["normal"],
            text_color="#2c3e50"
        )
        self.date_label.grid(row=0, column=1, sticky="e", padx=5, pady=5)
    
    def grid(self, **kwargs):
        return self.header_frame.grid(**kwargs)
    
    def update_connection_status(self, connected, system_ok, message=""):
        """Update connection status display"""
        if connected:
            if system_ok:
                self.connection_status.configure(text="🟢 Connected", text_color="green")
            else:
                self.connection_status.configure(text="🟡 Connected (System Inactive)", text_color="orange")
        else:
            self.connection_status.configure(text="🔴 Disconnected", text_color="red")

class Footer:
    def __init__(self, parent):
        self.parent = parent
        self.create_footer()
        
    def create_footer(self):
        """Create footer with company name"""
        self.footer_label = ctk.CTkLabel(
            self.parent,
            text=COMPANY_NAME,
            font=FONTS["small"],
            text_color="gray"
        )
    
    def grid(self, **kwargs):
        return self.footer_label.grid(**kwargs)

class GuidePanel:
    def __init__(self, parent):
        self.parent = parent
        self.create_guide()
        
    def create_guide(self):
        """Create loan score guide panel"""
        self.guide_frame = ctk.CTkFrame(self.parent, fg_color="transparent")
        
        # Guide title
        self.guide_label = ctk.CTkLabel(
            self.guide_frame,
            text="Loan Score Guide",
            font=FONTS["subtitle"]
        )
        self.guide_label.pack(anchor="w", pady=(0, 5))
        
        # Score key content
        score_key = (
            "Score Range  | Interpretation         | Eligibility\n"
            "-------------| ---------------------- | -----------\n"
            " 0 -30%      | Low risk (good client) | ✅ Yes\n"
            "30 -70%      | Moderate risk          | ✅ Yes\n"
            "70 -100%     | High risk              | ❌ No"
        )
        
        # Text box for monospace font
        self.score_key_box = ctk.CTkTextbox(
            self.guide_frame,
            height=100,
            width=400,
            font=FONTS["monospace"],
            activate_scrollbars=False
        )
        self.score_key_box.insert("1.0", score_key)
        self.score_key_box.configure(state="disabled")
        self.score_key_box.pack()
    
    def grid(self, **kwargs):
        return self.guide_frame.grid(**kwargs)