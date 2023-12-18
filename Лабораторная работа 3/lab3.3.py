def count_letters(text):
    letter_count = {}

    for char in text:
        if char.isalpha():
            char_lower = char.lower()
            letter_count[char_lower] = letter_count.get(char_lower, 0) + 1

    return letter_count

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    letter_frequency = {}

    for letter, count in letter_count.items():
        frequency = count / total_letters
        letter_frequency[letter] = round(frequency, 2)

    return letter_frequency

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
letters_count_result = count_letters(text)
letters_frequency_result = calculate_frequency(letters_count_result)

for letter, frequency in letters_frequency_result.items():
    print(f"{letter}: {frequency}")
