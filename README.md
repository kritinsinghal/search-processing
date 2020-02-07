# nuffsaid coding challenge

As stated, I have added three files - search_schools.py, search_schools1.py and count_schools.py. The instruction to run each has been given below.

Note: search_schools1.py is an algorithm with faster preprocessing time though the search may not be the best.

## Running count_schools.py
1. Clone the repository to your local directory.
2. Visit the directory
3. `python` run the following command in your terminal
4. `import count_schools` followed by `count_schools.print_counts()` in the python window

## Running search_schools.py
For search_schools, I have designed a preprocessing algorithm and wrapped the search function and the preprocessing algorithm inside a class. This is a sample script to run the search query:

```
from search_schools import SearchSchool
p = SearchSchool() // preprocessor
query = "jefferson belleville"
start = datetime.datetime.now()
p.school_search(query)
end = datetime.datetime.now()
print(end-start)
```
