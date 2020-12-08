# Multi Replacer
Search and Replace all the files underneath a given directory tree with a given mapping table.

The table items must be separated with
> [..] runs of consecutive whitespace [..]                                                                    

as we use here the default of python's [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split)-method.

In the test folder you can find a [sample](test/mapping.txt) of a mapping table:
```
# Taken from https://documentation.coremedia.com/cmcc-10/artifacts/2010/webhelp/deployment-en/content/contentServerRenamedProperties.html
sql.store.sgmlcache.size 	sql.store.sgml-cache-size-bytes
sql.store.sgmlcache.sizeBytes 	sql.store.sgml-cache-size-bytes
```
As you can see, also comments are possible starting with a hash ('#').

Feel free to adapt this to your needs. The relevant line of code is currently [here](multi-replacer.py#L38). 

## Usage
```
./multi-replacer.py FILE_EXTENSION FOLDER MAPPING_FILE
```                                                   

## Test
You can use (or play around) with the given infrastructure in the `test`-folder.

```
./multi-replacer.py properties test test/mapping.txt
```                                                   
