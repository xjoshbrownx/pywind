import os
from html_processor import HTMLProcessor

if __name__ == "__main__":
    input_dir = "input_html_files"
    output_dir = "output_html_files"
    os.makedirs(output_dir, exist_ok=True)

    processor = HTMLProcessor()

    for filename in os.listdir(input_dir):
        if filename.endswith(".html"):
            input_file_path = os.path.join(input_dir, filename)
            output_file_path = os.path.join(output_dir, filename)
            processor.process_html(input_file_path, output_file_path)
