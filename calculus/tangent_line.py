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

        def func_der_1(x):
            # y = 0.0015 * x ^ 4 - 0.048 * x ^ 3 + 0.492 * x ^ 2 - 1.862 * x + 2.045
            return 0.0015 * np.power(x, 4) - 0.048 * np.power(x, 3) + 0.492 * np.power(x, 2) - 1.862 * x + 2.045

        point_a_x_tracker = ValueTracker(5)
        point_b_x_tracker = ValueTracker(7)
        ending_point = 6
        end_h_value = 0.0001
        print("Real derivative: " + str(func_der_1(ending_point)))

        def point_a_x():
            return point_a_x_tracker.get_value()

        def point_b_x():
            return point_b_x_tracker.get_value()

        def h():
            return point_b_x() - point_a_x()

        def point_a_y():
            return func(point_a_x())

        def point_b_y():
            return func(point_b_x())

        def point_a_coord():
            return plane.coords_to_point(point_a_x(), point_a_y())

        def point_b_coord():
            return plane.coords_to_point(point_b_x(), point_b_y())

        def m():
            return (point_b_y() - point_a_y()) / h()

        def c():
            return point_a_y() - m() * point_a_x()

        def secant_line_func(x):
            return m() * x + c()

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        graph = plane.plot(func, color=WHITE, x_range=[0, func_x_intersection_1])
        graph_func_label = MathTex(r"f(x)", color=WHITE).shift(np.array([-4.2, -1.2, 0.0]))

        func_x_intersection_1_line = DashedLine(plane.coords_to_point(func_x_intersection_1, -10, 0),
                                                plane.coords_to_point(func_x_intersection_1, 10, 0),
                                                dash_length=0.1, stroke_opacity=0.5)

        rounding_value = 4

        def dot_a_func():
            return Dot(point_a_coord())

        dot_a = dot_a_func()
        dot_a.add_updater(lambda x: x.become(dot_a_func()))

        def dot_b_func():
            return Dot(point_b_coord())

        dot_b = dot_b_func()
        dot_b.add_updater(lambda x: x.become(dot_b_func()))

        def math_text_h_func():
            return MathTex(r"h = b_{x} - a_{x} = " + str(round(h(), rounding_value))).shift(np.array([0, 3, 0]))

        math_text_h = math_text_h_func()
        math_text_h.add_updater(lambda x: x.become(math_text_h_func()))

        def math_text_m_func():
            return (MathTex(r"m = \frac{f(b_{x}) - f(a_{x})}{h} \approx " + str(round(m(), rounding_value)))
                    .shift(np.array([0, 2.2, 0])))

        math_text_m = math_text_m_func()
        math_text_m.add_updater(lambda x: x.become(math_text_m_func()))

        math_text_line = MathTex(r"y = mx + c").shift(np.array([0, 1.4, 0]))

        def math_text_line_calculate_func():
            return MathTex(
                r"c = a_{y} - ma_{x} = "
                + str(round(point_a_y(), rounding_value))
                + "-" + str(round(m(), rounding_value))
                + "*" + str(round(point_a_x(), rounding_value))
                + r"\approx" + str(round(c(), rounding_value))
            ).shift(np.array([0, 0.8, 0]))

        math_text_line_calculate = math_text_line_calculate_func()
        math_text_line_calculate.add_updater(lambda x: x.become(math_text_line_calculate_func()))

        def math_text_secant_line_func():
            return (MathTex(
                "y = " + str(round(m(), rounding_value))
                + "x + (" + str(round(c(), rounding_value)) + ")", color=YELLOW
            ).shift(np.array([0, 0.2, 0])))

        math_text_secant_line = math_text_secant_line_func()
        math_text_secant_line.add_updater(lambda x: x.become(math_text_secant_line_func()))

        def secant_line_calculated_func():
            return plane.plot(secant_line_func, color=YELLOW, x_range=[-1, 13])

        secant_line_calculated = secant_line_calculated_func()
        secant_line_calculated.add_updater(lambda x: x.become(secant_line_calculated_func()))

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.add(func_x_intersection_1_line)
        self.play(
            Create(graph),
            Write(graph_func_label),
            Create(dot_a),
            Create(dot_b),
        )
        self.play(
            Write(math_text_h),
            Write(math_text_m),
            Write(math_text_line),
            Write(math_text_line_calculate),
        )
        self.play(
            Write(math_text_secant_line)
        )
        self.play(
            Create(secant_line_calculated)
        )
        self.play(
            point_a_x_tracker.animate.set_value(ending_point),
            point_b_x_tracker.animate.set_value(ending_point + end_h_value),
            run_time=10, rate_func=lingering)
        self.wait(5)
