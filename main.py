from attackcti import attack_client
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    "--file",
    help="-Specify the full path of the json file",
    required=False)
args = parser.parse_args()



def get_techniques():
    file = args.file
    techniques = []
    with open(file, "r+") as jsonfile:
        file = json.load(jsonfile)
        for i in file["techniques"]:
            if i["showSubtechniques"] is True:
                continue
            else:
                techniques.append(i["techniqueID"])
        techniques = list(dict.fromkeys(techniques))
        return techniques


def get_techniques_info_by_ID(ID):
    for name in all_techniques:
        if ID.lower() in name['external_references'][0]['external_id'].lower():
            fin_lst.append(
                f"""<strong>{name["kill_chain_phases"][0]["phase_name"]}: </strong><a href="{name['external_references'][0]['url']}">[MITRE ATT&amp;CK] {name["name"]} - {ID}</a><br> """
            )


if __name__ == "__main__":
    fin_lst = []
    techniques = get_techniques()
    lift = attack_client()
    all_techniques = lift.get_techniques()

    for x in techniques:
        get_techniques_info_by_ID(x)

    print("\n" +
          f"<H2>MITRE ATT&amp;CK:</H2> {' '.join(fin_lst)}")
