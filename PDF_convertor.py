import pypdfium2 as pdfium
import pathlib
import argparse

def PDF_convert(PDF_path, dst_path):
    pathlib.Path(dst_path).mkdir(exist_ok=True)
    pdf_files = [f for f in pathlib.Path(PDF_path).rglob('*')]
    # Load a document
    for pdf_file in pdf_files:
        pdf = pdfium.PdfDocument(pdf_file)
    
        for i in range(len(pdf)):
            page = pdf[i]
            image = page.render(scale=3).to_pil()
            image.save(f"{dst_path}/{pdf_file.stem}_{i:04d}.jpg")

    return


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--PDF_path", required=True, help="PDF file path")
    parser.add_argument("--dst_path", required=True, help='directory where covnerted PDF image will saved')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    PDF_convert(args.PDF_path, args.dst_path)