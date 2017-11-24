# ExList
This is a wrapper of Python's List.
You can use `map`, `filter` and `fold` succesively by method chain.

## Install
```
pip install exlist
```
## Usage
```python3
>>> from exlist import ExList
>>> l = ExList([1,2,3,4])
>>> l.map(lambda x: x*3)
[3, 6, 9, 12]
>>> l.map(lambda x: x*3).filter(lambda x: x%2 == 0)
[6, 12]
>>> l.map(lambda x: x*3).filter(lambda x: x%2 == 0).fold(0, lambda x,y: x+y)
18
```
