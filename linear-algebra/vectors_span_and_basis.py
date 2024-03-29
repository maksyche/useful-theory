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
            x_range=(-3.2, 3.2),
            y_range=(-1.8, 1.8),
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
        vector_i_coords = np.array([1, 0, 0])
        vector_i = plane.get_vector(np.array(vector_i_coords), color=RED)
        vector_i_label = MathTex(r"\hat{i}", color=RED).next_to(vector_i, direction=DOWN, buff=0.05)

        vector_j_coords = np.array([0, 1, 0])
        vector_j = plane.get_vector(np.array(vector_j_coords), color=BLUE)
        vector_j_label = MathTex(r"\hat{j}", color=BLUE).next_to(vector_j, direction=LEFT, buff=0.1)

        vector_v_coords = np.array([1.5, 0.5, 0])
        vector_v = plane.get_vector(np.array(vector_v_coords), color=YELLOW)
        vector_v_coords_label = (MathTex(r"\begin{bmatrix} 1.5 \\ 0.5 \end{bmatrix}")
                                 .next_to(vector_v.get_end(), direction=RIGHT, buff=0.1))

        self.play(Create(vector_i), Create(vector_j))
        self.play(Write(vector_i_label), Write(vector_j_label))
        self.play(Create(vector_v), Write(vector_v_coords_label))
        self.wait(0.5)
