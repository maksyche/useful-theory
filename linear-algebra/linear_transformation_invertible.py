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
        vector_v_coords = np.array([1, 1])
        matrix = np.array([[0, -2], [2, 0]])
        # matrix_inverse = np.linalg.inv(matrix)  # No pretty rounding
        matrix_inverse = np.array([[0, 0.5], [-0.5, 0]])
        matrix_identity = np.array([[1, 0], [0, 1]])

        text = (
            MathTex(r"(AA^{-1})\vec{v} = "
                    r"\Bigg(\begin{bmatrix}" + str(matrix[0][0]) + r"&" + str(matrix[0][1]) + r"\\" +
                    str(matrix[1][0]) + r"&" + str(matrix[1][1]) + r"\end{bmatrix}" +

                    r"\begin{bmatrix}" + str(matrix_inverse[0][0]) + r"&" + str(matrix_inverse[0][1]) + r"\\" +
                    str(matrix_inverse[1][0]) + r"&" + str(matrix_inverse[1][1]) + r"\end{bmatrix}\Bigg)" +
                    r"\begin{bmatrix}" + str(vector_v_coords[0]) + r"\\" + str(vector_v_coords[1]) + r"\end{bmatrix}=" +

                    r"\begin{bmatrix}" + str(matrix_identity[0][0]) + r"&" + str(matrix_identity[0][1]) + r"\\" +
                    str(matrix_identity[1][0]) + r"&" + str(matrix_identity[1][1]) + r"\end{bmatrix}\begin{bmatrix}" +
                    str(vector_v_coords[0]) + r"\\" + str(vector_v_coords[1]) + r"\end{bmatrix} = " +
                    r"\begin{bmatrix}" + str(vector_v_coords[0]) + r"\\" +
                    str(vector_v_coords[1]) + r"\end{bmatrix}")
            .shift(np.array([0, -2, 0])))
        # self.add(index_labels(text[0]))  # Show text indices for easy coloring
        text[0][6:8].set_color(YELLOW)
        text[0][34:36].set_color(YELLOW)
        text[0][39].set_color(GREEN_C)
        text[0][41].set_color(GREEN_C)
        text[0][40].set_color(RED_C)
        text[0][42].set_color(RED_C)
        text[0][45:47].set_color(YELLOW)
        text[0][50:52].set_color(ORANGE)

        background_rectangle = BackgroundRectangle(text, color=config.background_color, fill_opacity=1, buff=0.1)

        self.add(background_rectangle, text)
        vector_v = self.add_vector(vector_v_coords, color=YELLOW)
        self.wait()
        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.moving_mobjects = []
        self.apply_matrix(matrix_inverse)
        self.play(vector_v.animate(time=0.1).set_color(ORANGE))
        self.wait(3)
