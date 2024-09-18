# from gui import GUI
from core import ImageProcessor, Encryption, Embedder, Extractor
import os

if __name__ == "__main__":
    # Инициализация классов
    image_processor = ImageProcessor()
    encryption = Encryption()
    embedder = Embedder()
    extractor = Extractor()

    # Путь к изображениям и данным
    image_path = "tests/image/pngwing.com.png"
    data_path = "tests/text/exam.txt"
    output_image_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'output_image.png')
    output_data_path = os.path.join(os.path.expanduser('~'), 'Downloads', "extracted_data.txt")
    password = "securepassword"

    # Чтение данных из файла с указанием кодировки
    with open(data_path, "r", encoding="utf-8") as file:
        text_data = file.read()
        data = text_data.encode('utf-8')  # Преобразуем текст в байты

    # Загрузка изображения
    image = image_processor.load_image(image_path)

    # Встраивание данных в изображение
    modified_image = embedder.embed_data(image, data, password, encryption)
    image_processor.save_image(modified_image, output_image_path)

    # Загрузка модифицированного изображения
    modified_image = image_processor.load_image(output_image_path)

    # Извлечение данных из изображения
    extracted_data = extractor.extract_data(modified_image, password, encryption)

    # Декодирование байтов в строку с использованием UTF-8
    extracted_text = extracted_data.decode('utf-8')

    # Сохранение извлеченных данных в файл с указанием кодировки
    with open(output_data_path, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print("Извлеченный текст:", extracted_text)

