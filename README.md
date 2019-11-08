### yargy-based and deeppavlov-based NER for organization recognition in raw text

```sh
$ python -m venv env
$ source ./env/bin/activate
$ git clone https://github.com/alissiawells/ner
$ cd ner
$ pip install -r requirements.txt
$ pip install deeppavlov
$ python -m deeppavlov install ner_ontonotes_bert
```
edit input.txt

Usage:
```sh
$ python ner.py persons input.txt
```
or
```sh
$ python ner.py organizations input.txt
```

To test on default text:
```sh
$ python orgner.py test' 
```
TODO:
format BIO markup to tags 
