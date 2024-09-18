# from gui import GUI
from core import ImageProcessor, Encryption, Embedder, Extractor
import os

if __name__ == "__main__":
    # Инициализация классов
    image_processor = ImageProcessor()
    encryption = Encryption()
    embedder = Embedder()
    extractor = Extractor()

    # Путь к изображению и данным
    image_path = "tests/image/pngwing.com.png" # Путь к изображению
    data_path = "tests/text/exam.txt" # Путь к текстовому файла
    output_image_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'modified_image.png') # Путь к выходному изображению
    password = "securepassword" # Пароль для шифрования и дешифрования

    # Чтение данных из файла
    with open(data_path, "rb") as file:
        data = file.read()

    # Загрузка изображения
    image = image_processor.load_image(image_path)

    # Встраивание данных в изображение
    modified_image = embedder.embed_data(image, data, password, encryption)
    image_processor.save_image(modified_image, output_image_path)

    # Извлечение данных из изображения
    extracted_data = extractor.extract_data(modified_image, password, encryption)



    # Сохранение извлеченных данных
    with open(os.path.join(os.path.expanduser('~'), 'Downloads', 'extracted_data.txt'), encoding="utf-8") as file:
        file.write(extracted_data)

