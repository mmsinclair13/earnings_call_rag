import json

def load_transcript():
    with open(r"C:\Word Documents\swe project\earnings_all_rag\outputs\transcripts.json", 'r', encoding='utf-8') as f:
        print(f"Loaded transcripts from C:\Word Documents\swe project\earnings_all_rag\outputs\transcripts.json")
        return json.load(f)
    
load_transcript()



