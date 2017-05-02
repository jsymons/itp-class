# Question 5

Write a function `calculate_tax` that receives a number (`income`) and calculates how much of Federal taxes is due, according to the following table:

```
|    Income     | Tax Percentage |
| ------------- | -------------- |
| <= $50,000    |        15%     |
| <= $75,000    |        25%     |
| <= $100,000   |        30%     |
| > $100,000    |        35%     |
```

`<=` means "less than or equals to"
`>` means "greater than

**Examples:**

```python
# Example 1
income = 30000  # $30,000 is less than $50,000
calculate_tax(income)  # $30,000 * 0.15  = 4500 = $4,500

# Example 2
income = 80000  # $80,000 is more than $75,000 but less than $80,000
calculate_tax(income)  # $80,000 * 0.25 = 20000 = $20,000

# Example 3
income = 210000  # $210,000 is more than $100,000
calculate_tax(income)  # $210,000 * 0.35 = 73500 = $73,500
```
