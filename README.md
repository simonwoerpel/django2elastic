# django2elastic
simple script to load djangó's dumpdata json into an elasticsearch index

this simple script loads json objects
(created from django's dumpdata)
into an elasticsearch index.
it only uses the ['fields'] part of the objects and 
uses ['model'] as the elastic doc type and creates 
a unique id from uuid.uuid4()

example use:
```
django2elastic.py data.json index doctype
```

