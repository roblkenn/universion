import json

with open("VERSION", "r") as f:
    version = f.read().strip()

versionDict = {
    "version": version
}

with open("version.json", "w") as f:
    json.dump(versionDict, f)