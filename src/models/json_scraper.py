import json
import os
import glob


def parse_json_files_for_img_urls():
    for file in glob.glob(os.path.join("/Users/phillipoliveria/PycharmProjects/puppy_facts/src/JSON", '*.json')):
        filename = os.path.basename(file).strip('.json')
        with open(file) as f:
            data = json.load(f)
            with open("/Users/phillipoliveria/PycharmProjects/puppy_facts/src/insta_urls/{}.txt".format(filename),
                      "w") as i:
                for img in data:
                    for s in img['urls']:
                        i.write(str(s) + "\n")


