#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(Scene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        circle = Circle(radius=1.5, color=WHITE)
        math = MathTex(r"\sigma(\sum_{i=1}^{n} w_i x_i + b)")
        in1 = (Line(start=np.array((-5.0, 0.0, 0.0)), end=np.array((-1.5, 0.0, 0.0)))
               .rotate(angle=-0.15 * PI, about_point=np.array((0.0, 0.0, 0.0))))
        inn = (Line(start=np.array((-5.0, 0.0, 0.0)), end=np.array((-1.5, 0.0, 0.0)))
               .rotate(angle=0.15 * PI, about_point=np.array((0.0, 0.0, 0.0))))
        x1_circle = (Circle(radius=0.5, color=WHITE).move_to(in1.get_start()).shift(np.array((-0.5, 0, 0)))
                     .rotate(angle=-0.15 * PI, about_point=in1.get_start()))
        x1 = MathTex("x_1").move_to(x1_circle.get_center())
        w1 = (MathTex("w_1").move_to(np.array((-3, 0.25, 0)))
              .rotate(angle=-0.15 * PI, about_point=np.array((0.0, 0.0, 0.0))))
        xn_circle = (Circle(radius=0.5, color=WHITE).move_to(inn.get_start()).shift(np.array((-0.5, 0, 0)))
                     .rotate(angle=0.15 * PI, about_point=inn.get_start()))
        xn = MathTex("x_n").move_to(xn_circle.get_center())
        wn = (MathTex("w_n").move_to(np.array((-3, -0.25, 0)))
              .rotate(angle=0.15 * PI, about_point=np.array((0.0, 0.0, 0.0))))
        dot1 = Dot().shift(np.array((x1_circle.get_center()[0], 1.4, 0)))
        dot2 = Dot().shift(np.array((x1_circle.get_center()[0], 0.7, 0)))
        dot3 = Dot().shift(np.array((x1_circle.get_center()[0], 0, 0)))
        dot4 = Dot().shift(np.array((x1_circle.get_center()[0], -0.7, 0)))
        dot5 = Dot().shift(np.array((x1_circle.get_center()[0], -1.4, 0)))
        out = Line(start=np.array((5.0, 0.0, 0.0)), end=np.array((1.5, 0.0, 0.0)))
        y_circle = Circle(radius=0.5, color=WHITE).move_to(out.get_start()).shift(np.array((0.5, 0, 0)))
        y = MathTex("y").move_to(y_circle.get_center())

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        # TODO: Neuron pulse animation???
        self.add(circle, math, in1, x1_circle, x1, w1,
                 inn, xn_circle, xn, wn, dot1, dot2, dot3, dot4, dot5, out, y_circle, y)
        self.wait()
