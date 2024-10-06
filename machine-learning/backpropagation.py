#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(Scene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        l1_circle1 = Circle(radius=0.5, color=WHITE).shift(np.array((-6, 3, 0)))
        l1_circle1_text = MathTex(r"x_1").move_to(l1_circle1.get_center())
        l1_circle2 = Circle(radius=0.5, color=WHITE).shift(np.array((-6, 1, 0)))
        l1_circle2_text = MathTex(r"x_2").move_to(l1_circle2.get_center())
        l1_circle3 = Circle(radius=0.5, color=WHITE).shift(np.array((-6, -3, 0)))
        l1_circle3_text = MathTex(r"x_{n^{(I)}}").move_to(l1_circle3.get_center())
        l2_circle1 = Circle(radius=0.5, color=WHITE).shift(np.array((-2, 1.5, 0)))
        l2_circle1_text = MathTex(r"z_1^{(H)}").move_to(l2_circle1.get_center())
        l2_b1_text = MathTex(r"b_1^{(H)}").shift(np.array((-2, 3, 0)))
        l2_circle2 = Circle(radius=0.5, color=WHITE).shift(np.array((-2, -1.5, 0)))
        l2_circle2_text = MathTex(r"z_{n^{(H)}}^{(H)}").move_to(l2_circle2.get_center())
        l2_b2_text = MathTex(r"b_{n^{(H)}}^{(H)}").shift(np.array((-2, -3, 0)))
        l2_circle1_additional = Circle(radius=0.5, color=WHITE).shift(np.array((-0.5, 1.5, 0)))
        l2_circle1_additional_text = MathTex(r"a_1^{(H)}").move_to(l2_circle1_additional.get_center())
        l2_circle2_additional = Circle(radius=0.5, color=WHITE).shift(np.array((-0.5, -1.5, 0)))
        l2_circle2_additional_text = MathTex(r"a_1^{(H)}").move_to(l2_circle2_additional.get_center())
        l3_circle = Circle(radius=0.5, color=WHITE).shift(np.array((3, 0, 0)))
        l3_circle_text = MathTex(r"z^{(O)}").move_to(l3_circle.get_center())
        l3_b_text = MathTex(r"b^{(O)}").shift(np.array((3, 1.5, 0)))
        l3_circle_additional = Circle(radius=0.5, color=WHITE).shift(np.array((4.5, 0, 0)))
        l3_circle_additional_text = MathTex(r"a^{(O)}").move_to(l3_circle_additional.get_center())
        ek_text = MathTex(r"E_k").shift(np.array((6, 0, 0)))
        yhat_text = MathTex(r"\hat{y}").shift(np.array((6, 1.5, 0)))
        l1_dot1 = Dot().shift(np.array(center_of_mass([l1_circle2.get_center(), l1_circle3.get_center()])))
        l1_dot2 = Dot().move_to(l1_dot1.get_center()).shift(np.array((0, 0.7, 0)))
        l1_dot3 = Dot().move_to(l1_dot1.get_center()).shift(np.array((0, -0.7, 0)))
        l2_dot1 = Dot().shift(np.array(center_of_mass([l2_circle1.get_center(), l2_circle2.get_center()])))
        l2_dot2 = Dot().move_to(l2_dot1.get_center()).shift(np.array((0, 0.5, 0)))
        l2_dot3 = Dot().move_to(l2_dot1.get_center()).shift(np.array((0, -0.5, 0)))
        l2_dot1_additional = Dot().shift(np.array(center_of_mass(
            [l2_circle1_additional.get_center(), l2_circle2_additional.get_center()])))
        l2_dot2_additional = Dot().move_to(l2_dot1_additional.get_center()).shift(np.array((0, 0.5, 0)))
        l2_dot3_additional = Dot().move_to(l2_dot1_additional.get_center()).shift(np.array((0, -0.5, 0)))

        def generate_line_between_objects(circle1, circle2):
            line = Line(start=circle1.get_center(), end=circle2.get_center())
            line.set_length(line.get_length() - 1.0)
            return line

        def generate_line_label(line, label):
            return MathTex(label).move_to(line.get_center()).rotate(angle=line.get_angle()).shift(np.array((0, 0.4, 0)))

        l1_circle1_l2_circle1_line = generate_line_between_objects(l1_circle1, l2_circle1)
        l1_circle1_l2_circle1_line_label = generate_line_label(l1_circle1_l2_circle1_line, r"w_{1,1}^{(H)}")
        l1_circle1_l2_circle2_line = generate_line_between_objects(l1_circle1, l2_circle2)
        l1_circle1_l2_circle2_line_label = (generate_line_label(l1_circle1_l2_circle2_line, r"w_{n^{(H)},1}^{(H)}")
                                            .shift(np.array((0.5, -0.4, 0))))
        l1_circle2_l2_circle1_line = generate_line_between_objects(l1_circle2, l2_circle1)
        l1_circle2_l2_circle1_line_label = generate_line_label(l1_circle2_l2_circle1_line, r"w_{1,2}^{(H)}")
        l1_circle2_l2_circle2_line = generate_line_between_objects(l1_circle2, l2_circle2)
        l1_circle2_l2_circle2_line_label = (generate_line_label(l1_circle2_l2_circle2_line, r"w_{n^{(H)},2}^{(H)}")
                                            .shift(np.array((-0.3, 0.2, 0))))
        l1_circle3_l2_circle1_line = generate_line_between_objects(l1_circle3, l2_circle1)
        l1_circle3_l2_circle1_line_label = (generate_line_label(l1_circle3_l2_circle1_line, r"w_{1,n^{(I)}}^{(H)}")
                                            .shift(np.array((-0.9, -0.8, 0))))
        l1_circle3_l2_circle2_line = generate_line_between_objects(l1_circle3, l2_circle2)
        l1_circle3_l2_circle2_line_label = generate_line_label(l1_circle3_l2_circle2_line,
                                                               r"w_{n^{(H)},n^{(I)}}^{(H)}")
        l2_b1_line = generate_line_between_objects(l2_circle1, l2_b1_text)
        l2_b2_line = generate_line_between_objects(l2_circle2, l2_b2_text)
        l2_circle1_additional_line = generate_line_between_objects(l2_circle1, l2_circle1_additional)
        l2_circle2_additional_line = generate_line_between_objects(l2_circle2, l2_circle2_additional)
        l2_circle1_additional_l3_circle_line = generate_line_between_objects(l2_circle1_additional, l3_circle)
        l2_circle1_additional_l3_circle_line_label = generate_line_label(l2_circle1_additional_l3_circle_line,
                                                                         r"w_{1}^{(O)}")
        l2_circle2_additional_l3_circle_line = generate_line_between_objects(l2_circle2_additional, l3_circle)
        l2_circle2_additional_l3_circle_line_label = generate_line_label(l2_circle2_additional_l3_circle_line,
                                                                         r"w_{n^{(H)}}^{(O)}")
        l3_b_line = generate_line_between_objects(l3_circle, l3_b_text)
        l3_circle_additional_line = generate_line_between_objects(l3_circle, l3_circle_additional)
        ek_line = generate_line_between_objects(l3_circle_additional, ek_text)
        yhat_line = generate_line_between_objects(ek_text, yhat_text)

        math_text = (MathTex(r"\frac{\partial E_{k}}{\partial w_{1,2}^{(H)}} = "
                             r"\frac{\partial z_{1}^{(H)}}{\partial w_{1,2}^{(H)}} "
                             r"\cdot \frac{\partial a_{1}^{(H)}}{\partial z_{1}^{(H)}}"
                             r"\cdot \frac{\partial z^{(O)}}{\partial a_{1}^{(H)}}"
                             r"\cdot \frac{\partial a^{(O)}}{\partial z^{(O)}}"
                             r"\cdot \frac{\partial E_{k}}{\partial a^{(O)}}", color=RED)
                     .shift(np.array((-1, -3, 0)))
                     .align_to(np.array((-1, -3, 0)), direction=LEFT))
        math_text[0][13:].set_color(ManimColor("#0e1116")),

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.add(l1_circle1, l1_circle1_text, l1_circle2, l1_circle2_text, l1_circle3, l1_circle3_text, l2_circle1,
                 l2_circle1_text, l2_b1_text, l2_b1_line, l2_circle2, l2_circle2_text, l2_b2_text, l2_b2_line,
                 l2_circle1_additional, l2_circle1_additional_text, l2_circle2_additional, l2_circle2_additional_text,
                 l2_circle1_additional_line, l2_circle2_additional_line, l3_circle, l3_circle_text, l3_b_text,
                 l3_b_line, l1_circle1_l2_circle1_line, l1_circle1_l2_circle1_line_label, l1_circle1_l2_circle2_line,
                 l1_circle1_l2_circle2_line_label, l1_circle2_l2_circle1_line, l1_circle2_l2_circle1_line_label,
                 l1_circle2_l2_circle2_line, l1_circle2_l2_circle2_line_label, l1_circle3_l2_circle1_line,
                 l1_circle3_l2_circle1_line_label, l1_circle3_l2_circle2_line, l1_circle3_l2_circle2_line_label,
                 l2_circle1_additional_l3_circle_line, l2_circle1_additional_l3_circle_line_label,
                 l2_circle2_additional_l3_circle_line, l2_circle2_additional_l3_circle_line_label, l3_circle_additional,
                 l3_circle_additional_text, l3_circle_additional_line, ek_text, ek_line, yhat_text, yhat_line, l1_dot1,
                 l1_dot2, l1_dot3, l2_dot1, l2_dot2, l2_dot3, l2_dot1_additional, l2_dot2_additional,
                 l2_dot3_additional)

        self.wait()
        self.play(
            Write(math_text),
            l1_circle2_l2_circle1_line_label.animate.set_color(RED),
            l1_circle2_l2_circle1_line.animate.set_color(RED),
        )
        self.wait(3)
        self.play(
            math_text[0][:29].animate.set_color(RED),
            l2_circle1.animate.set_color(RED),
            l2_circle1_text.animate.set_color(RED)
        )
        self.wait(3)
        self.play(
            math_text[0][:43].animate.set_color(RED),
            l2_circle1_additional_line.animate.set_color(RED),
            l2_circle1_additional.animate.set_color(RED),
            l2_circle1_additional_text.animate.set_color(RED)
        )
        self.wait(3)
        self.play(
            math_text[0][:56].animate.set_color(RED),
            l2_circle1_additional_l3_circle_line.animate.set_color(RED),
            l3_circle.animate.set_color(RED),
            l3_circle_text.animate.set_color(RED)
        )
        self.wait(3)
        self.play(
            math_text[0][:68].animate.set_color(RED),
            l3_circle_additional_line.animate.set_color(RED),
            l3_circle_additional.animate.set_color(RED),
            l3_circle_additional_text.animate.set_color(RED)
        )
        self.wait(3)
        self.play(
            math_text[0][:].animate.set_color(RED),
            ek_line.animate.set_color(RED),
            ek_text.animate.set_color(RED)
        )
        self.wait(5)
