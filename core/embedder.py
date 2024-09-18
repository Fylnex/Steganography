import logging


class Embedder:
    """
    Класс для встраивания данных в изображение методом LSB.
    """

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def embed_data(self, image, data, password, encryption_class):
        """
        Встраивает зашифрованные данные в изображение с использованием метода LSB.

        :param image: Image object, изображение для встраивания
        :param data: bytes, данные для встраивания
        :param password: str, пароль для шифрования данных
        :param encryption_class: Encryption, класс для шифрования данных
        :return: Image object, модифицированное изображение
        """
        encrypted_data = encryption_class.encrypt_data(data, password)
        binary_data = ''.join(format(byte, '08b') for byte in encrypted_data)

        image_data = list(image.getdata())
        for i in range(len(binary_data)):
            pixel = list(image_data[i])
            pixel[0] = (pixel[0] & ~1) | int(binary_data[i])
            image_data[i] = tuple(pixel)

        image.putdata(image_data)
        self.logger.info("Data embedded successfully")
        return image
