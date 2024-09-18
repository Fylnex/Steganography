
from core import ImageProcessor, Encryption, Embedder, Extractor
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import os


class SteganographyApp:
   def __init__(self, root):
      self.root = root
      self.root.title("Steganography App")
      self.root.geometry("600x400")

      self.create_main_menu()

   def create_main_menu(self):
      """Создание главного меню с выбором действий."""
      # Удаляем все существующие виджеты
      for widget in self.root.winfo_children():
         widget.destroy()

      # Кнопки для выбора режима
      self.embed_button = tk.Button(self.root, text="Embed Data", command=self.embed_mode)
      self.embed_button.pack(pady=10)

      self.extract_button = tk.Button(self.root, text="Extract Data", command=self.extract_mode)
      self.extract_button.pack(pady=10)

   def embed_mode(self):
      """Открытие экрана для встраивания данных."""
      self.clear_screen()

      # Поля для встраивания данных
      self.image_label = tk.Label(self.root, text="Selected Image: None")
      self.image_label.pack(pady=5)
      self.select_image_button = tk.Button(self.root, text="Select Image", command=self.select_image)
      self.select_image_button.pack(pady=10)

      self.data_file_label = tk.Label(self.root, text="Selected Data File: None")
      self.data_file_label.pack(pady=5)
      self.select_data_button = tk.Button(self.root, text="Select Data File", command=self.select_data_file)
      self.select_data_button.pack(pady=10)

      # Кнопки для выполнения действия и возврата
      self.embed_button = tk.Button(self.root, text="Embed Data", command=self.perform_embedding)
      self.embed_button.pack(pady=10)

      self.back_button = tk.Button(self.root, text="Back", command=self.create_main_menu)
      self.back_button.pack(pady=10)

      # Поле для вывода статуса
      self.status_label = tk.Label(self.root, text="", fg="green")
      self.status_label.pack(pady=10)

   def extract_mode(self):
      """Открытие экрана для извлечения данных."""
      self.clear_screen()

      # Поля для извлечения данных
      self.image_label = tk.Label(self.root, text="Selected Image: None")
      self.image_label.pack(pady=5)
      self.select_image_button = tk.Button(self.root, text="Select Image", command=self.select_image)
      self.select_image_button.pack(pady=10)

      # Кнопки для выполнения действия и возврата
      self.extract_button = tk.Button(self.root, text="Extract Data", command=self.perform_extraction)
      self.extract_button.pack(pady=10)

      self.back_button = tk.Button(self.root, text="Back", command=self.create_main_menu)
      self.back_button.pack(pady=10)

      # Поле для вывода статуса
      self.status_label = tk.Label(self.root, text="", fg="green")
      self.status_label.pack(pady=10)

   def clear_screen(self):
      """Очищает экран, удаляя все виджеты."""
      for widget in self.root.winfo_children():
         widget.destroy()

   def perform_embedding(self):
      """Функция для выполнения процесса встраивания данных."""
      if self.image_path and self.data_file_path:
         try:
            # Чтение данных из файла
            with open(self.data_file_path, "r", encoding="utf-8") as file:
               data = file.read().encode('utf-8')

            # Инициализация классов
            image_processor = ImageProcessor()
            embedder = Embedder()

            # Загрузка изображения
            image = image_processor.load_image(self.image_path)

            # Встраивание данных в изображение
            modified_image = embedder.embed_data(image, data)

            # Сохранение модифицированного изображения
            output_image_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'output_image.png')
            image_processor.save_image(modified_image, output_image_path)

            self.status_label.config(text="Data embedded successfully!", fg="green")
         except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")
      else:
         messagebox.showerror("Error", "Please select image and data file.")

   def perform_extraction(self):
      """Функция для выполнения процесса извлечения данных."""
      if self.image_path:
         try:
            # Инициализация классов
            image_processor = ImageProcessor()
            extractor = Extractor()

            # Загрузка изображения
            image = image_processor.load_image(self.image_path)

            # Извлечение данных из изображения
            extracted_data = extractor.extract_data(image)

            # Декодирование байтов в строку
            extracted_text = extracted_data.decode('utf-8')

            # Сохранение извлеченных данных
            output_data_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'extracted_data.txt')
            with open(output_data_path, "w", encoding="utf-8") as file:
               file.write(extracted_text)

            self.status_label.config(text="Data extracted successfully!", fg="green")
            messagebox.showinfo("Extracted Data", f"Extracted data saved to {output_data_path}")
         except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")
      else:
         messagebox.showerror("Error", "Please select image.")

   def select_image(self):
      """Открытие диалогового окна для выбора изображения."""
      self.image_path = filedialog.askopenfilename(
         title="Select Image",
         filetypes=[("Image Files", "*.png;*.jpg;*.bmp")]
      )
      if self.image_path:
         self.image_label.config(text=f"Selected Image: {os.path.basename(self.image_path)}")

   def select_data_file(self):
      """Открытие диалогового окна для выбора файла с данными."""
      self.data_file_path = filedialog.askopenfilename(
         title="Select Data File",
         filetypes=[("Text Files", "*.txt")]
      )
      if self.data_file_path:
         self.data_file_label.config(text=f"Selected Data File: {os.path.basename(self.data_file_path)}")


if __name__ == "__main__":
   root = tk.Tk()
   app = SteganographyApp(root)
   root.mainloop()
