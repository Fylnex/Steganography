import logging


class Extractor:
    """
    Класс для извлечения данных из изображения методом LSB.
    """

    def __init__(self):
        # Инициализация логгера
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def extract_data(self, image):
        """
        Извлекает данные из изображения без шифрования.

        :param image: Image object, изображение для извлечения данных
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
        extracted_data = int(data_bits, 2).to_bytes(data_len, byteorder='big')

        self.logger.info("Data extracted successfully")
        return extracted_data




