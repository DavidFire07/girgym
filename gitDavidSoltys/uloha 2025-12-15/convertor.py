import json

try:
    with open("pandas_numpy.txt", "r", encoding="utf-8") as file:
        notebook_json = json.load(file)

    with open("pandas_nympy.ipynb", "w", encoding="utf-8") as file:
        json.dump(notebook_json, file, indent=2)

    print("Conversion succeeded")

except:
    print("Conversion failed")