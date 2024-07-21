#!/usr/bin/env python3
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
            x_range=(-0.5, 12.3),
            y_range=(-0.5, 6.7),
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
        axes_labels = plane.get_axis_labels()

        self.add(plane, axes_labels)

        # --------------------------------------------------------------------------------------------------------------
        # Calculating
        def func(x):
            # y = 0.0003 * x ^ 5 - 0.012 * x ^ 4 + 0.164 * x ^ 3 - 0.931 * x ^ 2 + 2.045 * x
            return (0.0003 * np.power(x, 5) - 0.012 * np.power(x, 4) + 0.164 * np.power(x, 3) - 0.931 * np.power(x, 2)
                    + 2.045 * x)

        # Solved equation f(x) = 0
        func_x_intersection_1 = 11.7457

        point_a_x = 5
        point_b_x = 7
        point_a_y = round(func(point_a_x), 2)
        point_b_y = round(func(point_b_x), 2)
        point_a_coord = plane.coords_to_point(point_a_x, point_a_y)
        point_b_coord = plane.coords_to_point(point_b_x, point_b_y)

        m = round((point_b_y - point_a_y) / (point_b_x - point_a_x), 3)
        c = round(point_a_y - m * point_a_x, 3)

        def secant_line_func(x):
            return m * x + c

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        graph = plane.plot(func, color=WHITE, x_range=[0, func_x_intersection_1])
        graph_func_label = MathTex(r"f(x)", color=WHITE).shift(np.array([-4.2, -1.2, 0.0]))

        func_x_intersection_1_line = DashedLine(plane.coords_to_point(func_x_intersection_1, -10, 0),
                                                plane.coords_to_point(func_x_intersection_1, 10, 0),
                                                dash_length=0.1, stroke_opacity=0.5)

        dot_a = Dot(point_a_coord)
        dot_b = Dot(point_b_coord)

        math_text_a_b = MathTex(
            r"a_{x} = " + str(point_a_x) + ",\quad b_{x} = " + str(point_b_x)
        ).shift(np.array([0, 3, 0]))
        math_text_m = MathTex(
            r"m = \frac{f(b_{x}) - f(a_{x})}{b_{x} - a_{x}} \approx " + str(m)
        ).shift(np.array([0, 2.2, 0]))
        math_text_line = MathTex(r"y = mx + c").shift(np.array([0, 1.4, 0]))
        math_text_line_calculate = MathTex(
            r"c = a_{y} - ma_{x} = " + str(point_a_y) + "-"
            + str(m) + "*" + str(point_a_x) + r"\approx" + str(c)
        ).shift(np.array([0, 0.8, 0]))
        math_text_secant_line = MathTex(
            "y = " + str(m) + "x + " + str(c), color=YELLOW
        ).shift(np.array([0, 0.2, 0]))

        point_a_label = (MathTex(r"[" + str(point_a_x) + "," + str(point_a_y) + "]")
                         .next_to(dot_a, direction=DOWN, buff=0.2))
        point_b_label = (MathTex(r"[" + str(point_b_x) + "," + str(point_b_y) + "]")
                         .next_to(dot_b, direction=DOWN, buff=0.2))

        secant_line_calculated = plane.plot(secant_line_func, color=YELLOW, x_range=[-1, 13])

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.add(func_x_intersection_1_line)
        self.play(
            Create(graph),
            Write(graph_func_label))
        self.wait()

        self.play(Write(math_text_a_b))
        self.play(
            Create(dot_a),
            Create(dot_b),
        )
        self.play(
            Write(point_a_label),
            Write(point_b_label),
        )

        self.play(Write(math_text_m))
        self.play(Write(math_text_line))
        self.play(Write(math_text_line_calculate))
        self.wait()

        # self.play(
        #     Create(secant_line)
        # )
        # self.wait()
        self.play(
            Write(math_text_secant_line)
        )
        self.play(
            Create(secant_line_calculated)
        )
        self.wait(3)
