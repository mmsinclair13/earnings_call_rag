# Goal of ingest.py is to take the pdf from nvidia and make it 1) open
# 2) extract the text
# 3 print the infmration necessary: for now just the number of pages, 
#             file name, first few characters and the totla number of characters extracted

from pypdf import PdfReader
from pathlib import Path
import json

pdf_folder = Path("data/nvidia")
pdf_files = list(pdf_folder.glob("*.pdf"))

print(f"Found {len(pdf_files)} PDF files my guy")

transcripts = []

for pdf_file in pdf_files:
    print(f"\nLoading {pdf_file.name}")
    reader = PdfReader(pdf_file)
    print(f"Pages: {len(reader.pages)}")

    quarter = pdf_file.stem
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text 
    
    
    transcript = {
        "company": "nvidia",
        "quarter": quarter,
        "text": text,
        }
    transcripts.append(transcript)


    output_file = Path("outputs/transcripts.json")
    with output_file.open("w", encoding="utf-8") as f:
        json.dump(transcripts, f, indent=4)
        
    print(f"Saved transcripts to {output_file}")
print(f"Total transcripts: {len(transcripts)} transferred successfully")
