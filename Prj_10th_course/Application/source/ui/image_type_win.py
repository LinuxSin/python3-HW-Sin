import customtkinter as ctk
from tkinter import messagebox
from internal.command_handler import Command_handler

class ImageTypeWin(ctk.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.title("Выбор типа изображений")
        self.geometry("300x200")
        self.resizable(False, False)
        
        # Делаем окно модальным после отображения
        self.after(100, self._make_modal)
        
        self._create_widgets()
    
    def _make_modal(self):
        self.grab_set()
        self.focus_set()
    
    def _create_widgets(self):
        ctk.CTkLabel(self, text="Выберите тип изображений:").pack(pady=10)
        
        # Кнопка для загруженных изображений
        ctk.CTkButton(
            self,
            text="Загруженные",
            command=lambda: self._show_images(Command_handler().get_images())
        ).pack(pady=5)
        
        # Кнопка для сгенерированных изображений
        ctk.CTkButton(
            self,
            text="Сгенерированные",
            command=lambda: self._show_images(Command_handler().get_generated_images())
        ).pack(pady=5)
        
        # Кнопка для аугментированных изображений
        ctk.CTkButton(
            self,
            text="Аугментированные",
            command=lambda: self._show_images(Command_handler().get_augmentation_images())
        ).pack(pady=5)
    
    def _show_images(self, images):
        if images:
            from ui.gallery_win import Gallery_win
            Gallery_win(self.parent, images)
            self.destroy()
        else:
            messagebox.showwarning("Внимание", "Изображения данного типа отсутствуют")