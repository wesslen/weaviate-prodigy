import csv
import typer
import srsly

def create_json_for_unique_text(json_list):
    """
    Create a JSON object for each unique "text" value, nesting the "meta" tags for each key.

    Args:
        json_list (list): List of JSON objects.

    Returns:
        list: List of nested JSON objects.
    """
    unique_texts = {}  # Dictionary to store unique texts as keys and their meta tags as values

    # Iterate through the input list of JSON objects
    for json_obj in json_list:
        text = json_obj["text"]
        meta = json_obj["meta"]

        # If text already exists as a key in the unique_texts dictionary, update the meta tags
        if text in unique_texts:
            for key, value in meta.items():
                unique_texts[text]["meta"][key].append(value)
        # If text does not exist as a key in the unique_texts dictionary, create a new entry
        else:
            unique_texts[text] = {"text": text, "meta": {key: [value] for key, value in meta.items()}}

    # Convert dictionary values to list of JSON objects
    nested_json_list = list(unique_texts.values())

    return nested_json_list

def combine_text_columns(input_file: str, output_file: str):
    """
    Combine the 2nd and 3rd columns of a tab-separated input file into a new column named "text".

    Args:
        input_file (str): Input file name.
        output_file (str): Output file name.
    """
    # Read input file and write to output file
    with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
        # Create CSV reader and writer objects
        reader = csv.reader(file_in, delimiter="\t")
        writer = csv.writer(file_out, delimiter="\t")

        # Write header to output file
        header = next(reader)

        examples = []
        # Loop through each row in input file
        for row in reader:
            for text in row[1:2]:
                examples.append({
                    "text": text, 
                    "meta": {
                        "PAIR_ID": row[0], 
                        "score": row[3], 
                        "choice": row[4]
                            }
                    })

    unique_examples = create_json_for_unique_text(examples)

    print("Text columns combined successfully!")    
    srsly.write_jsonl(output_file, unique_examples)

def main(input_file: str, output_file: str):
    """
    Main function to run the script.

    Args:
        input_file (str): Input file name.
        output_file (str): Output file name.
    """
    combine_text_columns(input_file, output_file)
    

if __name__ == "__main__":
    typer.run(main)
