from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import logging


class Encryption:
    """
    Класс для шифрования и дешифрования данных с использованием AES.
    """

    def __init__(self, salt=None):
        self.salt = salt or os.urandom(16)
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def derive_key(self, password):
        """
        Генерация ключа на основе пароля с использованием PBKDF2.

        :param password: str, пароль
        :return: bytes, сгенерированный ключ
        """
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        self.logger.info("Key derived successfully")
        return key

    def encrypt_data(self, data, password):
        """
        Шифрование данных с использованием AES.

        :param data: bytes, данные для шифрования
        :param password: str, пароль для генерации ключа
        :return: bytes, зашифрованные данные
        """
        key = self.derive_key(password)
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
        self.logger.info("Data encrypted successfully")
        return iv + encrypted_data

    def decrypt_data(self, encrypted_data, password):
        """
        Дешифрование данных с использованием AES.

        :param encrypted_data: bytes, зашифрованные данные
        :param password: str, пароль для генерации ключа
        :return: bytes, расшифрованные данные
        """
        key = self.derive_key(password)
        iv = encrypted_data[:16]
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        self.logger.info("Data decrypted successfully")
        return decrypted_data
