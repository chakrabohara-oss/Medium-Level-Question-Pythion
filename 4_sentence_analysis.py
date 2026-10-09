sentence = input("Enter random sentence: ")

'''Remove unnecessary spaces'''
cleaned_sentence = " ".join(sentence.split())
print(cleaned_sentence)

'''lowercase sentence'''
lower_sentence = cleaned_sentence.lower()
print(lower_sentence)

'''Word count'''
words = sentence.split()
total_words = len(words)
print(f"Total words in this sentence is {total_words}")

'''Word count'''
count = lower_sentence.count("python")
print(f"The word python appear {count} times in this sentence.")

'''Longest word'''
longest_word = max(words, key=len)
print(f"Longest word is {longest_word}")

