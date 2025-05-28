class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1  # 1: down, -1: up
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Xác định độ dài của mỗi "thanh ray" (rail)
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1  # 1: đi xuống, -1: đi lên

        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        # Xây dựng lại các "thanh ray" từ bản mã
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length])) # Chuyển chuỗi con thành list các ký tự
            start += length

        # Đọc lại văn bản gốc từ các "thanh ray"
        plain_text = ""
        rail_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rail_index].pop(0) # Lấy và xóa ký tự đầu tiên của rail hiện tại
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction

        return plain_text        