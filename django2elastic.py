# coding: utf-8
"""
this simple script loads json objects
(created from django's dumpdata)
into an elasticsearch index.
it only uses the ['fields'] part of the objects and 
uses ['model'] as the elastic doc type and creates 
a unique id from uuid.uuid4()

example use:
    django2elastic.py data.json index doctype
"""

from elasticsearch import Elasticsearch

import argparse
import uuid
import simplejson as json


def ask_to_continue(prompt):
    while True:
        if not str(input(prompt+'\npress [y] to continue or ctrl-c to abort\n')) == 'y':
            continue
        else:
            break
    return True


parser = argparse.ArgumentParser()
parser.add_argument('inputfile', type=str, help='the input file, must be .json created from django dumpdata command')
parser.add_argument('index', type=str, help='the elastic index')
args = parser.parse_args()
input_fp = args.inputfile
index = args.index


print('connecting to elastic index %s...' % index)

es = Elasticsearch()
try:
    print(es.info())
except Exception as e:
    print(e)
    raise

print('...OK')

print('loading data from %s...' % input_fp)

DATA = json.load(open(input_fp))

print('found %s objects' % str(len(DATA)))
print('this would be a sample document:\n')
print(DATA[0]['fields'])


ask_to_continue('looks good?')

i = 0
for d in DATA:
    doc = d['fields']
    es.index(index=index, doc_type=d['model'], id=uuid.uuid4(), body=doc)
    i += 1
    print('imported: %s of %s' % (str(i), str(len(DATA))))


print('END: converted %s records into elasticsearch' % str(i))

