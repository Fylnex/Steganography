# from gui import GUI
from core import ImageProcessor, Encryption, Embedder, Extractor

if __name__ == "__main__":
    # Инициализация классов
    image_processor = ImageProcessor()
    encryption = Encryption()
    embedder = Embedder()
    extractor = Extractor()

    # Путь к изображению и данным
    image_path = "tests/image/pngwing.com.png"
    data_path = "tests/text/exam.txt"
    output_image_path = "output_image.png"
    password = "securepassword"

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
    with open("extracted_data.txt", "wb") as file:
        file.write(extracted_data)

