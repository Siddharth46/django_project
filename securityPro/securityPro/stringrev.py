def reverse_words(sentence):
    list1 = sentence.split()
    print(list1)
    list2 = [x[::-1] for x in list1]
    print(' '.join(list2))

reverse_words("hello how are you")