def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char_code = ord(char) + shift_amount
                if shifted_char_code > ord('z'):
                    shifted_char_code = ord('a') + (shifted_char_code - ord('z') - 1)
            elif char.isupper():
                shifted_char_code = ord(char) + shift_amount
                if shifted_char_code > ord('Z'):
                    shifted_char_code = ord('A') + (shifted_char_code - ord('Z') - 1)
            encrypted_text += chr(shifted_char_code)
        else:
            encrypted_text += char  
    return encrypted_text


def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)

import nltk
from nltk.corpus import words
nltk.download('words')
english_words = set(words.words())

def crack(encrypted_text):
    for shift in range(26):
        decrypted_attempt = decrypt(encrypted_text, shift)
        words_in_attempt = decrypted_attempt.split()
        english_word_count = sum(word.lower() in english_words for word in words_in_attempt)

        if english_word_count >= len(words_in_attempt) / 2:
            return decrypted_attempt
    return ""
