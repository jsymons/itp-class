# Question 5

Write a function `calculate_tax` that receives a number (`income`) and calculates how much of Federal taxes is due, according to the following table (all income is multiplied by ONE percentage, does not work like USA taxes):

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
calculate_tax(income)  # 4500

# Example 2
income = 80000  # $80,000 is more than $75,000 but less than $100,000
calculate_tax(income)  # 24000

# Example 3
income = 210000  # $210,000 is more than $100,000
calculate_tax(income)  # 73500
```
