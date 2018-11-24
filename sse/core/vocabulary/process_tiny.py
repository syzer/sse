from ahocorasick import Automaton
from collections import defaultdict
import json
import pickle
from os import makedirs
from os import path
import zipfile

import numpy as np
import pandas as pd


DATA_PATH = path.join(path.dirname(__file__), "..", "..", "..", "data")


if __name__ == "__main__":
    makedirs(path.join(DATA_PATH, "processed", "vocabularies-tiny"), exist_ok=True)
    with zipfile.ZipFile(path.join(DATA_PATH, "raw", "vocabularies-tiny.zip"), "r") as zip_file:
        zip_file.extractall(path.join(DATA_PATH, "processed", "vocabularies-tiny"))

    # one concept name resolves to "NaN" for some reason. I decided to skip it.
    df = pd.read_csv(path.join(DATA_PATH, "processed", "vocabularies-tiny", "CONCEPT.csv"), sep="\t").dropna(subset=["concept_name"])

    concept_hashmap = defaultdict(list)

    # Assert we have the same amount of concept names and ids.
    assert len(df["concept_name"] == df["concept_id"])

    tiny_automaton = Automaton()

    for concept_name, concept_id in zip(df["concept_name"], df["concept_id"]):
        print(concept_name, concept_id)
        concept_hashmap[concept_name].append(str(concept_id))
        tiny_automaton.add_word(concept_name, (concept_id, concept_name))

    with open(path.join(DATA_PATH, "processed", "concept_map.json"), "w") as json_file:
        json.dump(concept_hashmap, json_file)

    tiny_automaton.make_automaton()

    with open(path.join(DATA_PATH, "processed", "tiny_vocabulary_automaton.pkl"), "wb") as automaton_file:
        pickle.dump(tiny_automaton, automaton_file)
