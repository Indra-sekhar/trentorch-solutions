# Second Largest Value

Beginner | dsa-sheet | arrays | array-basics

Return the **second largest different value** in `nums`. Equal values count once, so in `[7, 7, 5]` the second largest is `5`. If there are fewer than two different values, return `-1`.

### Examples

**Example 1**

Input:

```python
second_largest([4, 9, 9, 6])
```

Output:

```text
6
```

The largest is 9, the second largest different value is 6.

**Example 2**

Input:

```python
second_largest([5, 5, 5])
```

Output:

```text
-1
```

Only one different value, so the answer is `-1`.

### Constraints

- `0 <= len(nums) <= 3 * 10**5`
- `0 <= nums[i] <= 10**9`
