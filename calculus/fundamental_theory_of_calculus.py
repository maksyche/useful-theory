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
            x_range=(-0.2, 6.2),
            y_range=(-0.2, 3.4),
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
        start_range = 0
        end_range = 6

        def func(x):
            return x - 1 / 6 * np.power(x, 2)

        def decimal_range(start, stop, increment):
            while start < stop:
                yield start
                start += increment

        def calculate_area(dx):
            area = 0
            for i in decimal_range(start_range, end_range, dx):
                area += dx * func(i + dx / 2)  # Centered rectangle
            return area

        def antider(x):
            return 1 / 2 * np.power(x, 2) - 1 / 18 * np.power(x, 3)

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        graph_func = plane.plot(func, color=YELLOW, x_range=[start_range, end_range])

        graph_label = (MathTex(r"f(x) = x - \frac{x^2}{6} \quad F(x) = \frac{x^2}{2} - \frac{x^3}{18}",
                               color=WHITE))
        graph_label[0][0:11].set_color(YELLOW)
        s_exact_label = (
            MathTex(r"S = \int_{" + str(start_range) + "}^{" + str(end_range) + "} f(x)dx = F("
                    + str(end_range) + ") - F(" + str(start_range) + ") = "
                    + str(antider(end_range) - antider(start_range)),
                    color=WHITE))
        s_exact_label[0][0:1].set_color(BLUE)

        (VGroup(graph_label, s_exact_label)
         .arrange(DOWN)
         .shift(np.array([-2.5, 2, 0])))

        def generate_rectangles(dx):
            return plane.get_riemann_rectangles(
                graph_func,
                x_range=[start_range, end_range],
                stroke_width=0.1,
                dx=dx,
                input_sample_type="center",
            )

        rectangles_1_dx = end_range - start_range
        rectangles_1 = generate_rectangles(rectangles_1_dx)
        rectangles_3_dx = (end_range - start_range) / 3
        rectangles_3 = generate_rectangles(rectangles_3_dx)
        rectangles_6_dx = (end_range - start_range) / 6
        rectangles_6 = generate_rectangles(rectangles_6_dx)
        rectangles_60_dx = (end_range - start_range) / 60
        rectangles_60 = generate_rectangles(rectangles_60_dx)
        rectangles_120_dx = (end_range - start_range) / 120
        rectangles_120 = generate_rectangles(rectangles_120_dx)
        rectangles_600_dx = (end_range - start_range) / 600
        rectangles_600 = generate_rectangles(rectangles_600_dx)

        def generate_nor_text(number_of_rectangles):
            return (MathTex(r"\text{Number of rectangles:}\enspace" + str(number_of_rectangles),
                            color=WHITE)).next_to(graph_label, direction=RIGHT, aligned_edge=LEFT, buff=4.2)

        def generate_s_approx_text(dx):
            s_approx_text = (MathTex(r"S \approx " + str(round(calculate_area(dx), 6)),
                                     color=WHITE)).shift(np.array([3.7, 1.45, 0]))
            s_approx_text[0][0:1].set_color(BLUE)
            return s_approx_text

        number_of_rectangles_1_label = generate_nor_text(1)
        s_approx_rectangles_1_label = (MathTex(r"S \approx "
                                               + str(rectangles_1_dx)
                                               + "*" + str(round(func((end_range - start_range) / 2), 3))
                                               + r"\approx" + str(round(calculate_area(rectangles_1_dx), 3)),
                                               color=WHITE)).shift(np.array([3.7, 1.45, 0]))
        s_approx_rectangles_1_label[0][0:1].set_color(BLUE)
        s_approx_rectangles_1_width_brace = Brace(rectangles_1, sharpness=0.1, direction=UP, buff=-3)
        s_approx_rectangles_1_width_label = (MathTex(str(rectangles_1_dx) + r"\enspace\text{s}")
                                             .next_to(s_approx_rectangles_1_width_brace,
                                                      direction=UP))
        s_approx_rectangles_1_height_brace = Brace(rectangles_1, sharpness=0.1, direction=LEFT, buff=-12)
        s_approx_rectangles_1_height_label = (MathTex(str(func((end_range - start_range) / 2))
                                                      + r"\enspace\text{m/s}")
                                              .next_to(s_approx_rectangles_1_height_brace, direction=LEFT))

        number_of_rectangles_3_label = generate_nor_text(3)
        s_approx_rectangles_3_label = generate_s_approx_text(rectangles_3_dx)
        number_of_rectangles_6_label = generate_nor_text(6)
        s_approx_rectangles_6_label = generate_s_approx_text(rectangles_6_dx)
        number_of_rectangles_60_label = generate_nor_text(60)
        s_approx_rectangles_60_label = generate_s_approx_text(rectangles_60_dx)
        number_of_rectangles_120_label = generate_nor_text(120)
        s_approx_rectangles_120_label = generate_s_approx_text(rectangles_120_dx)
        number_of_rectangles_600_label = generate_nor_text(600)
        s_approx_rectangles_600_label = generate_s_approx_text(rectangles_600_dx)

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.add(graph_func, graph_label, s_exact_label)
        self.play(
            Write(number_of_rectangles_1_label),
            Write(s_approx_rectangles_1_label),
        )
        self.play(
            Write(rectangles_1),
        )
        self.play(
            Write(s_approx_rectangles_1_width_label),
            Write(s_approx_rectangles_1_height_label),
            Create(s_approx_rectangles_1_width_brace),
            Create(s_approx_rectangles_1_height_brace),
        )
        self.wait(3)
        self.play(
            Unwrite(s_approx_rectangles_1_width_label),
            Unwrite(s_approx_rectangles_1_height_label),
            Uncreate(s_approx_rectangles_1_width_brace),
            Uncreate(s_approx_rectangles_1_height_brace),
        )
        self.play(
            ReplacementTransform(rectangles_1, rectangles_3),
            TransformMatchingShapes(number_of_rectangles_1_label, number_of_rectangles_3_label),
            ReplacementTransform(s_approx_rectangles_1_label, s_approx_rectangles_3_label)
        )
        self.wait()
        self.play(
            ReplacementTransform(rectangles_3, rectangles_6),
            TransformMatchingShapes(number_of_rectangles_3_label, number_of_rectangles_6_label),
            ReplacementTransform(s_approx_rectangles_3_label, s_approx_rectangles_6_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(rectangles_6, rectangles_60),
            TransformMatchingShapes(number_of_rectangles_6_label, number_of_rectangles_60_label),
            ReplacementTransform(s_approx_rectangles_6_label, s_approx_rectangles_60_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(rectangles_60, rectangles_120),
            TransformMatchingShapes(number_of_rectangles_60_label, number_of_rectangles_120_label),
            ReplacementTransform(s_approx_rectangles_60_label, s_approx_rectangles_120_label),
        )
        self.wait()
        self.play(
            ReplacementTransform(rectangles_120, rectangles_600),
            TransformMatchingShapes(number_of_rectangles_120_label, number_of_rectangles_600_label),
            ReplacementTransform(s_approx_rectangles_120_label, s_approx_rectangles_600_label),
        )
        self.wait(3)
