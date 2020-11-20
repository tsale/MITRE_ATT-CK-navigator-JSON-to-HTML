from attackcti import attack_client
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="-Specify the full path of the json file", required=False)
args = parser.parse_args()
file = args.file

lift = attack_client()
file = "file.json"

all_techniques = lift.get_techniques()
lst = []
subs = []
result_lst = list()

with open(file, "r+") as jsonfile:
    file = json.load(jsonfile)
    for i in file["techniques"]:
        if i["showSubtechniques"] is True:
            continue
        else:
            lst.append(i["techniqueID"])
    lst = list(dict.fromkeys(lst))

def get_techniques_info_by_ID(ID):
    for name in all_techniques:
        if ID.lower() in name['external_references'][0]['external_id'].lower():
            result_lst.append(
                f"""<a href="{name['external_references'][0]['url']}">[MITRE ATT&amp;CK] {name["name"]} - {ID}</a> """)


for x in lst:
    get_techniques_info_by_ID(x)

print("\n" + f"<p><strong>MITRE ATT&amp;CK:</strong> {' | '.join(result_lst)}")