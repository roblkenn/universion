import json

with open("setup.py", "r") as f:
    toSearch = f.read()

tag = "version=\""
start = toSearch.find(tag) + len(tag)
end = toSearch.find("\"", start)

versionDict = {
    "version": toSearch[start:end]
}

with open("version.json", "w") as f:
    json.dump(versionDict, f)