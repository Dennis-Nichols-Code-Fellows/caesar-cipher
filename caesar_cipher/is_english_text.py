import re
from caesar_cipher.corpus_loader import word_list, name_list


def is_english(text):

    candidate_words = text.split()
    word_count = 0

    for candidate in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', candidate)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass

    percentage = int(word_count / len(text.split()) * 100)
    verified = True if percentage > 70 else False

    return verified

