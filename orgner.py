#!/usr/bin/env python3
from __future__ import unicode_literals

import re
import os
import sys

from natasha import OrganisationExtractor
from natasha.grammars.organisation import Organisation

from deeppavlov import configs, build_model

from typing import List, Any

def orgNatasha(text, show=True):
    """
    based on yargy
    input: text - string
    output: list of strings (organizations)
    """
    extractor = OrganisationExtractor()
    matches = extractor(text)
    organizations = []  # type: List[Strings]
    for match in matches:
        start, stop = match.span
        organizations.append(text[start:stop])
    if show:
        print('Natasha:')
        print(organizations)
    return organizations

def orgDeeppavlov(text, show=True):
    """
    based on BERT
    input: text - string
    output: list of strings (organizations)
    """
    #ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=False)
    ner_model = build_model(configs.ner.ner_ontonotes_bert_mult, download=True)
    organizations = []
    matches = ner_model([text])[0][0]
    tags = ner_model([text])[1][0]
    indices = [i for i, x in enumerate(tags) if "ORG" in x]
    for i in indices:
        organizations.append(matches[i])
    if show:
        print('Deppavlov')
        print(organizations)
    return organizations


if __name__ == "__main__":
    """
    deeppavlov/requirements/bert_dp.txt
    python -m deeppavlov install ner_ontonotes_bert
    """

    if (len(sys.argv) == 3):
        input = os.path.abspath(sys.argv[1])
        output = os.path.abspath(sys.argv[2])

        with open(input, 'r') as f:
            text = f.read()

        with open(output, 'w') as f:
            if len(text) < 500:

                f.write('Deeppavlov\n')
                organizations1 = orgDeeppavlov(text, show=False)
                for x in organizations1:
                    f.write(x+'\n')

                f.write('Natasha\n')
                organizations2 = orgNatasha(text, show=False)
                for x in organizations2:
                    f.write(x+'\n')

            else:
                texts = text.split('.')
                output = []
                for string in range(len(texts)):
                    organizations1 = orgDeeppavlov(string, show=False)
                    organizations2 = orgNatasha(string, show=False)
                    output.append('Deeppavlov')
                    output.append(organizations1)
                    output.append('Natasha')
                    output.append(organizations2)
                    output.append(string)
                for x in output:
                    f.write(x+'\n')

        print('Done')

    elif (len(sys.argv) == 2):
        testText = '''

            Дочернее подразделение госкомпании «Газпром» — «Газпром добыча Иркутск» — провело тендер на поставку питьевой воды из Байкала.
            Расходы на поставку воды из озера составят 336 713 рублей. Ожидаемая дата поставки воды «дочке» «Газпрома» — 31 декабря 2018 года.
            Исполнителем контракта стало ООО «Аква Плюс». Воду будут поставлять в таре трех типов: в возвратных бутылях объемом 18,9 литра,
            а также в бутылках объемом 5 литров и 0,5 литра.
            '''

        organizations1 = orgDeeppavlov(testText, show=True)
        organizations2 = orgNatasha(testText, show=True)
        print(testText)

    else:
        print("Usage: 'python orgner.py input.txt output.txt' or 'python orgner.py test' to test on default text")
