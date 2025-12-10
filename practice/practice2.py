def count_frequencies(my_words):
    i = 0
    dict1 = {}
    for i in my_words:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    return dict1

def main():
    my_words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    print(count_frequencies(my_words))


if '__main__' == __name__:
    main()
