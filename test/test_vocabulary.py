from os import path
from ahocorasick import Automaton
import pandas as pd

from sse.core.vocabulary.add_vocabulary import add_concepts, prepare_data
from sse.core.vocabulary.match_text import generate_matches


dummy_abstract = "In previous studies, it was revealed that ethyl acetate (EtOAc) extracts from Sophora flavescens Ait. improved glucose tolerance, reduced hyperglycemia, and restored insulin levels to treat diabetes. The aim of this study was to develop an accurate and sensitive UHPLC-MS method for simultaneous determination of flavonoids in EtOAc extracts of Kushen in rat plasma. Ethyl acetate-acetonitrile (2:1) was selected as the solvent to extract the four flavonoids from rat plasma. A BEH C18 column (2.1 mm×100 mm, 1.7 μm) with a C18 guard cartridge was chosen as the separation plant using a gradient elution with acetonitrile (solvent A) and 0.1% formic acid (solvent B) in water. For all four analytes, the method showed good linearity (r2 > 0.991) in 1-500 ng/mL. The inter- and intra-day accuracy ranged from -13.78-7.19%, and the precision (RSD) was less than 8.75%. Recoveries of all four flavonoids ranged from 85.9 to 101.3%. According to the results of multi-target pharmacokinetic studies, we find that four active flavonoids in EtOAc extracts from Kushen have similar absorption kinetics but have very different metabolic kinetics and double peak phenomenon was observed in the concentration-time curve of norkurarinone which is different from previous study. In conclusion, the detection and multi-target pharmacokinetic studies of active flavonoids after oral administration of EtOAc extracts from Kushen by an efficient, sensitive and selective UHPLC-MS method were established successfully, and the results may provide a foundation for future studies of Kushen."


def test_add_concepts():
    data_path = prepare_data(
        path.join(
            path.dirname(__file__),
            "..", "data", "raw", "vocabularies-tiny.zip"
        )
    )

    dataframe = pd.read_csv(path.join(data_path, "CONCEPT.csv"), sep="\t").dropna(
        subset=["concept_name"]
    )
    automaton = Automaton()
    automaton = add_concepts(automaton, zip(dataframe["concept_name"], dataframe["concept_id"]))

    automaton.make_automaton()

    assert len(tuple(automaton.keys())) == 15791

    first_keys = sorted(automaton.keys())[:10]
    assert first_keys == ['% REF', '(1-6)-alpha-glucomannan', '1 alpha-hydroxyergocalciferol', "1,1',1'',1'''-(ethylenedinitrilo)tetra-2-propanol", '1,1,1-trichloro-2,2,2-trifluoroethane', '1,1-difluoroethane', '1,10-decanediol', '1,10-phenanthroline', '1,2,6-hexanetriol', '1,2-Dipalmitoylphosphatidylcholine']

    first_concept_id, first_concept_name = automaton.get(first_keys[0])

    assert (first_concept_id, first_concept_name) == (8514, '% REF')


def test_match_text():
    data_path = prepare_data(
        path.join(
            path.dirname(__file__),
            "..", "data", "raw", "vocabularies-tiny.zip"
        )
    )

    dataframe = pd.read_csv(path.join(data_path, "CONCEPT.csv"), sep="\t").dropna(
        subset=["concept_name"]
    )
    automaton = Automaton()
    automaton = add_concepts(automaton, zip(dataframe["concept_name"], dataframe["concept_id"]))

    automaton.make_automaton()

    matches = list(generate_matches(automaton=automaton, text=dummy_abstract))
    match_soll_values = [(54, (46257025, 'ethyl acetate')), (653, (45616149, 'formic acid')), (785, (8512, 'day'))]
    assert matches == match_soll_values
