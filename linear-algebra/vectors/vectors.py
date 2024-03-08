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
            x_range=(-6.4, 6.4),
            y_range=(-3.6, 3.6),

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

        vector_a = Vector(np.array([1.5, 2.5]), color=BLUE)
        vector_a_label = MathTex("\\vec{a}", color=BLUE).next_to(vector_a, direction=UP, buff=-0.8)
        vector_a_coord_label = vector_a.coordinate_label(integer_labels=False, color=BLUE)
        vector_a_vertical_line = DashedLine(np.array([vector_a.get_end()[0], 0, 0]), vector_a.get_end(),
                                            color=YELLOW, stroke_opacity=0.5)
        vector_a_horizontal_line = DashedLine(np.array([0, vector_a.get_end()[1], 0]), vector_a.get_end(),
                                              color=YELLOW, stroke_opacity=0.5)
        self.play(Create(vector_a_vertical_line), Create(vector_a_horizontal_line))
        self.play(Create(vector_a))
        self.play(Write(vector_a_label))
        self.play(Write(vector_a_coord_label))
        self.wait(0.5)

        vector_b = Vector(np.array([-4, -2]), color=RED)
        vector_b_label = MathTex("\\vec{b}", color=RED).next_to(vector_b, direction=DOWN, buff=-0.8)
        vector_b_coord_label = vector_b.coordinate_label(color=RED)
        vector_b_vertical_line = DashedLine(np.array([vector_b.get_end()[0], 0, 0]), vector_b.get_end(),
                                            color=YELLOW, stroke_opacity=0.5)
        vector_b_horizontal_line = DashedLine(np.array([0, vector_b.get_end()[1], 0]), vector_b.get_end(),
                                              color=YELLOW, stroke_opacity=0.5)
        self.play(Create(vector_b_vertical_line), Create(vector_b_horizontal_line))
        self.play(Create(vector_b))
        self.play(Write(vector_b_label))
        self.play(Write(vector_b_coord_label))
        self.wait(3)
