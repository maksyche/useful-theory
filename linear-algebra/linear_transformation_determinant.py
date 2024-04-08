#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            i_hat_color=GREEN_C,
            j_hat_color=RED_C,
            *kwargs
        )

    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        # plane = NumberPlane(
        #     # X/Y ration should always be 16/9, but with some space after the last tick:
        #     # 17.6/9.9
        #     # 12.8/7.2
        #     # 9.6/5.4
        #     # 6.4/3.6
        #     # 4.8/2.7
        #     # 3.2/1.8
        #     # 2.4/1.35
        #     # 1.6/0.9
        #     x_range=(-3.2, 3.2),
        #     y_range=(-1.8, 1.8),
        #     x_length=12.8,
        #     y_length=7.2,
        #
        #     axis_config={
        #         "include_numbers": True,
        #         "include_ticks": True,
        #     }
        # )

        # Axes labels config
        # plane.get_axis(0).set(color=BLUE)
        # plane.get_axis(1).set(color=BLUE)
        # axes_labels = self.get_axis_labels()

        # self.add(plane, axes_labels)

        # The scene itself
        matrix = np.array([[1, -2], [1, 1]])
        determinant = np.linalg.det(matrix)

        text = (
            MathTex(r"\begin{vmatrix}" + str(matrix[0][0]) + r"&" + str(matrix[0][1]) + r"\\" +
                    str(matrix[1][0]) + r"&" + str(matrix[1][1]) + r"\end{vmatrix} = " +
                    "(" + str(matrix[0][0]) + "*" + str(matrix[1][1]) + ") - " +
                    "(" + str(matrix[0][1]) + "*" + str(matrix[1][0]) + ") = " +
                    str(round(determinant)))
            .shift(np.array([-4, 3, 0])))
        # self.add(index_labels(text[0]))  # Show text indices for easy coloring
        text[0][4].set_color(GREEN_C)
        text[0][7].set_color(GREEN_C)
        text[0][15].set_color(GREEN_C)
        text[0][24].set_color(GREEN_C)
        text[0][5:7].set_color(RED_C)
        text[0][8].set_color(RED_C)
        text[0][17].set_color(RED_C)
        text[0][21:23].set_color(RED_C)
        text[0][27].set_color(YELLOW)

        plane = Polygon(ORIGIN, np.array([1, 0, 0]), np.array([1, 1, 0]), np.array([0, 1, 0]),
                        color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0.5)

        background_rectangle = BackgroundRectangle(text, color=config.background_color, fill_opacity=0.7, buff=0.1)

        self.add_transformable_mobject(plane)
        self.add(background_rectangle, text)
        self.wait()
        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait(3)
