import logging


class Extractor:
    """
    Класс для извлечения данных из изображения.
    """

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract_data(self, image, password, encryption_class):
        """
        Извлекает и дешифрует данные из изображения, закодированные с помощью метода LSB.

        :param image: Image object, изображение для извлечения данных
        :param password: str, пароль для дешифрования данных
        :param encryption_class: Encryption, класс для дешифрования данных
        :return: bytes, извлеченные и расшифрованные данные
        """
        image_data = list(image.getdata())
        binary_data = ''.join([str(pixel[0] & 1) for pixel in image_data])
        encrypted_data = int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder='big')

        decrypted_data = encryption_class.decrypt_data(encrypted_data, password)
        self.logger.info("Data extracted successfully")
        return decrypted_data
