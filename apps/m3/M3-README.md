# Milestone-3
## Technical Brief 

## Milestone 2 vs Milestone 3
## With the API added in milestone 2, it was quite limited. The user searches for a tag in the text and replaces it with a new tag. However, this doesn't allow the user to change attributes, use any sort of conditional logic or perform any sort of side effects. With an updated API we can allow the user to have more flexibility in how they want to go about changing tags, changing attributes or really doing anything they want with this new API, their own functions and working with html and xml files.

## Performance Considerations
## The API in milestone 2 and the the API in milestone 3 both run almost instantly for small files. However, for large files the new API runs quicker, as the older API can take upwards of a few minutes. This could be because the previous milestone implementation uses the lower function twice for comparisons for every tag, which would take longer for every tag. Otherwise, in both implementations the whole file input is taken in all at once and then passed to the parser. This seems to be the most efficient implemenation as modern input and output is fast. What takes the longest is the parsing and tree building of BeautifulSoup.

# Build Script 

# For first time setup to make sure imports work
## From the root directory run: 
```
pip install -e
``` 

# For testing the updated API
## Navigate into the test directory from the root directory 
```
cd bs4/tests
```
## Then run the current tests in test_replacer.py
``` 
pytest test_replacer.py -s
```

# For running task 7 with the updated API
## Navigate into the m3 directory from the root directory
```
cd apps/m3
```
## Then run the program with a file 
## Example:
```
python task7.py "../../romeoAndJuliet.html"
```
## The new output file should contain the changed or new class attributes