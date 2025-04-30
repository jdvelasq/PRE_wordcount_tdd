import argparse

from ._internals.file_operations import create_output_folder
from ._internals.results import save_counting_results
from ._internals.word_count import count_words_in_folder


def parse_arguments():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Word count utility for processing text files."
    )
    parser.add_argument("input_folder", type=str, help="Path to the input folder")
    parser.add_argument("output_folder", type=str, help="Path to the output folder")
    return parser.parse_args()


def orchestrate_word_count(args):
    """Orchestrate the word count process."""

    input_folder = args.input_folder
    output_folder = args.output_folder

    # Count words in the input folder
    counter = count_words_in_folder(input_folder)

    # Create the output folder
    create_output_folder(output_folder)

    # Save the results
    save_counting_results(counter, output_folder)


def main():
    """Main function to parse arguments and orchestrate the word count process."""
    args = parse_arguments()
    orchestrate_word_count(args)


if __name__ == "__main__":
    main()
