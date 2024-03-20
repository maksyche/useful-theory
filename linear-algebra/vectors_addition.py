#!/usr/bin/env python3
from manim import *  # 0.18.0


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
        # plane.get_axis(0).set(color=BLUE)
        # plane.get_axis(1).set(color=BLUE)
        axes_labels = plane.get_axis_labels()

        self.add(plane, axes_labels)

        # The scene itself
        vector_a_coords = np.array([2.5, 0.5, 0])
        vector_a = plane.get_vector(np.array(vector_a_coords), color=RED)
        vector_a_label = MathTex("\\vec{a}", color=RED).next_to(vector_a, direction=UP, buff=-0.3)
        vector_a_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " \\\\ " + str(vector_a_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_a.get_end(), direction=RIGHT, buff=0.2))
        vector_b_coords = np.array([1.5, 2, 0])
        vector_b = plane.get_vector(np.array(vector_b_coords), color=BLUE)
        vector_b_label = MathTex("\\vec{b}", color=BLUE).next_to(vector_b, direction=RIGHT, buff=-1.1)
        vector_b_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_b_coords[0]) + " \\\\ " + str(vector_b_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_b.get_end(), direction=RIGHT, buff=0.2))
        vector_b_group = VGroup(vector_b, vector_b_label)
        vector_c_coords = np.add(vector_a_coords, vector_b_coords)
        vector_c = plane.get_vector(np.array(vector_c_coords), color=YELLOW)
        vector_c_label = MathTex("\\vec{c}", color=YELLOW).next_to(vector_c, direction=UP, buff=-2.2)
        vector_c_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_c_coords[0]) + " \\\\ " + str(vector_c_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_c.get_end(), direction=RIGHT, buff=0.2))
        math_text_vector_addition = MathTex("\\vec{c} = \\vec{a} + \\vec{b}")
        math_text_vector_addition_calc = MathTex(
            "\\vec{c} = "
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " \\\\ "
            + str(vector_a_coords[1]) + " \\end{bmatrix} + "
            "\\begin{bmatrix}" + str(vector_b_coords[0]) + " \\\\ "
            + str(vector_b_coords[1]) + " \\end{bmatrix} = "
            "\\begin{bmatrix}" + str(vector_c_coords[0]) + " \\\\ "
            + str(vector_c_coords[1]) + " \\end{bmatrix}"
        )
        (VGroup(math_text_vector_addition, math_text_vector_addition_calc)
         .arrange(DOWN).next_to(vector_c, direction=UP, buff=-0.5))

        self.play(Create(vector_a), Create(vector_b), Write(vector_a_label), Write(vector_b_label),
                  Write(vector_a_coord_label), Write(vector_b_coord_label))
        self.play(FadeOut(vector_a_coord_label), FadeOut(vector_b_coord_label))
        self.play(vector_b_group.animate.shift(vector_a.get_vector()))
        self.play(Create(vector_c), Write(vector_c_label), Write(vector_c_coord_label))
        self.play(Write(math_text_vector_addition))
        self.play(Write(math_text_vector_addition_calc))
        self.wait(3)
