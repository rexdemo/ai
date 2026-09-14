
def sort_sentence(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    return ' '.join(sorted_words)


if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    result = sort_sentence(input_sentence)
    print("Sorted sentence:", result)

