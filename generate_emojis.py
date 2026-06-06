import os
import json

base_url = "https://raw.githubusercontent.com/haa-gg/DonutPlains/main/emojis/born_in_chaos/"
emojis_dir = "emojis/born_in_chaos"

emoji_list = []
for filename in os.listdir(emojis_dir):
    if filename.endswith(".png"):
        name = filename[:-4]  # Remove .png
        # Some items have '_item' in the texture name, let's strip it to match the standard name
        if name.endswith("_item"):
            name = name[:-5]
            
        emoji_list.append({
            "name": name,
            "url": base_url + filename
        })

with open("emojis.json", "w") as f:
    json.dump(emoji_list, f, indent=4)
print("emojis.json generated.")
