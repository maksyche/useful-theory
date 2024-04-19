#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            foreground_plane_kwargs={
                "x_range": [-100, 100],
                "y_range": [-100, 100],
            },
            *kwargs
        )

    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        # The scene itself
        vector_x_coords = np.array([1, 1])
        matrix = np.array([[1, -1], [2, -1]])
        # matrix_inverse = np.linalg.inv(matrix)  # No pretty rounding
        matrix_inverse = np.array([[-1, 1], [-2, 1]])

        vector_v_coords = np.dot(matrix, vector_x_coords)
        print(vector_v_coords)

        math_text = MathTex(r"A\vec{x} = \vec{v}")
        math_text_matrix = (MathTex(r"\begin{bmatrix}" + str(matrix[0][0]) + r"&" + str(matrix[0][1]) + r"\\" +
                                    str(matrix[1][0]) + r"&" + str(matrix[1][1]) + r"\end{bmatrix}\begin{bmatrix}" +
                                    str(vector_x_coords[0]) + r"\\" + str(vector_x_coords[1]) + r"\end{bmatrix} = " +
                                    r"\begin{bmatrix}" + str(vector_v_coords[0]) + r"\\" +
                                    str(vector_v_coords[1]) + r"\end{bmatrix}"))
        math_text_group = VGroup(math_text, math_text_matrix).arrange(DOWN).shift(np.array([-4, 2, 0]))
        math_text[0][0].set_color(YELLOW)
        math_text[0][1:3].set_color(RED)
        math_text[0][4:6].set_color(ORANGE)
        math_text_matrix[0][1:7].set_color(YELLOW)
        math_text_matrix[0][9:11].set_color(RED)
        math_text_matrix[0][14:16].set_color(ORANGE)

        background_rectangle = BackgroundRectangle(math_text_group, color=config.background_color, fill_opacity=0.7,
                                                   buff=0.1)

        math_text_inverse = MathTex(r"\vec{x} = A^{-1}\vec{v}")
        math_text_matrix_inverse = (
            MathTex(r"\begin{bmatrix}" + str(vector_x_coords[0]) + r"\\" +
                    str(vector_x_coords[1]) + r"\end{bmatrix} = "
                                              r"\begin{bmatrix}" + str(matrix_inverse[0][0]) + r"&" + str(
                matrix_inverse[0][1]) + r"\\" +
                    str(matrix_inverse[1][0]) + r"&" + str(matrix_inverse[1][1]) + r"\end{bmatrix}\begin{bmatrix}" +
                    str(vector_v_coords[0]) + r"\\" + str(vector_v_coords[1]) + r"\end{bmatrix}"))
        math_text_inverse_group = (VGroup(math_text_inverse, math_text_matrix_inverse)
                                   .arrange(DOWN).shift(np.array([-4, 2, 0])))

        math_text_inverse[0][0:2].set_color(RED)
        math_text_inverse[0][3:6].set_color(PURPLE_A)
        math_text_inverse[0][6:8].set_color(ORANGE)
        math_text_matrix_inverse[0][1:3].set_color(RED)
        math_text_matrix_inverse[0][6:12].set_color(PURPLE_A)
        math_text_matrix_inverse[0][14:16].set_color(ORANGE)

        math_text_equation = MathTex(
            r"\begin{cases}" +
            "(" + str(matrix[0][0]) + r")x_{1} + (" + str(matrix[0][1]) + r")x_{2}=" + str(vector_v_coords[0]) + r"\\" +
            "(" + str(matrix[1][0]) + r")x_{1} + (" + str(matrix[1][1]) + r")x_{2}=" + str(vector_v_coords[1]) + r"\\" +
            r"\end{cases}"
        ).shift(np.array([4, 2, 0]))
        math_text_equation[0][2].set_color(YELLOW)
        math_text_equation[0][4:6].set_color(RED)
        math_text_equation[0][8:10].set_color(YELLOW)
        math_text_equation[0][11:13].set_color(RED)
        math_text_equation[0][14].set_color(ORANGE)
        math_text_equation[0][16].set_color(YELLOW)
        math_text_equation[0][18:20].set_color(RED)
        math_text_equation[0][22:24].set_color(YELLOW)
        math_text_equation[0][25:27].set_color(RED)
        math_text_equation[0][28].set_color(ORANGE)

        background_rectangle_equation = BackgroundRectangle(math_text_equation, color=config.background_color,
                                                            fill_opacity=0.7, buff=0.1)

        self.play(
            Create(background_rectangle), Write(math_text), Write(math_text_matrix),
            Create(background_rectangle_equation), Write(math_text_equation)
        )

        # Show text indices for easy coloring
        # self.add(index_labels(math_text[0]))
        # self.add(index_labels(math_text_matrix[0]))
        # self.add(index_labels(math_text_inverse[0]))
        # self.add(index_labels(math_text_matrix_inverse[0]))
        # self.add(index_labels(math_text_equation[0]))

        vector_v = Vector(vector_v_coords, color=ORANGE)
        self.add(vector_v)
        self.add_vector(vector_x_coords, color=RED)
        self.wait()
        self.moving_mobjects = []
        self.apply_matrix(matrix)
        self.wait(3)
        self.play(
            ReplacementTransform(math_text, math_text_inverse),
            ReplacementTransform(math_text_matrix, math_text_matrix_inverse)
        )
        self.moving_mobjects = []
        self.apply_matrix(matrix_inverse)
        self.wait(3)
        self.play(
            Uncreate(background_rectangle), Unwrite(math_text_inverse), Unwrite(math_text_matrix_inverse),
            Uncreate(background_rectangle_equation), Unwrite(math_text_equation)
        )
        self.wait(0.1)
