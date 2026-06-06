import json

with open("emojis.json", "r") as f:
    data = json.load(f)

base_url = "https://raw.githubusercontent.com/haa-gg/DonutPlains/main/emojis/born_in_chaos/"

# Add aliases for badly named textures
data.append({"name": "seed_of_chaos", "url": base_url + "chaossemt.png"})
data.append({"name": "bone_handle", "url": base_url + "bonruk.png"})

with open("emojis.json", "w") as f:
    json.dump(data, f, indent=4)
