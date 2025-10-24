import threading
import logging

logger = logging.getLogger(__name__)

class ThreadManager:
    def __init__(self):
        self.active_threads = []
        self.cancelled = False
    
    def start_thread(self, target, args=(), daemon=True):
        """Start a new thread and track it"""
        thread = threading.Thread(target=target, args=args, daemon=daemon)
        thread.start()
        self.active_threads.append(thread)
        return thread
    
    def cancel_all(self):
        """Cancel all active threads"""
        self.cancelled = True
        for thread in self.active_threads:
            if thread.is_alive():
                # You might need more sophisticated cancellation logic
                pass
    
    def cleanup_thread(self, thread):
        """Remove thread from tracking"""
        if thread in self.active_threads:
            self.active_threads.remove(thread)
    
    def any_alive(self):
        """Check if any threads are still alive"""
        return any(thread.is_alive() for thread in self.active_threads)