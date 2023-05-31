word_user = input('Type your word : ')

dictionary = {"lazy": "lazy definition", "word": "word definition", "sentence": "sentence definition"}

# check_dictionary = {w: k for w, k in dictionary.items() if w == word_user}
# if check_dictionary:
#     print(check_dictionary)
# else:
#     print("unknown word")

if dictionary.get(word_user) != None:
    print(dictionary.get(word_user))
else:
    print("Unknown word")