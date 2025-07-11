import json
from datetime import datetime

def convert_iso_to_millis(iso_string):
    dt = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

def merge_data(data1, data2):
    merged = []
    for i in data1:
        merged.append({
            "timestamp": convert_iso_to_millis(i["timestamp"]),
            "device": i["device"],
            "temperature": i["temperature"]
        })
    for i in data2:
        merged.append({
            "timestamp": i["timestamp"],
            "device": i["device"],
            "temperature": i["temperature"]
        })
    return sorted(merged, key=lambda x: x["timestamp"])

if __name__ == "__main__":
    with open("data-1.json") as f1, open("data-2.json") as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)

    out = merge_data(d1, d2)
    with open("output.json", "w") as f_out:
        json.dump(out, f_out, indent=2)

