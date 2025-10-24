import customtkinter as ctk
from config.styling import FONTS, PADDING

class ProgressManager:
    def __init__(self, parent):
        self.parent = parent
        self._dot_anim_job = None
        self._dot_base_msg = None
        self._dot_index = 0
        
        self.create_progress_frame()
        
    def create_progress_frame(self):
        """Create progress frame with fixed height"""
        self.progress_frame = ctk.CTkFrame(self.parent, height=60)
        self.progress_frame.grid_propagate(False)  # Prevent frame from shrinking
        self.progress_frame.grid_columnconfigure(0, weight=1)
        
        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            self.progress_frame,
            orientation="horizontal",
            height=20,
            corner_radius=10
        )
        self.progress_bar.set(0)
        self.progress_bar.grid(row=0, column=0, sticky="ew", padx=20, pady=(10, 5))
        
        # Progress label
        self.progress_label = ctk.CTkLabel(
            self.progress_frame,
            text="",
            font=FONTS["subtitle"],
            text_color="#2c3e50"
        )
        self.progress_label.grid(row=1, column=0, pady=(0, 10))
        
        # Hide initially
        self.progress_frame.grid_remove()
    
    def show(self):
        """Show progress frame"""
        self.progress_frame.grid()
        self.progress_frame.update_idletasks()
    
    def hide(self):
        """Hide progress frame"""
        self._stop_dot_animation()
        self.progress_frame.grid_remove()
    
    def update(self, message, value=None):
        """Update progress label and bar"""
        if message is not None and isinstance(message, str) and message.endswith('...'):
            base = message.rstrip('.')
            self._start_dot_animation(base)
        else:
            self._stop_dot_animation()
            self.progress_label.configure(text=message)

        if value is not None:
            self.progress_bar.set(value / 100.0)
        
        self.parent.update_idletasks()
    
    def _start_dot_animation(self, base_message, interval_ms=400):
        """Start dot animation"""
        if self._dot_base_msg == base_message and self._dot_anim_job is not None:
            return

        self._stop_dot_animation()
        self._dot_base_msg = base_message
        self._dot_index = 0

        def _step():
            self._dot_index = (self._dot_index + 1) % 4
            dots = '.' * self._dot_index
            try:
                self.progress_label.configure(text=f"{self._dot_base_msg}{dots}")
            except Exception:
                pass
            self._dot_anim_job = self.parent.after(interval_ms, _step)

        _step()

    def _stop_dot_animation(self):
        """Stop dot animation"""
        try:
            if self._dot_anim_job is not None:
                self.parent.after_cancel(self._dot_anim_job)
        except Exception:
            pass
        self._dot_anim_job = None
        self._dot_base_msg = None
        self._dot_index = 0