import logging

import logging


class Embedder:
    """
    Класс для встраивания данных в изображение методом LSB (наименее значимого бита).
    """

    def __init__(self):
        # Инициализация логгера
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def embed_data(self, image, data):
        """
        Встраивает данные в изображение без шифрования с использованием метода LSB.

        :param image: Image object, изображение для встраивания
        :param data: bytes, данные для встраивания
        :return: Image object, модифицированное изображение
        """
        data_len = len(data)

        # Преобразуем длину данных в 64-битное число
        len_bin = format(data_len, '064b')
        data_bin = ''.join(format(byte, '08b') for byte in data)
        full_bin = len_bin + data_bin

        pixels = list(image.getdata())
        new_pixels = []
        data_index = 0

        max_bits = len(pixels) * 3
        if len(full_bin) > max_bits:
            raise ValueError("Данные слишком большие для выбранного изображения.")

        for pixel in pixels:
            r, g, b = pixel[:3]
            if data_index < len(full_bin):
                r = (r & ~1) | int(full_bin[data_index])
                data_index += 1
            if data_index < len(full_bin):
                g = (g & ~1) | int(full_bin[data_index])
                data_index += 1
            if data_index < len(full_bin):
                b = (b & ~1) | int(full_bin[data_index])
                data_index += 1
            new_pixel = (r, g, b)
            if len(pixel) == 4:  # Если есть альфа-канал
                new_pixel += (pixel[3],)
            new_pixels.append(new_pixel)
            if data_index >= len(full_bin):
                new_pixels.extend(pixels[len(new_pixels):])
                break
        image.putdata(new_pixels)
        self.logger.info("Data embedded successfully")
        return image




