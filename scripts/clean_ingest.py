import json
import re
from pathlib import Path

def load_transcripts():
    with open("outputs/transcripts.json", "r") as f:
        return json.load(f)

def split_section(transcript):
    section_header = [
        "CORPORATE PARTICIPANTS",
        "OTHER PARTICIPANTS",
        "MANAGEMENT DISCUSSION SECTION",
        "QUESTION AND ANSWER SECTION"
    ]
    sections = {}
    current_section = None
    current_content = []

    # header_count = 0  # Track how many headers we find

    for line in transcript["text"].split("\n"):
        line = line.strip()
        normalized_line = re.sub(r'\s+', ' ', line)
        
        if normalized_line in [h.strip().upper() for h in section_header]:
            if current_section:
                sections[current_section] = "".join(current_content)
            current_section = normalized_line
            current_content = []
        else:
            if current_section is not None:
                current_content.append(line)
                
    if current_section:
        sections[current_section] = "".join(current_content)
    return sections

if __name__ == "__main__":
    transcripts = load_transcripts()
    all_transcripts = {}
    
    for transcript in transcripts:
        quarter = transcript["quarter"]
        sections = split_section(transcript)
        all_transcripts[quarter] = sections
        
    print(all_transcripts["NVDA-Q3-2026"] ["QUESTION AND ANSWER SECTION"])
 
        


    # output_file = Path("outputs/transcripts2.json")
    # with output_file.open("w", encoding="utf-8") as f:
    #     json.dump(transcripts, f, indent=4)
        
    # # print(f"Saved transcripts to {output_file}")
    # print(repr(transcripts[0]["text"][0:100]))
    # # print(repr(transcripts[:200]))

    

    