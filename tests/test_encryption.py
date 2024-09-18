
from core import Encryption

def test_encryption():
    encryption = Encryption()
    password = "securepassword"
    data = "Привет, это тестовое сообщение!".encode('utf-8')

    # Шифрование данных
    encrypted_data = encryption.encrypt_data(data, password)

    # Дешифрование данных
    decrypted_data = encryption.decrypt_data(encrypted_data, password)

    assert data == decrypted_data, "Шифрование/дешифрование не работает корректно."
    print("Шифрование и дешифрование работают корректно.")


if __name__ == "__main__":
    test_encryption()
