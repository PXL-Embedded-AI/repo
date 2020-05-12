import json, time
    
print('JSON file contents:')

with open('D:\spectrumHistogram.json', 'r') as f_json:
    parsed = json.load(f_json)
    print(json.dumps(parsed, indent=4, sort_keys=False))
