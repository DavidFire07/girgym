import json

with open("zadanie.txt", "r", encoding="utf-8") as file:
    notebook_json = json.load(file)

with open("zadanie.ipynb", "w", encoding="utf-8") as file:
    json.dump(notebook_json, file, indent=2)

print("Notebook created: zadanie.ipynb")