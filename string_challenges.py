# Вывести последнюю букву в слове
print("-------- Задание 1. --------")
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
print("-------- Задание 2. --------")
word = 'Архангельск'
print(word.lower().count("а"))


# Вывести количество гласных букв в слове
print("-------- Задание 3. --------")
word = 'Архангельск'
vowels, count = ["ё", "у", "е", "ы", "а", "о", "э", "я", "и", "ю"], 0
for letter in word.lower():
    if letter in vowels:
        count += 1
print(count)

# Вывести количество слов в предложении
print("-------- Задание 4. --------")
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
print("-------- Задание 5. --------")
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
print("-------- Задание 6. --------")
sentence = 'Мы приехали в гости'
mid = 0.0
for word in sentence.split():
    mid += len(word)
print(mid/len(sentence.split()))
