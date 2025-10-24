import customtkinter as ctk

# Configure appearance
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Font configurations
FONTS = {
    "title": ("Helvetica", 16, "bold"),
    "subtitle": ("Arial", 12, "bold"),
    "normal": ("Arial", 11),
    "monospace": ("Courier", 11, "bold"),
    "small": ("Arial", 9, "italic"),
}

# Button styles
BUTTON_STYLES = {
    "primary": {
        "fg_color": "#4CAF50",
        "font": ("Arial", 10, "bold")
    },
    "secondary": {
        "fg_color": "#2196F3",
        "font": ("Arial", 10)
    },
    "danger": {
        "fg_color": "#f44336",
        "font": ("Arial", 10)
    },
    "warning": {
        "fg_color": "#ff9800",
        "font": ("Arial", 10)
    },
    "info": {
        "fg_color": "#9C27B0",
        "font": ("Arial", 10)
    }
}

# Layout constants
PADDING = {
    "small": 5,
    "medium": 10,
    "large": 15,
    "xlarge": 20
}