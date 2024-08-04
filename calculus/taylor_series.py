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
            x_range=(-6.4, 6.4),
            y_range=(-3.6, 3.6),
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
            return np.cos(x)

        def approximation_1(x):
            return 1

        def approximation_3(x):
            return 1 - 0.5 * np.power(x, 2)

        def approximation_5(x):
            return 1 - 1 / 2 * np.power(x, 2) + 1 / 24 * np.power(x, 4)

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        graph_func = plane.plot(func, color=WHITE, x_range=[-8, 8])
        graph_func_label = MathTex(r"f(x) = cos(x)", color=WHITE).shift(np.array([5, -1.5, 0.0]))

        graph_approximation_1 = plane.plot(approximation_1, color=YELLOW, x_range=[-8, 8])
        graph_approximation_1_label = MathTex(r"f(x) = 1", color=YELLOW).shift(np.array([-3.5, 3, 0.0]))

        graph_approximation_2_label = MathTex(r"f(x) = 1 + 0x", color=YELLOW).shift(np.array([-3.5, 3, 0.0]))

        graph_approximation_3 = plane.plot(approximation_3, color=YELLOW, x_range=[-8, 8])
        graph_approximation_3_label = (MathTex(r"f(x) = 1 + 0x - \frac{1}{2}x^2", color=YELLOW)
                                       .shift(np.array([-3.5, 3, 0.0])))

        graph_approximation_4_label = (MathTex(r"f(x) = 1 + 0x - \frac{1}{2}x^2 + 0x^3", color=YELLOW)
                                       .shift(np.array([-3.5, 3, 0.0])))

        graph_approximation_5 = plane.plot(approximation_5, color=YELLOW, x_range=[-8, 8])
        graph_approximation_5_label = (MathTex(r"f(x) = 1 + 0x - \frac{1}{2}x^2 + 0x^3 + \frac{1}{24}x^4",
                                               color=YELLOW)
                                       .shift(np.array([-3.5, 3, 0.0])))

        graph_approximation_5_simplified_label = (MathTex(r"f(x) = 1 - \frac{1}{2}x^2 + \frac{1}{24}x^4",
                                                          color=YELLOW)
                                                  .shift(np.array([-3.5, 3, 0.0])))

        # Choose the biggest one
        graph_approximation_label_background = BackgroundRectangle(graph_approximation_5_label,
                                                                   color=config.background_color,
                                                                   fill_opacity=0.9, buff=0.1)

        # A hack so we can come back to the first graph
        graph_approximation_1_copy = graph_approximation_1.copy()
        graph_approximation_1_label_copy = graph_approximation_1_label.copy()

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.add(graph_func, graph_func_label)
        self.add(graph_approximation_1, graph_approximation_label_background, graph_approximation_1_label)
        self.wait()
        self.play(ReplacementTransform(graph_approximation_1_label, graph_approximation_2_label))
        self.wait(2)
        self.play(
            ReplacementTransform(graph_approximation_2_label, graph_approximation_3_label),
            ReplacementTransform(graph_approximation_1, graph_approximation_3)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(graph_approximation_3_label, graph_approximation_4_label)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(graph_approximation_4_label, graph_approximation_5_label),
            ReplacementTransform(graph_approximation_3, graph_approximation_5),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(graph_approximation_5_label, graph_approximation_5_simplified_label),
        )
        self.wait(2)
        self.play(
            ReplacementTransform(graph_approximation_5_simplified_label, graph_approximation_1_label_copy),
            ReplacementTransform(graph_approximation_5, graph_approximation_1_copy),
        )
        self.wait()
