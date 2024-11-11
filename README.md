# FIRST LEVEL HEADING
## SECOND LEVEL HEADING
### THIRD LEVEL HEADING

# Styling
1. **This is bold text**
2. _This is italicized text_
3. ~~This is striken through text~~
4. **Bold and nested _Italicized_ text**
5. ***All bold and Italic***
6. This is a <sub>subscript</sub>
7. This is a <sup>superscript</sup>
8. This is <ins>underlined</ins>

# Quoting Text
Text that is not a quote
>Text that is a quote (with >, indent + diff color)

# Links
[This is the link for dillinger](https://dillinger.io/)

# Images
![Screenshot of octocat](https://cdn1.byjus.com/wp-content/uploads/2022/09/Dot-Product-Of-Two-Vectors-2.png)

# Lists
### Unordered
* CSE
+ ECE
- EEE

### Ordered
1. CSE
2. ECE
3. EEE

### Nested
1. Nested first
    - Nested 2
        - Nested 3

### Tasked lists
- [x] CSE
- [ ] ECE
- [ ] EEE

# Footnotes
This is a footnote[^1]
[^1]: my reference
  you can write i another line by adding 2 spaces preceeding the line
 
# Alerts
> [!IMPORTANT]
> This message is important

# Table
| Flood fill | Djikstra's |
| --- | --- |
|changes the area connected to a node in a multi-dimensional array | finds the shortest path between nodes in a graph.|
|The flood fill algorithm is used in image processing|used to find the shortest path in road networks|
|The time complexity of the flood fill algorithm is O(M*N), where M and N are the number of rows and columns|The time complexity of Dijkstra's algorithm is O(V^2)|

# Code
Python code for dot product of two vectors:
```
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same length")
    
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

result = dot_product(vector1, vector2)
print("Dot Product:", result)

```
# Mathematical Expression
Dot prodect of two vectors a and b:
$$a.b=|a||b|cos\theta$$
