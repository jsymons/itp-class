# Advanced Nested Pyramid

Write a function `advanced_nested_pyramid()` that creates a string pyramid like the one shown below:

```
*
**
***
****
*****
```

The function should accept 3 parameters: the start level (1 in the previous example), the last level of the pyramid (5, in the previous example) and the character to use. Examples:

```python
advanced_nested_pyramid(start=1, last=5, character='*')
"""
*
**
***
****
*****
"""

advanced_nested_pyramid(start=1, last=3, character='@')
"""
@
@@
@@@
"""

advanced_nested_pyramid(start=3, last=7, character='A')
"""
AAA
AAAA
AAAAA
AAAAAA
AAAAAAA
"""
```
