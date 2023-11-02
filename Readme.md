# GoWiki
This is a search engine built on the full English corpus of wikipedia (~75GB)


## Code Files

1. **myWikiIndexer.py** - File containing all functions related to XML parsing and text preprocessing, the code for indexing.
2. **k-way-merge.py** - File with functions related to k-way mergesort algorithm and creates secondary index.
3. **search.py** - Main file containing all the code for Query Processing

## Execution of Code

### Prerequisits

#### Required Directories

1. **index** - Initial index gets created here
2. **finalIndex** - They get merged here and also stored secondary index in this directory

#### Required Files

1. **stopwords.txt** - A txt file containing all the stop words in the current directory of the code
2. **wiki_dump.xml** - The XML file containing the full data of wikipedia

### Execution

1. Run **myWikiIndexer.py** with path to dump and folder to index as command line arguments.
2. Run **k-way-merge.py** - Will sort the index and create secondary index
3. Run **search.py** - An infinite loop runs expecting queries.

    