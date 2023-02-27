# TRABAJAR CON MULTIPLES ARCHIVOS

def count_words(filename):
    """Cuenta el número aproximado de palabras de un archivo."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        # Fallos silenciosos con pass
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['text_files/alice.txt', 'text_files/moby_dick.txt', 'text_files/Little_women.txt', 'text_files/siddhartha.txt']
for filename in filenames:
    count_words(filename)
