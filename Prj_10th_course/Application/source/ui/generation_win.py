# import customtkinter as ctk
# from tkinter import messagebox
# from internal.command_handler import Command_handler

# class Generation_win(ctk.CTkToplevel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.title("Настройки генерации")
#         self.geometry("400x300")
        
#         # Поля для ввода параметров с значениями по умолчанию
#         self.img_size_label = ctk.CTkLabel(self, text="Размер изображения (ширина,высота):")
#         self.img_size_label.pack(pady=5)
#         self.img_size_entry = ctk.CTkEntry(self, placeholder_text="400,600")
#         self.img_size_entry.insert(0, "400,600")  # Значение по умолчанию
#         self.img_size_entry.pack(pady=5)
        
#         self.nof_imgs_label = ctk.CTkLabel(self, text="Количество изображений:")
#         self.nof_imgs_label.pack(pady=5)
#         self.nof_imgs_entry = ctk.CTkEntry(self, placeholder_text="1")
#         self.nof_imgs_entry.insert(0, "1")  # Значение по умолчанию
#         self.nof_imgs_entry.pack(pady=5)
        
#         self.nof_cells_label = ctk.CTkLabel(self, text="Количество ячеек:")
#         self.nof_cells_label.pack(pady=5)
#         self.nof_cells_entry = ctk.CTkEntry(self, placeholder_text="50")
#         self.nof_cells_entry.insert(0, "50")  # Значение по умолчанию
#         self.nof_cells_entry.pack(pady=5)
        
#         # Кнопка генерации
#         self.generate_btn = ctk.CTkButton(self, text="Сгенерировать", command=self.generate)
#         self.generate_btn.pack(pady=20)
    
#     def generate(self):
#         try:
#             # Получаем и проверяем размер изображения
#             img_size_str = self.img_size_entry.get().strip()
#             if not img_size_str:
#                 raise ValueError("Введите размер изображения")
            
#             try:
#                 img_size = tuple(map(int, img_size_str.split(',')))
#                 if len(img_size) != 2:
#                     raise ValueError("Размер должен быть в формате 'ширина,высота'")
#             except ValueError:
#                 raise ValueError("Некорректный формат размера изображения")
            
#             # Получаем и проверяем количество изображений
#             nof_imgs_str = self.nof_imgs_entry.get().strip()
#             if not nof_imgs_str:
#                 raise ValueError("Введите количество изображений")
#             nof_imgs = int(nof_imgs_str)
#             if nof_imgs <= 0:
#                 raise ValueError("Количество изображений должно быть больше 0")
            
#             # Получаем и проверяем количество ячеек
#             nof_cells_str = self.nof_cells_entry.get().strip()
#             if not nof_cells_str:
#                 raise ValueError("Введите количество ячеек")
#             nof_cells = int(nof_cells_str)
#             if nof_cells <= 0:
#                 raise ValueError("Количество ячеек должно быть больше 0")
            
#             # Вызываем функцию генерации
#             Command_handler().generate(img_size=img_size, nof_imgs=nof_imgs, nof_cells=nof_cells)
#             self.destroy()
            
#         except ValueError as e:
#             messagebox.showerror("Ошибка ввода", str(e))
#         except Exception as e:
#             messagebox.showerror("Ошибка генерации", f"Произошла ошибка: {str(e)}")


# import customtkinter as ctk
# from tkinter import messagebox
# from internal.command_handler import Command_handler

# class GenerationWin(ctk.CTkToplevel):
#     def __init__(self, parent, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.parent = parent
#         self.title("Настройки генерации")
#         self.geometry("400x300")
#         self.resizable(False, False)
        
#         # Переменные для хранения параметров
#         self.img_size = (400, 600)
#         self.nof_imgs = 1
#         self.nof_cells = 50
        
#         self._create_widgets()
    
#     def _create_widgets(self):
#         # Размер изображения
#         ctk.CTkLabel(self, text="Размер изображения (ширина,высота):").pack(pady=(10, 5))
#         self.size_entry = ctk.CTkEntry(self, placeholder_text="400,600")
#         self.size_entry.insert(0, "400,600")
#         self.size_entry.pack(pady=5)
        
#         # Количество изображений
#         ctk.CTkLabel(self, text="Количество изображений:").pack(pady=5)
#         self.num_imgs_entry = ctk.CTkEntry(self, placeholder_text="1")
#         self.num_imgs_entry.insert(0, "1")
#         self.num_imgs_entry.pack(pady=5)
        
