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
            # 12.8/7.2
            # 9.6/5.4
            # 6.4/3.6
            # 3.2/1.8
            # 1.6/0.9
            x_range=(-2.8, 10),
            y_range=(-2.2, 5),
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
        vector_a_coords = np.array([2, 1, 0])
        vector_a = plane.get_vector(np.array(vector_a_coords), color=YELLOW)
        vector_a_label = MathTex("\\vec{a}", color=YELLOW).next_to(vector_a, direction=UP, buff=-0.25)
        vector_a_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " \\\\ " + str(vector_a_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_a.get_end(), direction=RIGHT, buff=0.2))

        vector_minus_squish_coords = np.multiply(vector_a_coords, -0.8)
        vector_minus_squish = plane.get_vector(np.array(vector_minus_squish_coords), color=BLUE)
        vector_minus_squish_label = MathTex("-0.8\\vec{a}", color=BLUE).next_to(vector_minus_squish, direction=DOWN, buff=0)
        vector_minus_squish_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_minus_squish_coords[0]) + " \\\\ "
            + str(vector_minus_squish_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_minus_squish.get_end(), direction=LEFT, buff=0.2))

        vector_stretch_coords = np.multiply(vector_a_coords, 2.5)
        vector_stretch = plane.get_vector(np.array(vector_stretch_coords), color=RED)
        vector_stretch_label = MathTex("2.5\\vec{a}", color=RED).next_to(vector_stretch, direction=UP, buff=-0.9)
        vector_stretch_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_stretch_coords[0]) + " \\\\ " + str(vector_stretch_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_stretch.get_end(), direction=RIGHT, buff=0.2))

        math_text_vector_mult_minus_squish_calc = MathTex(
            "-0.8\\vec{a} = \\vec{a} * -0.8 = "
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " * -0.8 \\\\ "
            + str(vector_a_coords[1]) + " * -0.8 \\end{bmatrix} = "
                                        "\\begin{bmatrix}" + str(vector_minus_squish_coords[0]) + " \\\\ "
            + str(vector_minus_squish_coords[1]) + " \\end{bmatrix}"
        ).next_to(plane, direction=UP, buff=-1.5)
        math_text_vector_mult_2_5_calc = MathTex(
            "2.5\\vec{a} = \\vec{a} * 2.5 = "
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " * 2.5 \\\\ "
            + str(vector_a_coords[1]) + " * 2.5 \\end{bmatrix} = "
                                        "\\begin{bmatrix}" + str(vector_stretch_coords[0]) + " \\\\ "
            + str(vector_stretch_coords[1]) + " \\end{bmatrix}"
        ).next_to(plane, direction=UP, buff=-1.5)

        self.play(Create(vector_a), Write(vector_a_label), Write(vector_a_coord_label))
        self.wait()
        self.play(Create(vector_minus_squish), Write(vector_minus_squish_label), Write(vector_minus_squish_coord_label))
        self.play(FadeOut(vector_a_coord_label), FadeOut(vector_a_label))
        self.play(FadeOut(vector_a), Create(vector_stretch), Write(vector_stretch_label),
                  Write(vector_stretch_coord_label))
        self.play(Write(math_text_vector_mult_minus_squish_calc))
        self.wait(5)
        self.play(FadeOut(math_text_vector_mult_minus_squish_calc))
        self.play(Write(math_text_vector_mult_2_5_calc))
        self.wait(5)
