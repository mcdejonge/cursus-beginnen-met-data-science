The file titanic.csv was downloaded from https://github.com/datasciencedojo/datasets/

The file titanic_clean was processed as follows:
- For the Age column, NaN values were imputed using a random distribution with the same median and standard deviation as the original values.
- Additional columns were added assigning classes to fares:
```python
    categories = [
    { 'min' : 0,
     'max' : 10,
     'category' : 'Deck class'},
    { 'min' : 10,
     'max' : 45,
     'category' : 'Third class'},
    { 'min' : 45,
     'max' : 100,
     'category' : 'Second class'},
    { 'min' : 100,
     'max' : 200,
     'category' : 'First class'},
    { 'min' : 200,
     'max' : 999, # Some unlikely large number
     'category' : 'Executive class'},
]
```
- An addtional column was added indicating whether a cabin was known or not.
- NaN values in the cabin column were set to "UNKNOWN"
- NaN values in the embarked column were set to the most common value.