#         # Количество ячеек
#         ctk.CTkLabel(self, text="Количество ячеек:").pack(pady=5)
#         self.num_cells_entry = ctk.CTkEntry(self, placeholder_text="50")
#         self.num_cells_entry.insert(0, "50")
#         self.num_cells_entry.pack(pady=5)
        
#         # Кнопки
#         btn_frame = ctk.CTkFrame(self)
#         btn_frame.pack(pady=15)
        
#         self.generate_btn = ctk.CTkButton(
#             btn_frame, 
#             text="Сгенерировать", 
#             command=self._generate_images
#         )
#         self.generate_btn.pack(side="left", padx=10)
        
#         self.cancel_btn = ctk.CTkButton(
#             btn_frame,
#             text="Отмена",
#             command=self.destroy,
#             fg_color="gray30"
#         )
#         self.cancel_btn.pack(side="right", padx=10)
    
#     def _generate_images(self):
#         try:
#             # Получаем и проверяем параметры
#             size_str = self.size_entry.get().strip()
#             if not size_str:
#                 raise ValueError("Введите размер изображения")
            
#             try:
#                 self.img_size = tuple(map(int, size_str.split(',')))
#                 if len(self.img_size) != 2:
#                     raise ValueError("Размер должен содержать ширину и высоту")
#             except ValueError:
#                 raise ValueError("Некорректный формат размера")
            
#             try:
#                 self.nof_imgs = int(self.num_imgs_entry.get())
#                 if self.nof_imgs <= 0:
#                     raise ValueError("Количество изображений должно быть > 0")
#             except ValueError:
#                 raise ValueError("Некорректное количество изображений")
            
#             try:
#                 self.nof_cells = int(self.num_cells_entry.get())
#                 if self.nof_cells <= 0:
#                     raise ValueError("Количество ячеек должно быть > 0")
#             except ValueError:
#                 raise ValueError("Некорректное количество ячеек")
            
#             # Вызываем генерацию через Command_handler
#             if Command_handler().generate(
#                 img_size=self.img_size,
#                 nof_imgs=self.nof_imgs,
#                 nof_cells=self.nof_cells
#             ):
#                 messagebox.showinfo("Успех", "Изображения успешно сгенерированы!")
#                 self.destroy()
            
#         except ValueError as e:
#             messagebox.showerror("Ошибка ввода", str(e))
#         except Exception as e:
#             messagebox.showerror("Ошибка генерации", str(e))

import customtkinter as ctk
from tkinter import messagebox
from internal.command_handler import Command_handler

class Generation_win(ctk.CTkToplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.title("Настройки генерации")
        self.geometry("400x300")
        
        # Откладываем grab_set до отображения окна
        self.after(100, self._make_modal)
        
        self._create_widgets()
    
    def _make_modal(self):
        """Делает окно модальным после его отображения"""
        self.grab_set()
        self.focus_set()
    
    def _create_widgets(self):
        # Размер изображения
        ctk.CTkLabel(self, text="Размер изображения (ширина,высота):").pack(pady=(10,5))
        self.size_entry = ctk.CTkEntry(self)
        self.size_entry.insert(0, "400,600")
        self.size_entry.pack(pady=5)
        
        # Количество изображений
        ctk.CTkLabel(self, text="Количество изображений:").pack()
        self.num_imgs_entry = ctk.CTkEntry(self)
        self.num_imgs_entry.insert(0, "1")
        self.num_imgs_entry.pack(pady=5)
        
        # Количество ячеек
        ctk.CTkLabel(self, text="Количество ячеек:").pack()
        self.num_cells_entry = ctk.CTkEntry(self)
        self.num_cells_entry.insert(0, "50")
        self.num_cells_entry.pack(pady=5)
        
        # Кнопка генерации
        self.generate_btn = ctk.CTkButton(
            self, 
            text="Сгенерировать", 
            command=self._generate_images
        )
        self.generate_btn.pack(pady=15)
    
   
    def _generate_images(self):
        try:
            img_size = tuple(map(int, self.size_entry.get().split(',')))
            nof_imgs = int(self.num_imgs_entry.get())
            nof_cells = int(self.num_cells_entry.get())
            
            if not Command_handler().generate(img_size, nof_imgs, nof_cells):
                raise Exception("Не удалось сгенерировать изображения")
                
            messagebox.showinfo("Успех", "Изображения сгенерированы!")
            self.destroy()
            
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", f"Проверьте введенные данные:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Ошибка генерации", str(e))