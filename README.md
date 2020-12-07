# Multi Replacer
Search and Replace all the files underneath a given directory tree with a given mapping table.

The table items must be separated with
> [..] runs of consecutive whitespace [..]                                                                    

as we use here the default of pythons [`str.split`](https://docs.python.org/3/library/stdtypes.html#str.split).

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
