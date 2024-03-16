#!/usr/bin/env python3
from manim import *  # 0.18.0


class MyScene(Scene):
    def construct(self):
        plane = NumberPlane(
            # X/Y ration should always be 16/9, but with some space after the last tick:
            # 17.6/9.9
            # 12.8/7.2
            # 6.4/3.6
            # 3.2/1.8
            # 1.6/0.9
            x_range=(-5.4, 7.4),
            y_range=(-1.6, 5.6),

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
        vector_coords = [4.5, 3]
        vector = plane.get_vector(np.array(vector_coords), color=BLUE)
        vector_coord_label = (
            MathTex("\\begin{bmatrix}" + str(vector_coords[0]) + " \\\\ " + str(vector_coords[1]) + " \\end{bmatrix}",
                    color=BLUE).next_to(vector.get_end(), direction=RIGHT, buff=0.2))
        vector_label = MathTex("\\vec{a}", color=BLUE).next_to(vector, direction=UP, buff=-0.95)
        vector_horizontal_line = plane.get_horizontal_line(np.array([vector.get_end()[0], vector.get_start()[1], 0]),
                                                           color=YELLOW)
        vector_horizontal_line_label = MathTex("a", color=YELLOW).next_to(vector_horizontal_line, direction=UP,
                                                                          buff=0.3)
        vector_vertical_line = plane.get_vertical_line(vector.get_end(), color=YELLOW)
        vector_vertical_line_label = MathTex("b", color=YELLOW).next_to(vector_vertical_line, direction=RIGHT, buff=0.2)
        unit_vector = plane.get_vector(vector_coords / vector.get_length(), color=RED)
        unit_vector_label = MathTex("\\hat{a}", color=RED).next_to(unit_vector, direction=UP, buff=0)
        math_text_length = MathTex("||\\vec{a}||=\\sqrt{a^2 + b^2}", color=YELLOW)
        math_text_unit = MathTex("\\hat{a}=\\frac{\\vec{a}}{||\\vec{a}||}", color=RED)
        VGroup(math_text_length, math_text_unit).arrange(DOWN).next_to(plane, direction=UL, buff=-4.5)
        self.play(Create(vector), Write(vector_label))
        self.play(Write(vector_coord_label))
        self.play(Create(vector_horizontal_line), Write(vector_horizontal_line_label))
        self.play(Create(vector_vertical_line), Write(vector_vertical_line_label))
        self.play(Write(math_text_length))
        self.play(Write(math_text_unit))
        self.play(Create(unit_vector))
        self.play(Write(unit_vector_label))
        self.wait(3)
