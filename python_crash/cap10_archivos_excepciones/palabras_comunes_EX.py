10.10

def count_common_words(filename):
    """Cuenta el número de palabras que se repiten en un archivo."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        # Fallos silenciosos con pass
        pass
    else:
        common_word = 'quiet'
        num_common_words = contents.count(common_word)
        print(f"The word '{common_word}' appears {num_common_words} times in the file.")

file = 'text_files/siddhartha.txt'
count_common_words(file)