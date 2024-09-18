from PIL import Image
import logging


class ImageProcessor:
    """
    Класс для загрузки и сохранения изображений.
    Использует библиотеку Pillow для работы с изображениями.
    """

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def load_image(self, image_path):
        """
        Загрузка изображения с указанного пути.

        :param image_path: str, путь к изображению
        :return: Image object
        """
        try:
            image = Image.open(image_path)
            self.logger.info(f"Image loaded successfully from {image_path}")
            return image
        except Exception as e:
            self.logger.error(f"Error loading image: {str(e)}")
            raise e

    def save_image(self, image, output_path, format=None):
        """
        Сохранение изображения по указанному пути.

        :param image: Image object, изображение для сохранения
        :param output_path: str, путь для сохранения
        :param format: str, формат для сохранения (если не указано в пути)
        """
        try:
            # Проверяем, указано ли расширение в пути
            if not format:
                if "." in output_path:
                    format = output_path.split(".")[-1].upper()  # Получаем формат из расширения файла
                else:
                    format = "PNG"  # Если расширения нет, используем PNG по умолчанию
                    output_path += ".png"  # Добавляем расширение .png, если его нет

            image.save(output_path, format=format)
            self.logger.info(f"Image saved successfully at {output_path}")
        except Exception as e:
            self.logger.error(f"Error saving image: {str(e)}")
            raise e

    def convert_image(self, image, format):
        """
        Конвертация изображения в указанный формат.

        :param image: Image object, изображение для конвертации
        :param format: str, формат для конвертации (например, "PNG")
        :return: Image object
        """
        try:
            converted_image = image.convert(format)
            self.logger.info(f"Image converted to format {format}")
            return converted_image
        except Exception as e:
            self.logger.error(f"Error converting image: {str(e)}")
            raise e
