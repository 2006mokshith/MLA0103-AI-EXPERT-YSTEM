sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
count = 0

for ch in sentence:
    if ch in vowels:
        print(ch)
        count += 1

print("Total vowels:", count)
