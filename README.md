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

```sh
$ python orgner.py input.txt output.txt
```
or
```sh
$ python orgner.py test' to test on default text
```
TODO:
format BIO markup to tags 
# NERon
