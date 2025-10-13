def caesar_encrypt(text, key):
    shift = key % 26
    res = []
    for ch in text:
        if 'a' <= ch <= 'z':
            res.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        elif 'A' <= ch <= 'Z':
            res.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        else:
            res.append(ch)
    return "".join(res)

plain = "purnomo yusgiantoro"
key = 230202774
cipher = caesar_encrypt(plain, key)
print("Plain :", plain)
print("Key   :", key,)
print("Cipher:", cipher)

