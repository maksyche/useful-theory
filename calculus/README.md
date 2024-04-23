# Calculus
* [Derivative Definition](#derivative-definition)
    * [The Average Rate of Change](#the-average-rate-of-change)

## Derivative Definition

### The Average Rate of Change

The **average rate of change** for $f(x)$ on the interval $[a, b]$ is **the slope of a secant line** between two points
$(a, f(a))$ and $(b, f(b))$.

Numerically, the slope of a secant line equals **rise over run**:

```math
m = \frac{\Delta{y}}{\Delta{x}} = \frac{y_{b} - y_{a}}{x_{b} - x_{a}} = \frac{f(x + h) - f(x)}{h}
```

where $y = f(x)$ and $h = x_{b} - x_{a}$ _(obviously, but still)_.

We can find a full formula of a secant line using a **line formula $y = mx + b$ and plugging in the slope and the
coordinates of any intersection point** ($a$ or $b$).

![Secant Line](secant_line.gif)
