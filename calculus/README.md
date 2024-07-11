# Calculus
* [Derivative](#derivative)
    * [The Average Rate of Change](#the-average-rate-of-change)
    * [The Instant Rate of Change (Derivative)](#the-instant-rate-of-change-derivative)
    * [Manual Derivative Calculation](#manual-derivative-calculation)

## Derivative

### The Average Rate of Change

The **average rate of change** for $f(x)$ on the interval $[a, b]$ is **the slope of a secant line** between two points
$(a, f(a))$ and $(b, f(b))$.

Numerically, the slope of a secant line equals **rise over run**:

```math
m = \frac{\Delta{y}}{\Delta{x}} = \frac{f(x_{b}) - f(x_{a})}{x_{b} - x_{a}}
```

We can find a full formula of a secant line using a **line formula $y = mx + b$ and plugging in the slope and the
coordinates of any intersection point** ($a$ or $b$).

![Secant Line](secant_line.gif)

In the example above, we calculated the average rate of change on the interval $[a, b]$. Now **let's give these values 
some real-world meaning**. Let's consider I went for a walk and this **graphic shows a distance from me to my home over 
time**. $y$ denotes a distance in kilometers and $x$ denotes time in hours I spent walking *(ignore that the graphic 
doesn't start at 0; let's assume I started the timer before actually going out)*. 

So, the average rate of change of the distance I walked on the interval from the 4th hour of my trip until the 6th hour 
is approximately $0.734$. What's the average rate of change of the distance? **It's speed**. This means that my average 
speed at this interval was approximately $0.734 km/h$.

### The Instant Rate of Change (Derivative)

The idea of the **instant rate of change** (which is also called a **derivative**) is similar to the
[average rate of change](#the-average-rate-of-change), but the **run is approaching zero**.

If we set $h = x_{b} - x_{a}$, we can rewrite the formula of the average rate of change:

```math
m = \frac{f(x + h) - f(x)}{h}
```

To get the formula of the instant rate of change (derivative), $h$ must be approaching 0:

```math
m = \frac{df}{dx} = \lim_{h \to 0}\frac{f(x + h) - f(x)}{h}
```

It doesn't matter if we **approach the point from the right or the left side** (assuming both limits exist) we get the 
same result:

```math
\lim_{h \to 0}\frac{f(x + h) - f(x)}{h} = \lim_{h \to 0}\frac{f(x) - f(x - h)}{h}
```

Graphically, the **instant rate of change** for $f(x)$ at the point $a$ is **the slope of a tangent line** at a point
$a$. The smaller $h$ we take for the calculation - the better result we get:

![Tangent Line](tangent_line.gif)

Let's again **give these values some real-world meaning**. If this graphic represents **a distance from me to my home 
over time** when I went for a walk *(just like in the [average rate of change](#the-average-rate-of-change) example)*, 
the **instant rate of change** actually represents my real speed in any given moment of time.

### Manual Derivative Calculation

The approach above is usually used in **computers to calculate the derivative**, but it only gives an **approximated
result**. If we directly plug in $h=0$ into the derivative formula, we get an **indeterminate expression**:

```math
\frac{f(x + h) - f(x)}{h} = \frac{f(x + 0) - f(x)}{0} = \frac{0}{0}
```

To calculate the exact value, we need to use some algebra. Let's take a simple function $f(x) = x^3$ as an example and
let's try to calculate the value of the derivative:

```math
\lim_{h \to 0}\frac{(x + h)^3 - x^3}{h} = \lim_{h \to 0}\frac{x^3 + h^3 + 3x^2h + 3xh^2 - x^3}{h} =
\lim_{h \to 0}(h^2 + 3x^2 + 3xh)
```

Now, if we plug in $h=0$:

```math
0^2 + 3x^2 + 3x * 0 = 3x^2
```

This is exactly the derivative that we get for $f(x) = x^3$ with the
[rules of computation](https://en.wikipedia.org/wiki/Derivative#Rules_of_computation).

Let's calculate the exact derivative for the example of the previous section. The function I used in that example (I
know it's not pretty) is:

```math
f(x) = 0.2x^3 - 2.02x^2 + 5.734x - 1.6926
```

The derivative of this function is:

```math
\frac{df}{dx} = 0.6x^2 - 4.04x + 5.734
```

Now, if we put $x=5$ in the exact derivative we get:

```math
0.6 * 5^2 - 4.04 * 5 + 5.734 = 15 - 20.2 + 5.734 = 0.534
```

Using $h = 0.0001$, the value of the derivative in the point $x=5$ calculated by the computer is 
**$0.5340980019985508$**, which is pretty close.


