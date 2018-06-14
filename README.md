# wrong

Evaluate your unit test skills

## Installation

You can install `wrong` through Python Package Index (PyPI):

```
pip install wrong
```

## Example with pytest

To evaluate your unit test skills, first write test functions for any of the modules in `wrong`. (We chose `wrong.sort` here) Then, import `sort` and run your test.

```
from wrong import sort

def test_sort_sorted():
    a = [1, 2, 3, 4]
    answer = [1, 2, 3, 4]
    sort(a)
    assert a == answer

def test_sort_unsorted():
    a = [1, 4, 2, 3]
    answer = [1, 2, 3, 4]
    sort(a)
    assert a == answer
```

If some of your unit tests fail, try testing with other implementations of sort with `wrong.importer(module_name, function_id).`

```
import wrong

sort = wrong.importer('sort', 0)

def test_sort_sorted():
    a = [1, 2, 3, 4]
    answer = [1, 2, 3, 4]
    sort(a)
    assert a == answer

def test_sort_unsorted():
    a = [1, 4, 2, 3]
    answer = [1, 2, 3, 4]
    sort(a)
    assert a == answer
```

`sort` has 1 correct implementation with id 0, and 4 incorrect implementations with ids 1, 2, 3, 4. If your tests pass for all correct implementations and fail for all incorrect implementations, your unit tests are working as intended!
