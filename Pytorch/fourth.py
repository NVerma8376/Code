import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a PDF file.
    Args:
        pdf_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def save_text_to_file(text, output_path):
    """
    Save the extracted text to a text file.
    Args:
        text (str): The text to save.
        output_path (str): Path to the output text file.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)

def process_pdfs_in_directory(input_dir, output_dir):
    """
    Process all PDFs in a directory, extracting text and saving it to text files.
    Args:
        input_dir (str): Directory containing PDF files.
        output_dir (str): Directory where extracted text files will be saved.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):  # Process only PDF files
            pdf_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
            
            print(f"Processing: {filename}")
            try:
                text = extract_text_from_pdf(pdf_path)
                save_text_to_file(text, output_path)
                print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    # Set the input and output directories
    input_directory = "pdfs"  # Directory containing PDF files
    output_directory = "extracted_text"  # Directory to save text files

    # Run the processing function
    process_pdfs_in_directory(input_directory, output_directory)
