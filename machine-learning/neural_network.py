#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(Scene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        l1_circle1 = Circle(radius=0.5, color=WHITE).shift(np.array((-4, 3, 0)))
        l1_circle1_text = MathTex(r"x_1").move_to(l1_circle1.get_center())
        l1_circle2 = Circle(radius=0.5, color=WHITE).shift(np.array((-4, 1, 0)))
        l1_circle2_text = MathTex(r"x_2").move_to(l1_circle2.get_center())
        l1_circle3 = Circle(radius=0.5, color=WHITE).shift(np.array((-4, -3, 0)))
        l1_circle3_text = MathTex(r"x_{n^{(I)}}").move_to(l1_circle3.get_center())
        l2_circle1 = Circle(radius=0.5, color=WHITE).shift(np.array((0, 1.5, 0)))
        l2_circle1_text = MathTex(r"a_1^{(H)}").move_to(l2_circle1.get_center())
        l2_circle2 = Circle(radius=0.5, color=WHITE).shift(np.array((0, -1.5, 0)))
        l2_circle2_text = MathTex(r"a_{n^{(H)}}^{(H)}").move_to(l2_circle2.get_center())
        l3_circle = Circle(radius=0.5, color=WHITE).shift(np.array((4, 0, 0)))
        l3_circle_text = MathTex(r"a^{(O)}").move_to(l3_circle.get_center())
        l1_dot1 = Dot().shift(np.array(center_of_mass([l1_circle2.get_center(), l1_circle3.get_center()])))
        l1_dot2 = Dot().move_to(l1_dot1.get_center()).shift(np.array((0, 0.7, 0)))
        l1_dot3 = Dot().move_to(l1_dot1.get_center()).shift(np.array((0, -0.7, 0)))
        l2_dot1 = Dot().shift(np.array(center_of_mass([l2_circle1.get_center(), l2_circle2.get_center()])))
        l2_dot2 = Dot().move_to(l2_dot1.get_center()).shift(np.array((0, 0.5, 0)))
        l2_dot3 = Dot().move_to(l2_dot1.get_center()).shift(np.array((0, -0.5, 0)))

        def generate_line_between_circles(circle1, circle2):
            line = Line(start=circle1.get_center(), end=circle2.get_center())
            line.set_length(line.get_length() - 1.0)
            return line

        def generate_line_label(line, label):
            return MathTex(label).move_to(line.get_center()).rotate(angle=line.get_angle()).shift(np.array((0, 0.4, 0)))

        l1_circle1_l2_circle1_line = generate_line_between_circles(l1_circle1, l2_circle1)
        l1_circle1_l2_circle1_line_label = generate_line_label(l1_circle1_l2_circle1_line, r"w_{1,1}^{(H)}")
        l1_circle1_l2_circle2_line = generate_line_between_circles(l1_circle1, l2_circle2)
        l1_circle1_l2_circle2_line_label = (generate_line_label(l1_circle1_l2_circle2_line, r"w_{n^{(H)},1}^{(H)}")
                                            .shift(np.array((0.5, -0.4, 0))))
        l1_circle2_l2_circle1_line = generate_line_between_circles(l1_circle2, l2_circle1)
        l1_circle2_l2_circle1_line_label = generate_line_label(l1_circle2_l2_circle1_line, r"w_{1,2}^{(H)}")
        l1_circle2_l2_circle2_line = generate_line_between_circles(l1_circle2, l2_circle2)
        l1_circle2_l2_circle2_line_label = (generate_line_label(l1_circle2_l2_circle2_line, r"w_{n^{(H)},2}^{(H)}")
                                            .shift(np.array((-0.3, 0.2, 0))))
        l1_circle3_l2_circle1_line = generate_line_between_circles(l1_circle3, l2_circle1)
        l1_circle3_l2_circle1_line_label = (generate_line_label(l1_circle3_l2_circle1_line, r"w_{1,n^{(I)}}^{(H)}")
                                            .shift(np.array((-0.9, -0.8, 0))))
        l1_circle3_l2_circle2_line = generate_line_between_circles(l1_circle3, l2_circle2)
        l1_circle3_l2_circle2_line_label = generate_line_label(l1_circle3_l2_circle2_line,
                                                               r"w_{n^{(H)},n^{(I)}}^{(H)}")
        l2_circle1_l3_circle_line = generate_line_between_circles(l2_circle1, l3_circle)
        l2_circle1_l3_circle_line_label = generate_line_label(l2_circle1_l3_circle_line, r"w_{1}^{(O)}")
        l2_circle2_l3_circle_line = generate_line_between_circles(l2_circle2, l3_circle)
        l2_circle2_l3_circle_line_label = generate_line_label(l2_circle2_l3_circle_line, r"w_{n^{(H)}}^{(O)}")

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        # TODO: Neuron pulse animation???
        self.add(l1_circle1, l1_circle1_text, l1_circle2, l1_circle2_text, l1_circle3, l1_circle3_text, l2_circle1,
                 l2_circle1_text, l2_circle2, l2_circle2_text, l3_circle, l3_circle_text, l1_circle1_l2_circle1_line,
                 l1_circle1_l2_circle1_line_label, l1_circle1_l2_circle2_line, l1_circle1_l2_circle2_line_label,
                 l1_circle2_l2_circle1_line, l1_circle2_l2_circle1_line_label, l1_circle2_l2_circle2_line,
                 l1_circle2_l2_circle2_line_label, l1_circle3_l2_circle1_line, l1_circle3_l2_circle1_line_label,
                 l1_circle3_l2_circle2_line, l1_circle3_l2_circle2_line_label, l2_circle1_l3_circle_line,
                 l2_circle1_l3_circle_line_label, l2_circle2_l3_circle_line, l2_circle2_l3_circle_line_label,
                 l1_dot1, l1_dot2, l1_dot3, l2_dot1, l2_dot2, l2_dot3)
        self.wait()
