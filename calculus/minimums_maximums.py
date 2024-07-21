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
            y_range=(-2.5, 2.7),
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

        def func_der_1(x):
            # y = 0.0015 * x ^ 4 - 0.048 * x ^ 3 + 0.492 * x ^ 2 - 1.862 * x + 2.045
            return 0.0015 * np.power(x, 4) - 0.048 * np.power(x, 3) + 0.492 * np.power(x, 2) - 1.862 * x + 2.045

        # Solved equation f'(x) = 0
        der_1_x_intersection_1 = 1.84562
        der_1_x_intersection_2 = 5.13267
        der_1_x_intersection_3 = 8.96076

        def func_der_2(x):
            # y = 0.006 * x ^ 3 - 0.144 * x ^ 2 + 0.984 * x - 1.862
            return 0.006 * np.power(x, 3) - 0.144 * np.power(x, 2) + 0.984 * x - 1.862

        # Solved equation f''(x) = 0
        der_2_x_intersection_1 = 3.16458
        der_2_x_intersection_2 = 7.1829

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        graph_func = plane.plot(func, color=WHITE, x_range=[0, func_x_intersection_1])
        graph_func_label = MathTex(r"f(x)", color=WHITE).shift(np.array([0.0, 1.6, 0.0]))

        graph_der_1 = plane.plot(func_der_1, color=YELLOW, x_range=[0, func_x_intersection_1])
        graph_der_1_label = MathTex(r"f'(x)", color=YELLOW).shift(np.array([0.0, 0.47, 0.0]))

        graph_der_2 = plane.plot(func_der_2, color=RED, x_range=[0, func_x_intersection_1])
        graph_der_2_label = MathTex(r"f''(x)", color=RED).shift(np.array([0.0, -0.6, 0.0]))

        func_x_intersection_1_line = DashedLine(plane.coords_to_point(func_x_intersection_1, -10, 0),
                                                plane.coords_to_point(func_x_intersection_1, 10, 0),
                                                dash_length=0.1, stroke_opacity=0.5)

        der_1_x_intersection_1_line = DashedLine(plane.coords_to_point(der_1_x_intersection_1, -10, 0),
                                                 plane.coords_to_point(der_1_x_intersection_1, 10, 0),
                                                 color=YELLOW, dash_length=0.1, stroke_opacity=0.5)

        der_1_x_intersection_1_dot_func = Dot(plane.coords_to_point(
            der_1_x_intersection_1, func(der_1_x_intersection_1), 0),
            color=YELLOW)

        der_1_x_intersection_1_dot_der_1 = Dot(plane.coords_to_point(der_1_x_intersection_1, 0, 0),
                                               color=YELLOW)

        der_1_x_intersection_2_line = DashedLine(plane.coords_to_point(der_1_x_intersection_2, -10, 0),
                                                 plane.coords_to_point(der_1_x_intersection_2, 10, 0),
                                                 color=YELLOW, dash_length=0.1, stroke_opacity=0.5)

        der_1_x_intersection_2_dot_func = Dot(plane.coords_to_point(
            der_1_x_intersection_2, func(der_1_x_intersection_2), 0),
            color=YELLOW)

        der_1_x_intersection_2_dot_der_1 = Dot(plane.coords_to_point(der_1_x_intersection_2, 0, 0),
                                               color=YELLOW)

        der_1_x_intersection_3_line = DashedLine(plane.coords_to_point(der_1_x_intersection_3, -10, 0),
                                                 plane.coords_to_point(der_1_x_intersection_3, 10, 0),
                                                 color=YELLOW, dash_length=0.1, stroke_opacity=0.5)

        der_1_x_intersection_3_dot_func = Dot(plane.coords_to_point(
            der_1_x_intersection_3, func(der_1_x_intersection_3), 0),
            color=YELLOW)

        der_1_x_intersection_3_dot_der_1 = Dot(plane.coords_to_point(der_1_x_intersection_3, 0, 0),
                                               color=YELLOW)

        der_2_x_intersection_1_line = DashedLine(plane.coords_to_point(der_2_x_intersection_1, -10, 0),
                                                 plane.coords_to_point(der_2_x_intersection_1, 10, 0),
                                                 color=RED, dash_length=0.1, stroke_opacity=0.5)

        der_2_x_intersection_1_dot_der_1 = Dot(plane.coords_to_point(
            der_2_x_intersection_1, func_der_1(der_2_x_intersection_1), 0),
            color=RED)

        der_2_x_intersection_1_dot_der_2 = Dot(plane.coords_to_point(der_2_x_intersection_1, 0, 0),
                                               color=RED)

        der_2_x_intersection_2_line = DashedLine(plane.coords_to_point(der_2_x_intersection_2, -10, 0),
                                                 plane.coords_to_point(der_2_x_intersection_2, 10, 0),
                                                 color=RED, dash_length=0.1, stroke_opacity=0.5)

        der_2_x_intersection_2_dot_der_1 = Dot(plane.coords_to_point(
            der_2_x_intersection_2, func_der_1(der_2_x_intersection_2), 0),
            color=RED)

        der_2_x_intersection_2_dot_der_2 = Dot(plane.coords_to_point(der_2_x_intersection_2, 0, 0),
                                               color=RED)

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.add(func_x_intersection_1_line)
        self.play(
            Write(graph_func_label),
            Create(graph_func)
        )
        self.wait()

        self.play(
            Write(graph_der_1_label),
            Create(graph_der_1)
        )
        self.wait()

        self.play(
            Create(der_1_x_intersection_1_dot_func),
            Create(der_1_x_intersection_1_dot_der_1),
            Create(der_1_x_intersection_1_line)
        )
        self.wait()

        self.play(
            Create(der_1_x_intersection_2_dot_func),
            Create(der_1_x_intersection_2_dot_der_1),
            Create(der_1_x_intersection_2_line)
        )
        self.wait()

        self.play(
            Create(der_1_x_intersection_3_dot_func),
            Create(der_1_x_intersection_3_dot_der_1),
            Create(der_1_x_intersection_3_line)
        )
        self.wait(5)

        self.play(
            Unwrite(graph_func_label),
            Uncreate(graph_func),

            Uncreate(der_1_x_intersection_1_dot_func),
            Uncreate(der_1_x_intersection_1_dot_der_1),
            Uncreate(der_1_x_intersection_1_line),

            Uncreate(der_1_x_intersection_2_dot_func),
            Uncreate(der_1_x_intersection_2_dot_der_1),
            Uncreate(der_1_x_intersection_2_line),

            Uncreate(der_1_x_intersection_3_dot_func),
            Uncreate(der_1_x_intersection_3_dot_der_1),
            Uncreate(der_1_x_intersection_3_line)
        )

        self.play(
            Write(graph_der_2_label),
            Create(graph_der_2)
        )
        self.wait()

        self.play(
            Create(der_2_x_intersection_1_dot_der_1),
            Create(der_2_x_intersection_1_dot_der_2),
            Create(der_2_x_intersection_1_line)
        )
        self.wait()

        self.play(
            Create(der_2_x_intersection_2_dot_der_1),
            Create(der_2_x_intersection_2_dot_der_2),
            Create(der_2_x_intersection_2_line)
        )
        self.wait(5)
