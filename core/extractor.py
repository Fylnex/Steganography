import logging


class Extractor:
    """
    Класс для извлечения данных из изображения с проверкой пароля.
    """

    def __init__(self):
        # Инициализация логгера
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract_data(self, image, input_password):
        """
        Извлекает данные из изображения с проверкой пароля.

        :param image: Image object, изображение для извлечения данных
        :param input_password: str, введенный пользователем пароль
        :return: bytes, извлеченные данные
        """
        pixels = list(image.getdata())
        bits = ''
        for pixel in pixels:
            for color in pixel[:3]:
                bits += str(color & 1)

        # Извлекаем длину данных (первые 64 бита)
        data_len_bits = bits[:64]
        data_len = int(data_len_bits, 2)

        # Извлекаем данные
        data_bits = bits[64:64 + data_len * 8]
        extracted_data_with_password = int(data_bits, 2).to_bytes(data_len, byteorder='big')

        # Извлекаем пароль (предположим, что длина пароля не превышает 64 байта)
        password_length = len(input_password.encode('utf-8'))
        extracted_password = extracted_data_with_password[:password_length].decode('utf-8')

        # Сверяем пароли
        if extracted_password != input_password:
            raise ValueError("Пароль неверный.")

        # Если пароль верен, возвращаем оставшиеся данные
        extracted_data = extracted_data_with_password[password_length:]
        self.logger.info("Data extracted successfully with correct password")
        return extracted_data





