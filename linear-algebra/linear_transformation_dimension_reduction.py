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
        vector_v_coords = np.array([4, 1])
        matrix = np.array([[1, -2], [0, 0]])

        transformed_v_coords = matrix.dot(vector_v_coords)

        text = (
            MathTex(r"A\vec{v} = \begin{bmatrix}" + str(matrix[0][0]) + r"&" + str(matrix[0][1]) + r"\\" +
                    str(matrix[1][0]) + r"&" + str(matrix[1][1]) + r"\end{bmatrix}\begin{bmatrix}" +
                    str(vector_v_coords[0]) + r"\\" + str(vector_v_coords[1]) + r"\end{bmatrix} = " +
                    r"\begin{bmatrix}" + str(transformed_v_coords[0]) + r"\\" +
                    str(transformed_v_coords[1]) + r"\end{bmatrix}")
            .shift(np.array([-4.5, 3, 0])))
        # self.add(index_labels(text[0]))  # Show text indices for easy coloring
        text[0][1:3].set_color(YELLOW)
        text[0][5].set_color(GREEN_C)
        text[0][8].set_color(GREEN_C)
        text[0][6:8].set_color(RED_C)
        text[0][9].set_color(RED_C)
        text[0][12:14].set_color(YELLOW)
        text[0][17:19].set_color(ORANGE)

        background_rectangle = BackgroundRectangle(text, color=config.background_color, fill_opacity=0.7, buff=0.1)

        self.add(background_rectangle, text)
        vector_v = self.add_vector(vector_v_coords, color=YELLOW)
        self.wait()
        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.play(vector_v.animate(time=0.1).set_color(ORANGE))
        self.wait(3)
