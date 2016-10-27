# Triple Nested Loop

Create a function `triple_nested_loop` that returns a string similar to this one:

```
....1
...22
..333
.4444
55555
```

To do it, you'll have to nest 2 for loops inside a bigger/outer for loop. You'll end up with something like this:

```python
for i in range(XXX):
    for j in range(YYY):
        pass
    for m in range(ZZZ):
        pass
```

The `triple_nested_loop` should receive a single parameter `size`. Example:

```python
triple_nested_loop(3)
"""
..1
.22
333
"""

triple_nested_loop(6)
"""
.....1
....22
...333
..4444
.55555
666666
"""
```
