import os


def count_words_in_folder(input_folder):
    """Count words in all files within the input folder."""
    counter = {}
    files_in_input_dir = os.listdir(input_folder)
    for filename in files_in_input_dir:
        with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
            for line in f:
                for word in line.split():
                    word = word.lower().strip(",.!?")
                    counter[word] = counter.get(word, 0) + 1
    return counter
