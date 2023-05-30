word_user = input('type your word ')

dictionary = {"lazy": "lazy definition", "word": "word definition", "sentence": "sentence definition"}

check_dictionary = {v: k for v, k in dictionary.items() if v == word_user}
if check_dictionary:
    print(check_dictionary)
else:
    print("unknown word")
