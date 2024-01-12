import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_files, output_file):
    try:
        merger = PdfMerger()
        for file in input_files:
            merger.append(file)
        
        output_file = f"{os.path.splitext(output_file)[0]}.pdf"
        merger.write(output_file)
        merger.close()
        print(f"PDFs merged and saved as {output_file}")
    except Exception as e:
        print(f"Merge failed: {e}")

def main():
    print("PDF Merger App")
    num_files = int(input("How many PDF files do you want to merge? "))

    files_to_merge = []
    for i in range(num_files):
        file_name = input(f"Enter the path of PDF file {i + 1}: ")
        files_to_merge.append(file_name)

    output_file_name = input("Enter the name of the output merged file: ")

    merge_pdfs(files_to_merge, output_file_name)

if __name__ == "__main__":
    main()