word: str = input("Give word: ")
if len(set(word)) == len(word):
    print("None")
else:
    print("Duplicate")
