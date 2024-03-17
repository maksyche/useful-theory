# Linear Algebra
* [Vectors](#vectors)
    * [Vector Magnitude and Direction](#vector-magnitude-and-direction)

## Vectors
![Vectors](vectors/vectors.gif)

A vector may have many definitions: a point in space, an ordered list of numbers, a quantity with magnitude and
direction, etc. More abstractly, a vector is simply an element of a [vector space](#vector-space). All these diverse 
things are gathered under the common name of vector because, for certain types of questions, a common way of reasoning 
can be applied to all of them.

### Vector Magnitude and Direction
The **magnitude of a vector** ( $||\vec{a}||$ ) is the distance from the endpoint of the vector to the origin. It's a 
number that represents the length of the vector independent of the direction. To calculate the magnitude of a vector we 
can use the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem). 

A **unit (normalized) vector** ( $\hat{a}$ ), on the other hand, represents the direction of the vector independent of its length. 
The magnitude of a unit vector is always 1. To calculate the unit vector of any vector, we take the original vector and 
divide it by its magnitude: 
$`\hat{a} = \frac{\vec{a}}{||\vec{a}||}`$.

We can use these two components to re-create the original vector by multiplying the unit vector by the length of the 
original vector: 
$`\vec{a} = \hat{a} * ||\vec{a}||`$.

![Vectors](vectors/vectors_magnitude_direction.gif)

### Vector Addition
Graphically, we can think of **adding two vectors** together as placing these vectors so the tail of the second one 
sits on the tip of the first one. The sum is a vector drawn from the origin to the tip of the second vector.

**Vector subtraction** works similarly. We place the tip of the smaller vector to sit on the tip of the bigger one and 
draw the result vector from the origin to the tail of the smaller vector.

Numerically, we add/subtract vectors **component by component**: 
$`\vec{c} = \vec{a} + \vec{b} = \begin{bmatrix} x_{a} + x_{b} \\ y_{a} + y_{b} \end{bmatrix}`$

![Vectors](vectors/vectors_addition.gif)