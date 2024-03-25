# Linear Algebra

* [Introduction to Vectors](#introduction-to-vectors)
    * [Vector Magnitude and Direction](#vector-magnitude-and-direction)
    * [Vector Addition](#vector-addition)
    * [Vector Scalar Multiplication](#vector-scalar-multiplication)
    * [Vector Linear Combination](#vector-linear-combination)
    * [Vector Linear Dependence](#vector-linear-dependence)
    * [Vector Span and Basis](#vector-span-and-basis)
    * [Vector Space](#vector-space)
    * [Vector Dot Product](#vector-dot-product)
    * [Vector Cross Product](#vector-cross-product)
    * [Calculating Angles Between Vectors](#calculating-angles-between-vectors)
* [Introduction to Matrices](#introduction-to-matrices)

## Introduction to Vectors

![Vectors](vectors.gif)

A vector may have many definitions: a point in space, an ordered list of numbers, a quantity with magnitude and
direction, etc. More abstractly, a vector is simply an element of a [vector space](#vector-space). All these diverse
things are gathered under the common name of vector because, for certain types of questions, a common way of reasoning
can be applied to all of them.

A vector can be written in matrix notation:

```math
\vec{a} = 
\begin{bmatrix} 
a_{1}   \\ 
a_{2}   \\
\cdots  \\
a_{n}
\end{bmatrix}
```

### Vector Magnitude and Direction

The **magnitude of a vector** ( $|\vec{a}|$ ) is the distance from the endpoint of the vector to the origin. It's a
number that represents the length of the vector independent of the direction. To calculate the magnitude of a vector,
we can use the [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem):

```math
|\vec{a}|=\sqrt{a_{x}^2 + a_{y}^2}
```

```math
|\vec{a}|=\sqrt{a_{x}^2 + a_{y}^2 + a_{z}^2}
```

A **unit (normalized) vector** ( $\hat{a}$ ), on the other hand, represents the direction of the vector independent of
its length. The magnitude of a unit vector is always 1. To calculate the unit vector of any vector, we take the
original vector and divide it by its magnitude:

```math
\hat{a} = \frac{\vec{a}}{|\vec{a}|}
```

We can use these two components to re-create the original vector by multiplying the unit vector by the length of the
original vector:

```math
\vec{a} = \hat{a} * |\vec{a}|
```

![Vectors](vectors_magnitude_direction.gif)

### Vector Addition

Graphically, we can think of **adding two vectors** together as placing these vectors so the tail of the second one
sits on the tip of the first one. The sum is a vector drawn from the origin to the tip of the second vector.

**Vector subtraction** works similarly. We place the tip of the smaller vector to sit on the tip of the bigger one and
draw the result vector from the origin to the tail of the smaller vector.

Numerically, we add/subtract vectors **component by component**:

```math
\vec{c} = \vec{a} + \vec{b} = \begin{bmatrix} a_{x} + b_{x} \\ a_{y} + b_{y} \end{bmatrix}
```

```math
\vec{c} = \vec{a} + \vec{b} = \begin{bmatrix} a_{x} + b_{x} \\ a_{y} + b_{y} \\ a_{z} + b_{z} \end{bmatrix}
```

![Vectors](vectors_addition.gif)

### Vector Scalar Multiplication

Graphically, we **multiply a vector by a number (scalar)** to either stretch or squish the vector (scale it).
Multiplying a vector by a negative number also **flips its direction**.

Numerically, we multiply/divide every **vector's component by the number**:

```math
\vec{a} * c = \begin{bmatrix} a_{x} * c \\ a_{y} * c \end{bmatrix}
```
```math
\vec{a} * c = \begin{bmatrix} a_{x} * c \\ a_{y} * c \\ a_{z} * c \end{bmatrix}
```

![Vectors](vectors_number_multiplication.gif)

### Vector Linear Combination

**Linear combinations** of vectors are obtained by using [vector addition](#vector-addition) and
[vector scalar multiplication](#vector-scalar-multiplication). For example, a linear combination of vectors
$\vec{v_{1}}$ and $\vec{v_{2}}$ would be an expression of the form $c_{1}\vec{v_{1}} + c_{2}\vec{v_{2}}$, where $c_{1}$
and $c_{2}$ are some constants.

### Vector Linear Dependence

Vectors are said to be **linearly dependent** if there exists a nontrivial (where scalars are not all zero)
[linear combination](#vector-linear-combination) of the vectors that equals the zero vector:

```math
c_{1}\vec{v_{1}} + c_{2}\vec{v_{2}} + ... + c_{n}\vec{v_{n}} = 0
```

If the set of vectors is **infinite**, the vectors in it are considered to be linearly dependent if the set contains a
**finite subset that is linearly dependent**.

Graphically, vectors are linearly dependent if **two vectors are on the same line** (for 2D) or if **three vectors are
on the same plane** (for 3D). It means that **one vector can be expressed as a linear combination of the other/s**. The
maximum number of possible linearly independent vectors is the same as the dimension of the
[vector space](#vector-space).

![Vectors](vectors_dependence.gif)

### Vector Span and Basis

The **span** of vectors is the set of all their [linear combinations](#vector-linear-combination). The **basis** of a
[vector space](#vector-space) is a set of linearly independent vectors that **span** the full space. For example, by
using linear combinations of any two linearly independent vectors, we can create any vector in the 2D space.

The **basis** vectors in the $x,y,z$ coordinate system are vectors $\hat{i},\hat{j},\hat{k}$ (i-hat, j-hat, and k-hat).
We can use these basis vectors to describe any other vector of 2D/3D space. For example a vector with coordinates
`[1.5, 0.5]` can be described this way:

```math
\begin{bmatrix} 1.5 \\ 0.5 \end{bmatrix} = (1.5 * \hat{i}) + (0.5 * \hat{j})
```

![Vectors](vectors_span_and_basis.gif)

### Vector Space

A **vector space $\mathbb{V}$**, simplified, is a collection of vectors, along with two defined operations you can do
on them: [vector addition](#vector-addition) and [scalar multiplication](#vector-scalar-multiplication).
Vector spaces are characterized by their dimension, which specifies the maximum number
of [linearly independent](#vector-linear-dependence) vectors in the space.

To have a vector space, the **eight following axioms must be satisfied**:

- Associativity of vector addition:
  $`\vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w}`$;
- Commutativity of vector addition:
  $`\vec{u} + \vec{v} = \vec{v} + \vec{u}`$;
- Identity element of vector addition (zero vector $\vec{0}$):
  $`\vec{v} + \vec{0} = \vec{v}`$;
- Inverse elements of vector addition:
  $`\vec{v} + (-\vec{v}) = \vec{0}`$;
- Compatibility of scalar multiplication with field multiplication:
  $`a(b\vec{v}) = (ab)\vec{v}`$;
- Identity element of scalar multiplication:
  $`1\vec{v} = \vec{v}`$;
- Distributivity of scalar multiplication with respect to vector addition:
  $`a(\vec{v} + \vec{u}) = a\vec{v} + a\vec{u}`$;
- Distributivity of scalar multiplication with respect to field addition:
  $`(a + b)\vec{v} = a\vec{v} + b\vec{v}`$.

Usually, we work with **real vector spaces $\mathbb{R}^n$** and **finite dimensions $n$**. A real vector space is a
vector space whose field of scalars is the field of [reals](https://en.wikipedia.org/wiki/Real_number) $\mathbb{R}$.

A [field](https://en.wikipedia.org/wiki/Field_mathematics) $\mathbb{F}$, simply speaking, is a set on which addition,
subtraction, multiplication, and division are defined such that the usual rules of algebra hold. The rules for fields
are more restrictive than ones for vector spaces (for example,
[multiplicative inverse](https://en.wikipedia.org/wiki/Multiplicative_inverse) is not explicitly defined for vectors
but is one of the field axioms). Thus, as a special case, a field is also a vector space over itself (for example,
$\mathbb{R}^n$ where $n=1$).

### Vector Dot Product

Numerically, the dot product can be calculated by multiplying vectors component-by-component and then adding the
results:

```math
\vec{a} \cdot \vec{b} = \begin{bmatrix} a_{x} \\ a_{y} \end{bmatrix} \cdot 
\begin{bmatrix} b_{x} \\ b_{y} \end{bmatrix} = a_{x} * b_{x} + a_{y} + b_{y}
```

The result of dot product is **always a scalar**.

This formula can be extended to work with **N-dimensional** vectors, but **can't be used with more than two vectors**:

```math
\vec{a} \cdot \vec{b} = \sum_{i=1}^N a_{i} * b_{i}
```

Geometrically, we can calculate dot product using another formula, which comes from the
[Law of Cosines](https://en.wikipedia.org/wiki/Law_of_cosines):

```math
\vec{a} \cdot \vec{b} = |\vec{a}| * |\vec{b}| * \cos(\theta)
```

The purpose of the dot product is to give us useful **information about angles and lengths simultaneously**. For
example, we use the dot product to calculate the work $W$ produced by a force $\vec{F}$ and caused the displacement
$\vec{s}$:

![Vectors](vectors_dot_product_work.gif)

In some cases, we don't care about the length, we only care about how much vectors are **pointing in the same
direction**. In this case, it's a lot easier to work with unit vectors. The dot product of two unit vectors equals
**the cosine value of the angle between them**. There are three most important angles for cosine: $0^{\circ}$ where
cosine equals 1, $90^{\circ}$ where cosine equals 0 and $180^{\circ}$ where cosine equals -1.

![Vectors](vectors_dot_product_unit.gif)

### Vector Cross Product

Let's start with 3D geometric representation first. The **cross product of two
[linearly independent](#vector-linear-dependence) vectors $\vec{a}\times\vec{b}$ is a vector**, which is perpendicular
to both $\vec{a}$ and $\vec{b}$, and thus normal to the plane containing them. This vector can be calculated using this
formula:

```math
\vec{a} \times \vec{b} = \hat{n} |\vec{a}|| \vec{b}| \sin\theta
```

where $\hat{n}$ is the unit vector perpendicular to both $\vec{a}$ and $\vec{b}$, and $\theta$ is the angle between
$\vec{a}$ and $\vec{b}$.

![Vectors](vectors_cross_product.gif)

The cross product of vectors in 2D space is not exactly defined. But its magnitude can still be calculated. **The
magnitude of the cross product equals the area of a parallelogram with the vectors for sides**. The result of the cross
product for two vectors in **2D space $|\vec{a} \times \vec{b}|$ is a scalar, which represents the area of this
parallelogram**.

Unlike the [dot product](#vector-dot-product), the cross product says **how different vectors are**, but with a nuance.
The cross product of two vectors is the biggest when they are **perpendicular to each other**.

![Vectors](vectors_cross_product_unit.gif)

Also, pay attention that the cross product is **anticommutative**:

```math
\vec{a} \times \vec{b} = -\vec{b} \times \vec{a}
```

The cross product is commonly used in computer graphics to calculate **the normal for a triangle or polygon** or in
physics to calculate **angular momentum and torque**.

Finally, let's calculate the cross product of two vectors numerically, using their components. The cross product can be
expressed in [matrix notation](#introduction-to-matrices) as a [formal determinant](#matrix-determinant):

```math
\vec{a} \times \vec{b} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix} = (a_2b_3-a_3b_2)\hat{i} + (a_3b_1-a_1b_3)\hat{j}+(a_1b_2-a_2b_1)\hat{k}
```

### Calculating Angles Between Vectors

Geometrical representation of both [dot product](#vector-dot-product) and [cross product](#vector-cross-product) can be
used to **calculate an angle between two vectors**:

```math
\theta = \arccos \frac{\vec{a} \cdot \vec{b}}{|\vec{a}||\vec{b}|}
```

```math
\theta = \arcsin \frac{|\vec{a} \times \vec{b}|}{|\vec{a}||\vec{b}|}
```

## Introduction to Matrices

A matrix is a collection of numbers, just like a vector. The difference is that a matrix is a table of numbers rather
than a list. We can think of vectors as matrices that have only one column/row.

A real matrix $A \in \mathbb{R}^{m \times n}$ with $m$ rows and $n$ columns can be written as:

```math
A = 
\begin{bmatrix} 
a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
\end{bmatrix}
```