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
            x_range=(-0.1, 2.1, 0.5),
            y_range=(-0.1, 1.1, 0.5),
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
            return - np.power(x, 2) + 2 * x

        def func_der(x):
            return - 2 * x + 2

        point_a_x_tracker = ValueTracker(0.4)

        def point_a_x():
            return round(point_a_x_tracker.get_value(), 3)

        def point_a_y():
            return round(func(point_a_x()), 3)

        def m():
            return round(func_der(point_a_x()), 3)

        def c():
            return round(point_a_y() - m() * point_a_x(), 3)

        def secant_line_func(x):
            return m() * x + c()

        def point_a_coord():
            return plane.coords_to_point(point_a_x(), point_a_y())

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        graph = plane.plot(func, color=RED, x_range=[0, 2])
        graph_func_label = MathTex(r"f(x) = -x^2 + 2x", color=RED).shift(np.array([0, 2.2, 0]))

        def dot_a_func():
            return Dot(point_a_coord())

        dot_a = dot_a_func()
        dot_a.add_updater(lambda x: x.become(dot_a_func()))

        def secant_line_calculated_func():
            return plane.plot(secant_line_func, color=YELLOW, x_range=[point_a_x() - 0.25, point_a_x() + 0.25])

        secant_line_calculated = secant_line_calculated_func()
        secant_line_calculated.add_updater(lambda x: x.become(secant_line_calculated_func()))

        def math_text_func():
            return MathTex(r"f(" + str(point_a_x()) + r") \approx " + str(point_a_y())).shift(np.array([0, 1.4, 0]))

        math_text = math_text_func()
        math_text.add_updater(lambda x: x.become(math_text_func()))

        math_text_der = MathTex(r"\frac{d}{dx}f(x) = -2x + 2").shift(np.array([0, 0.6, 0]))

        def math_text_func_der_calc():
            return MathTex(r"m = \frac{d}{dx}f(" + str(point_a_x()) + r") \approx " + str(m())).shift(np.array([0, -0.2, 0]))

        math_text_der_calc = math_text_func_der_calc()
        math_text_der_calc.add_updater(lambda x: x.become(math_text_func_der_calc()))

        def math_text_func_c():
            return MathTex(r"c = y_a - m * x_a \approx" + str(c())).shift(np.array([0, -1, 0]))

        math_text_c = math_text_func_c()
        math_text_c.add_updater(lambda x: x.become(math_text_func_c()))

        def math_text_func_line_calc():
            return (MathTex(r"g(x) = m * x + c \approx" + str(m()) + r"x + " + str(c()), color=YELLOW)
                    .shift(np.array([0, -1.8, 0])))

        math_text_line_calc = math_text_func_line_calc()
        math_text_line_calc.add_updater(lambda x: x.become(math_text_func_line_calc()))

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.play(
            Create(graph),
            Write(graph_func_label))
        self.play(
            Create(dot_a),
            Create(secant_line_calculated),
            Write(math_text),
            Write(math_text_der),
            Write(math_text_der_calc),
            Write(math_text_c),
            Write(math_text_line_calc),
        )
        self.play(
            point_a_x_tracker.animate.set_value(0.75),
            run_time=8)
        self.play(
            point_a_x_tracker.animate.set_value(0.4),
            run_time=2)
        self.wait(20)
