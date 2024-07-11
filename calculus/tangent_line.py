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

        # Simplified manually
        # def func_simplified(x):
        #     return np.power(x, 3) / 5 - 2.02 * np.power(x, 2) + 5.734 * x - 1.6926

        def func_derivative(x):
            return np.power(x, 2) * 3 / 5 - 4.04 * x + 5.734

        graph = plane.plot(func, color=WHITE, x_range=[0.333, 10])
        # graph2 = plane.plot(func_simplified, color=YELLOW, x_range=[0.2, 10])
        # graph_derivative = plane.plot(func_derivative, color=YELLOW, x_range=[0, 10])

        h = ValueTracker(1)
        point_a_x = 5
        point_a_coord = plane.coords_to_point(point_a_x, func(point_a_x))
        dot_a = Dot(point_a_coord)
        dot_b = Dot(plane.coords_to_point(point_a_x + h.get_value(), func(point_a_x + h.get_value())))

        # Not used because of the updater
        m = (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value()
        b = func(point_a_x) - m * point_a_x
        print("M in point a: " + str((func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value()))
        print("M in point a calculated manually: " + str(func_derivative(point_a_x)))
        print("b: " + str(b))

        math_text_h = MathTex(r"h = " + str(h.get_value())).shift(np.array([-2, 3.5, 0]))
        math_text = (MathTex(r"m = \frac{f(x + h) - f(x)}{h} \approx "
                             + str(round((func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value(), 5)))
                     .shift(np.array([-2, 2.5, 0])))
        math_text_line_shift = (MathTex(r"b = y - mx = " + str(round(func(point_a_x), 2)) + "-" +
                                        str(round((func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value(),
                                                  5)) + "*" + str(round(point_a_x)) + r"\approx" + str(
            round(func(point_a_x) - (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value() * point_a_x,
                  5)))
                                .shift(np.array([-2, 1.5, 0])))

        point_a_label = (MathTex(r"[" + str(point_a_x) + "," + str(round(func(point_a_x), 2)) + "]")
                         .next_to(dot_a, direction=DR, buff=0.1))

        # Draw a parallel line with a calculated slope
        secant_line_calculated = plane.plot(
            lambda x: (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value() * x +
                      func(point_a_x) - (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value() * point_a_x,
            color=YELLOW, x_range=[-1, 10])

        # Updaters
        math_text_h.add_updater(
            lambda x: x.become(
                MathTex(r"h = " + str(round(h.get_value(), 5))).shift(np.array([-2, 3.5, 0]))
            )
        )

        math_text.add_updater(
            lambda x: x.become(
                (MathTex(r"m = \frac{f(x + h) - f(x)}{h} \approx "
                         + str(round((func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value(), 5)))
                 .shift(np.array([-2, 2.5, 0])))
            )
        )

        math_text_line_shift.add_updater(
            lambda x: x.become(
                (MathTex(r"b = y - mx = " + str(round(func(point_a_x), 2)) + "-" +
                         str(round((
                                           func(point_a_x + h.get_value()) - func(point_a_x)
                                   ) / h.get_value(), 5)) + "*" + str(round(point_a_x)) +
                         r"\approx" + str(round(
                    func(point_a_x) - (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value() * point_a_x,
                    5)))
                 .shift(np.array([-2, 1.5, 0])))
            )
        )

        dot_b.add_updater(
            lambda x: x.become(
                Dot(plane.coords_to_point(point_a_x + h.get_value(), func(point_a_x + h.get_value())))
            )
        )

        secant_line_calculated.add_updater(
            lambda a: a.become(
                plane.plot(
                    lambda x: (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value() * x +
                              func(point_a_x) - (func(point_a_x + h.get_value()) - func(point_a_x)) / h.get_value() * point_a_x,
                    color=YELLOW, x_range=[-1, 10])
            )
        )

        self.add(
            math_text_h, math_text, math_text_line_shift,
            graph, dot_a, dot_b, point_a_label,
            secant_line_calculated
        )
        self.play(h.animate.set_value(0.00005), run_time=10, rate_func=exponential_decay)
        self.wait(1)
