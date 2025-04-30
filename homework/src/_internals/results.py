import os


def save_counting_results(counter, output_folder):
    """Save word count results to a file in the output folder."""
    output_file = os.path.join(output_folder, "results.tsv")
    with open(output_file, "w", encoding="utf-8") as f:
        for key, value in counter.items():
            f.write(f"{key}\t{value}\n")
