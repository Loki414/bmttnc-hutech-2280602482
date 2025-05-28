class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                # Lấy ký tự từ khóa, chuyển thành chữ hoa để tính toán độ dịch chuẩn
                key_char = key[key_index % len(key)].upper()
                key_shift = ord(key_char) - ord('A')

                if char.isupper():
                    encrypted_char_code = ord(char) - ord('A')
                    encrypted_text += chr((encrypted_char_code + key_shift) % 26 + ord('A'))
                else: # char.islower()
                    encrypted_char_code = ord(char) - ord('a')
                    encrypted_text += chr((encrypted_char_code + key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                # Lấy ký tự từ khóa, chuyển thành chữ hoa để tính toán độ dịch chuẩn
                key_char = key[key_index % len(key)].upper()
                key_shift = ord(key_char) - ord('A')

                if char.isupper():
                    decrypted_char_code = ord(char) - ord('A')
                    # Để đảm bảo kết quả modulo không âm khi trừ, có thể thêm 26 trước khi lấy modulo
                    decrypted_text += chr((decrypted_char_code - key_shift + 26) % 26 + ord('A'))
                else: # char.islower()
                    decrypted_char_code = ord(char) - ord('a')
                    # Để đảm bảo kết quả modulo không âm khi trừ, có thể thêm 26 trước khi lấy modulo
                    decrypted_text += chr((decrypted_char_code - key_shift + 26) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text