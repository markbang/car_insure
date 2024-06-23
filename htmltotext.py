import os
import html2text as ht

def convert_html_to_text(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".html"):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")

            # Read the HTML file
            with open(input_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()

            # Convert HTML to text and don't remove image and link
            
            text_maker = ht.HTML2Text()
            text_maker.ignore_images = False
            text_maker.ignore_links = False
            text_content = text_maker.handle(html_content)
            

            # Write the text to the output file
            with open(output_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text_content)

            print(f"Converted {filename} to text.")

if __name__ == "__main__":
    input_dir = 'notebooks'
    output_dir = 'text_output'
    convert_html_to_text(input_dir, output_dir)
