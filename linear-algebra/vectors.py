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
        vector_a_coords = np.array([1.5, 2.5])
        vector_a = plane.get_vector(np.array(vector_a_coords), color=BLUE)
        vector_a_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_a_coords[0]) + " \\\\ " + str(vector_a_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_a.get_end(), direction=RIGHT, buff=0.2))
        vector_a_label = MathTex("\\vec{a}", color=BLUE).next_to(vector_a, direction=UP, buff=-0.8)
        vector_a_vertical_line = plane.get_vertical_line(vector_a.get_end(), color=YELLOW)
        vector_a_horizontal_line = plane.get_horizontal_line(vector_a.get_end(), color=YELLOW)
        self.play(Create(vector_a_vertical_line), Create(vector_a_horizontal_line))
        self.play(Create(vector_a))
        self.play(Write(vector_a_label))
        self.play(Write(vector_a_coord_label))
        self.wait(0.5)

        vector_b_coords = np.array([-4, -2])
        vector_b = plane.get_vector(np.array(vector_b_coords), color=RED)
        vector_b_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_b_coords[0]) + " \\\\ " + str(vector_b_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector_b.get_end(), direction=LEFT, buff=0.2))
        vector_b_label = MathTex("\\vec{b}", color=RED).next_to(vector_b, direction=DOWN, buff=-0.8)
        vector_b_vertical_line = plane.get_vertical_line(vector_b.get_end(), color=YELLOW)
        vector_b_horizontal_line = plane.get_horizontal_line(vector_b.get_end(), color=YELLOW)

        self.play(Create(vector_b_vertical_line), Create(vector_b_horizontal_line))
        self.play(Create(vector_b))
        self.play(Write(vector_b_label))
        self.play(Write(vector_b_coord_label))
        self.wait(3)
