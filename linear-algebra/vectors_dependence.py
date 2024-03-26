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
        # plane.get_axis(0).set(color=BLUE)
        # plane.get_axis(1).set(color=BLUE)
        axes_labels = plane.get_axis_labels()

        self.add(plane, axes_labels)

        # The scene itself
        vector_a_coords = np.array([2, 2])
        vector_a = plane.get_vector(np.array(vector_a_coords), color=RED)
        vector_a_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " \\\\ " + str(vector_a_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_a.get_end(), direction=RIGHT, buff=0.2))
        vector_a_label = MathTex("\\vec{a}", color=RED).next_to(vector_a, direction=UP, buff=-0.7)

        vector_b_coords = np.multiply(vector_a_coords, -0.75)
        vector_b = Vector(np.array(vector_b_coords), color=BLUE)
        vector_b_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_b_coords[0]) + " \\\\ " + str(vector_b_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_b.get_end(), direction=LEFT, buff=0.2))
        vector_b_label = MathTex("\\vec{b}", color=BLUE).next_to(vector_b, direction=DOWN, buff=-0.4)

        vector_c_coords = np.array([5, -2])
        vector_c = Vector(np.array(vector_c_coords), color=YELLOW)
        vector_c_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_c_coords[0]) + " \\\\ " + str(vector_c_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_c.get_end(), direction=RIGHT, buff=0.2))
        vector_c_label = MathTex("\\vec{c}", color=YELLOW).next_to(vector_c, direction=DOWN, buff=-0.7)

        math_text_dependent = MathTex("\\vec{a},\\vec{b}\\text{ are linearly dependent}")
        math_text_independent = MathTex("\\vec{a},\\vec{c}\\text{ are linearly independent}")
        (VGroup(math_text_dependent, math_text_independent)
         .arrange(DOWN).next_to(vector_a, direction=LEFT, buff=0.5))

        self.play(Create(vector_a), Create(vector_b), Create(vector_c))
        self.play(Write(vector_a_label), Write(vector_a_coord_label),
                  Write(vector_b_label), Write(vector_b_coord_label),
                  Write(vector_c_label), Write(vector_c_coord_label))
        self.play(Write(math_text_dependent), Write(math_text_independent))
        self.wait(5)
