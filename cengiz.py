import json
dosya = open ("cengiz.json", "r")
json_dosya = json.load(dosya)
siralanacak=json_dosya["kimlik"]
print(json.dumps(siralanacak,indent=2,sort_keys=True))
