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
            x_range=(-5.4, 7.4),
            y_range=(-1.6, 5.6),
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
        vector_coords = np.array([4.5, 3])
        vector = plane.get_vector(np.array(vector_coords), color=BLUE)
        vector_coord_label = (MathTex(
            "\\begin{bmatrix}" + str(vector_coords[0]) + " \\\\ " + str(vector_coords[1]) + " \\end{bmatrix}",
        ).next_to(vector.get_end(), direction=RIGHT, buff=0.2))
        vector_label = MathTex("\\vec{a}", color=BLUE).next_to(vector, direction=UP, buff=-1.1)
        vector_horizontal_line = plane.get_horizontal_line(
            np.array([vector.get_end()[0], vector.get_start()[1], 0]), color=YELLOW)
        vector_horizontal_line_label = (MathTex("x_{a}", color=YELLOW)
                                        .next_to(vector_horizontal_line, direction=UP, buff=0.3))
        vector_vertical_line = plane.get_vertical_line(vector.get_end(), color=YELLOW)
        vector_vertical_line_label = (MathTex("y_{a}", color=YELLOW)
                                      .next_to(vector_vertical_line, direction=RIGHT, buff=0.2))
        unit_vector_coords = vector_coords / vector.get_length()
        unit_vector = plane.get_vector(unit_vector_coords, color=RED)
        unit_vector_label = MathTex("\\hat{a}", color=RED).next_to(unit_vector, direction=UP, buff=0)
        math_text_length = MathTex("||\\vec{a}||=\\sqrt{x_{a}^2 + y_{a}^2}")
        math_text_length_calc = MathTex(
            "||\\vec{a}||=\\sqrt{" + str(vector_coords[0]) + "^2 + " + str(vector_coords[1]) + "^2} \\approx "
            + str(round(vector.get_length(), 2))
        )
        math_text_unit = MathTex(
            "\\hat{a} = \\frac{\\vec{a}}{||\\vec{a}||} \\approx "
            "\\begin{bmatrix}" + str(round(unit_vector_coords[0], 2)) + " \\\\ "
            + str(round(unit_vector_coords[1], 2)) + " \\end{bmatrix}",
        )
        (VGroup(math_text_length, math_text_length_calc, math_text_unit)
         .arrange(DOWN).next_to(plane, direction=UL, buff=-4.5))

        self.play(Create(vector), Write(vector_label))
        self.play(Write(vector_coord_label))
        self.play(Create(vector_horizontal_line), Write(vector_horizontal_line_label))
        self.play(Create(vector_vertical_line), Write(vector_vertical_line_label))
        self.play(Write(math_text_length))
        self.play(Write(math_text_length_calc))
        self.play(Write(math_text_unit))
        self.play(Create(unit_vector))
        self.play(Write(unit_vector_label))
        self.wait(3)
