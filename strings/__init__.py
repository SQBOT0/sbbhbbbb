import os

import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir("./strings/langs/"):
    if "en" not in languages:
        with open("./strings/langs/en.yml", encoding="utf8") as f:
            languages["en"] = yaml.safe_load(f)
        languages_present["en"] = languages["en"]["name"]

    if filename.endswith(".yml"):
        language_name = filename[:-4]

        if language_name == "en":
            continue

        with open(f"./strings/langs/{filename}", encoding="utf8") as f:
            languages[language_name] = yaml.safe_load(f)

        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]

        try:
            languages_present[language_name] = languages[language_name]["name"]
        except Exception:
            import traceback

            traceback.print_exc()
            print("language_name =", language_name)
            print("languages keys =", list(languages.keys()))
            raise