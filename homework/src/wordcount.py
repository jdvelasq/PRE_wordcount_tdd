import os
import sys


def count_words(words):
    """Count occurrences of each word using a plain dictionary."""
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def preprocess_lines(lines):
    """Preprocess lines by normalizing and cleaning text."""
    return [line.lower().strip() for line in lines]


def read_all_lines(input_folder):
    """Read all lines from all files in the input folder."""
    lines = []
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            lines.extend(f.readlines())
    return lines


def split_into_words(lines):
    """Split lines into individual words and clean punctuation."""
    words = []
    for line in lines:
        words.extend(word.strip(",.!?") for word in line.split())
    return words


def write_word_counts(output_folder, word_counts):
    """Write word counts to a file in the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    output_file = os.path.join(output_folder, "wordcount.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in word_counts.items():
            f.write(f"{word}\t{count}\n")


def main():
    """Main function to orchestrate the word count process."""

    if len(sys.argv) != 3:
        print("Usage: python3 -m homework <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    words = split_into_words(preprocessed_lines)
    word_counts = count_words(words)
    write_word_counts(output_folder, word_counts)


if __name__ == "__main__":
    main()
