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
            y_range=(-0.6, 6.6),
            x_length=12.8,
            y_length=7.2,

            x_axis_config={
                "include_numbers": False,
                "include_ticks": False,
            },
            y_axis_config={
                "numbers_to_exclude": [],
                "stroke_width": 0,
                "include_numbers": False,
                "include_ticks": False,
            },
            background_line_style={
                "stroke_opacity": 0,  # Removes grid
            }
        )

        # Axes labels config
        # plane.get_axis(0).set(color=BLUE)
        # plane.get_axis(1).set(color=BLUE)
        axes_labels = plane.get_axis_labels()

        self.add(plane, axes_labels[:1])

        # The scene itself
        vector_f_coords = np.array([2, 3, 0])
        vector_f = plane.get_vector(np.array(vector_f_coords), color=RED)
        vector_f_label = MathTex("\\vec{F}", color=RED).next_to(vector_f, direction=UP, buff=-0.7)

        vector_s_coords = np.array([3, 0, 0])
        vector_s = plane.get_vector(np.array(vector_s_coords), color=BLUE)
        vector_s_label = (MathTex("\\vec{s}", color=BLUE)
                          .next_to(vector_s, direction=UP, buff=0.1)
                          .shift(np.array([0.5, 0, 0])))

        angle = Angle(vector_s, vector_f, radius=1, color=YELLOW)
        angle_label = (MathTex("\\theta", color=YELLOW)
                       .next_to(angle, direction=RIGHT, buff=0.1)
                       .shift(np.array([-0.1, 0.15, 0])))

        rectangle = Rectangle(height=0.5, width=1).move_to(plane.get_origin())

        math_text = MathTex("W = |\\vec{F}| * |\\vec{s}| * \\cos\\theta").next_to(plane, direction=UP, buff=-1)

        group = VGroup(vector_f, vector_f_label, vector_s, vector_s_label, rectangle, angle, angle_label)
        group.shift(np.array([0, 0.3, 0])).shift(np.array([-1.5, 0, 0]))
        group.remove(vector_s, angle, angle_label)

        self.add(vector_f, vector_s, rectangle, angle)
        self.play(Write(vector_f_label), Write(vector_s_label), Write(angle_label), Write(math_text))
        self.wait()
        self.play(
            group.animate.shift(np.array([3, 0, 0])),
            vector_s.animate.scale(0.00001, about_point=vector_s.get_end()),
            FadeOut(angle, run_time=0.2),
            FadeOut(angle_label, run_time=0.2),
            FadeOut(vector_s_label, run_time=0.2),
        )
        self.wait(0.5)
