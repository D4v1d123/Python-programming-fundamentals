# STRING DIVISION
word = "Mexico"

word_slice = word [1 : 5]
print("Mexico [1 : 5] => " + word_slice)

word_slice = word [-1]
print("Mexico [-1] => " + word_slice)

word_slice = word [: -1]
print("Mexico [: -1] => " + word_slice)

word_slice = word [:: -1]
print("Mexico [:: -1] => " + word_slice)

word_slice = word [0 : 6 : 2]
print("Mexico [0 : 6 : 2] => " + word_slice + "\n")