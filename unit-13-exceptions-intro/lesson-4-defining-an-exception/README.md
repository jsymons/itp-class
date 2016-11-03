# Defining an Exception

Create an empty exception named StringTooLongException. Remember that all exceptions must be derived from an `Exception` class.

```python
def string_check(a_string):
    if len(a_string) > 10:
        raise StringTooLongException
    else:
        return a_string
```