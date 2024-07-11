#!/usr/bin/env python3
import numpy as np
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(Scene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        plane = NumberPlane(
            # X/Y ration should always be 16/9, but with some space after the last tick:
            # 17.6/9.9
            # 12.8/7.2
            # 9.6/5.4
            # 6.4/3.6
            # 4.8/2.7
            # 3.2/1.8
            # 2.4/1.35
            # 1.6/0.9
            x_range=(-0.2, 9.4),
            y_range=(-0.2, 5.2),
            x_length=12.8,
            y_length=7.2,

            axis_config={
                "include_numbers": True,
                "include_ticks": True,
            },
            background_line_style={
                "stroke_opacity": 0,  # Removes grid
            }
        )

        # Axes labels config
        # plane.get_axis(0).set(color=BLUE)
        # plane.get_axis(1).set(color=BLUE)
        axes_labels = plane.get_axis_labels()

        self.add(plane, axes_labels)

        # The scene itself
        def func(x):
            return np.power(x - 3.7, 3) / 5 + np.power(x - 3.7, 2) / 5 - (x - 3.7) + 2

        # Start from 0.2 to have negative Y values on the graph
        graph = plane.plot(func, color=WHITE, x_range=[0.333, 10])

        point_a_x = 4
        point_b_x = 6
        point_a_coord = plane.coords_to_point(point_a_x, func(point_a_x))
        point_b_coord = plane.coords_to_point(point_b_x, func(point_b_x))
        dot_a = Dot(point_a_coord)
        dot_b = Dot(point_b_coord)
        secant_line = Line(point_a_coord, point_b_coord)
        secant_line.set_length(5)

        m = (func(point_b_x) - func(point_a_x)) / (point_b_x - point_a_x)
        b = func(point_a_x) - m * point_a_x

        math_text = MathTex(r"m = \frac{f(x_{b}) - f(x_{a})}{x_{b} - x_{a}} \approx " + str(round(m, 3)))
        math_text_line = MathTex(r"y = mx + b")
        math_text_line_shift = MathTex(r"b = y_{a} - mx_{a} = " + str(round(func(point_a_x), 2)) + "-" +
                                       str(round(m, 3)) + "*" + str(round(point_a_x)) + r"\approx" + str(round(b, 3)))
        (VGroup(math_text, math_text_line, math_text_line_shift)
         .arrange(DOWN).shift(np.array([-2, 2.7, 0])))

        point_a_label = (MathTex(r"[" + str(point_a_x) + "," + str(round(func(point_a_x), 2)) + "]")
                         .next_to(dot_a, direction=LEFT, buff=0.4))
        point_b_label = (MathTex(r"[" + str(point_b_x) + "," + str(round(func(point_b_x), 2)) + "]")
                         .next_to(dot_b, buff=0.4))

        # Draw a parallel line with a calculated slope
        def secant_line_func(x):
            return m * x + b

        math_text_secant_line = MathTex("y = " + str(round(m, 3)) + "x + (" + str(round(b, 3)) + ")",
                                        color=YELLOW).rotate(35.5 * DEGREES).shift(np.array([0.4, 0.4, 0]))
        secant_line_calculated = plane.plot(secant_line_func, color=YELLOW, x_range=[-1, 10])

        self.add(math_text, math_text_line, math_text_line_shift)
        self.add(graph)
        self.play(
            Create(dot_a),
            Create(dot_b),
        )
        self.play(
            Write(point_a_label),
            Write(point_b_label),
        )
        # self.play(
        #     Create(secant_line)
        # )
        # self.wait()
        self.play(
            Create(secant_line_calculated)
        )
        self.play(
            Write(math_text_secant_line)
        )
        self.wait(3)
