
def decode_caesar(encrypted_text, shift=3):
    decoded = []
    
    for char in encrypted_text.upper():
        if char.isalpha():
            char_pos = ord(char) - ord('A')
            new_pos = (char_pos - shift) % (アルファベットの数)
            decoded.append(chr(ord('A') + new_pos))
        else:
            decoded.append(char)
    
    return ''.join(decoded)


def main():
    print("=== 暗号解読プログラム ===")
    
    user_input = input("暗号化されたテキストを入力してください: ").strip()
    
    if user_input:
        result = decode_caesar(user_input)
        print(f"\n入力:    {user_input}")
        print(f"出力:    {(出力したい内容)}")
    else:
        print("入力がありません。")


if __name__ == "__main__":
    main()
