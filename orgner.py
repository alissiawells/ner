#!/usr/bin/env python3
from __future__ import unicode_literals

import re
import os
import sys

from deeppavlov import configs, build_model

from typing import List, Any

def buldmodel():
    ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)
    # ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=False)
    return ner_model

def organizations(ner_model, text, show=True):
    """
    based on BERT
    input: text - string
    output: list of strings (organizations)
    """
    orgs = []
    matches = ner_model([text])[0][0]
    tags = ner_model([text])[1][0]
    indices = [i for i, x in enumerate(tags) if "ORG" in x]

    for i in indices:
        orgs.append(matches[i])
        
    if show:
        print('organizations:')
        print(orgs)
    return orgs

def persons(ner_model, text, show=True):
    """
    based on BERT
    input: text - string
    output: list of strings (persons)
    """
    pers = []
    matches = ner_model([text])[0][0]
    tags = ner_model([text])[1][0]
    indices = [i for i, x in enumerate(tags) if "PERSON" in x]
    for i in indices:
        pers.append(matches[i])
    if show:
        print('persons:')
        print(pers)
    return pers


if __name__ == "__main__":
    """
    deeppavlov/requirements/bert_dp.txt
    python -m deeppavlov install ner_ontonotes_bert
    """

    ner_model = buldmodel()
    
    # with files
    if (len(sys.argv) == 3) and (sys.argv[1]=='persons'):
        input = os.path.abspath(sys.argv[2])
        output = 'output.txt'
        with open(input, 'r') as f:
            text = f.read()
        with open(output, 'w') as f:
            pers = persons(ner_model, text, show=False)
            for x in pers:
                f.write(x+'\n')
                    
    elif (len(sys.argv) == 3) and (sys.argv[1]=='organizations'):
        input = os.path.abspath(sys.argv[2])
        output = 'output.txt'
        with open(input, 'r') as f:
            text = f.read()
        with open(output, 'w') as f:
            orgs = organizations(ner_model, text, show=False)
            for x in orgs:
                f.write(x+'\n')

    #test
    elif (len(sys.argv)==2) and (sys.argv[1]=='persons'):
        testText = '''

            Дочернее подразделение госкомпании «Газпром» — «Газпром добыча Иркутск» — провело тендер на поставку питьевой воды из Байкала.
            Расходы на поставку воды из озера составят 336 713 рублей. Ожидаемая дата поставки воды «дочке» «Газпрома» — 31 декабря 2018 года.
            Исполнителем контракта стало ООО «Аква Плюс». Воду будут поставлять в таре трех типов: в возвратных бутылях объемом 18,9 литра,
            а также в бутылках объемом 5 литров и 0,5 литра.
            '''

        persons(ner_model, testText)
        print(testText)
        
    elif (len(sys.argv) == 2) and (sys.argv[1]=='organizations'):
        testText = '''

            Дочернее подразделение госкомпании «Газпром» — «Газпром добыча Иркутск» — провело тендер на поставку питьевой воды из Байкала.
            Расходы на поставку воды из озера составят 336 713 рублей. Ожидаемая дата поставки воды «дочке» «Газпрома» — 31 декабря 2018 года.
            Исполнителем контракта стало ООО «Аква Плюс». Воду будут поставлять в таре трех типов: в возвратных бутылях объемом 18,9 литра,
            а также в бутылках объемом 5 литров и 0,5 литра.
            '''

        organizations(ner_model, testText)
        print(testText)

    else:
        print("Usage as a script: 'python ner.py persons input.txt'\n \
        or 'python ner.py persons' to test on default text.\n \
        Replace persons on organizations to find companies.\n \
        Usage as a module:\n \
        import ner\n \
        ner_model = ner.buldmodel()\n \
        YL = ner.organizations(ner_model, text, print=False)\n \
        FL = ner.persons(ner_model, text, print=False) \
        In case you want to print the result, call the functions without th parameter show:\n \
        ner.persons(ner_model, text)")
