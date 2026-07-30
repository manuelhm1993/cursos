from abc import ABC, abstractmethod
import tkinter as tk

class ViewInterface(ABC):
    @abstractmethod
    def build_frame(self, master: tk.Tk) -> tk.Frame:
        pass