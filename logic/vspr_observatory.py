#!/usr/bin/env python3
import json
import arxiv
from huggingface_hub import HfApi

# [CONFIGURATION]
OUTPUT_PATH = "/tmp/observatory_state.json"
SCIENCE_QUERY = 'ti:"Condensed Matter" AND abs:"Topology"'
MODEL_ID = "Laminar-Mirror/Vesper-01"

def get_science_title():
    try:
        client = arxiv.Client(num_retries=1, page_size=1)
        search = arxiv.Search(query=SCIENCE_QUERY, max_results=1)
        results = list(client.results(search))
        return results[0].title if results else "VOID"
    except: return "FETCH_ERROR"

def get_weights_sha():
    try:
        api = HfApi()
        info = api.model_info(MODEL_ID)
        return info.sha
    except: return "SYNC_FAILED"

if __name__ == "__main__":
    state = {"science_title": get_science_title(), "weights_sha": get_weights_sha()}
    with open(OUTPUT_PATH, "w") as f:
        json.dump(state, f)
    print(f"[|||] OBSERVATORY DATA DUMPED TO {OUTPUT_PATH}")
