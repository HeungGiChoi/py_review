from random_word import RandomWords

rw = RandomWords()
word_list = rw.get_random_word(
    word_list=300,
    min_length=3
)

print(len(word_list))