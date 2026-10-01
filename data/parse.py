import re

with open("data/pattern.txt", encoding="utf-8") as f:
    text = f.read()

rnd = re.compile(r"^((?:Rnds?|Rows?)\.?\s*\d+(?:-\d+)?): (.*?)(?: \((\d+)\))?$", re.MULTILINE | re.IGNORECASE)

for m in rnd.finditer(text):
    round_label, instructions, count = m.groups()
    print(round_label, instructions, count)
