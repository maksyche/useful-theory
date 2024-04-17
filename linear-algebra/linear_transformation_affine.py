#!/usr/bin/env python3
from __future__ import annotations

from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(LinearTransformationScene):

    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=False,
            show_basis_vectors=False,
            include_foreground_plane=False,
            include_background_plane=False,
            camera_class=ThreeDCamera,  # So I can rotate the scene
            *kwargs
        )

    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        axes = ThreeDAxes(
            x_range=[-6.4, 6.4],
            y_range=[-3.6, 3.6],
            z_range=[-1.5, 1.5, 1],
            x_length=None,
            y_length=None,
            z_length=None,
            tips=False
        )

        self.add(axes)

        # The scene itself
        vector_1_coords = np.array([1, 1, 1])
        vector_2_coords = np.array([1, -1, 1])
        vector_3_coords = np.array([-1, -1, 1])
        vector_4_coords = np.array([-1, 1, 1])
        vector_5_coords = np.array([1, 0, 1])
        vector_6_coords = np.array([0, -1, 1])
        vector_7_coords = np.array([-1, 0, 1])
        vector_8_coords = np.array([0, 1, 1])

        plane_top = Polygon(vector_1_coords, vector_2_coords, vector_3_coords, vector_4_coords,
                            color=YELLOW, fill_color=YELLOW, fill_opacity=1, stroke_opacity=1)

        vector_bottom_1_coords = np.array([1, 1, -1])
        vector_bottom_2_coords = np.array([1, -1, -1])
        vector_bottom_3_coords = np.array([-1, -1, -1])
        vector_bottom_4_coords = np.array([-1, 1, -1])

        plane_front = Polygon(vector_2_coords, vector_3_coords, vector_bottom_3_coords, vector_bottom_2_coords,
                              color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_opacity=0.5,
                              joint_type=LineJointType.ROUND)
        plane_back = Polygon(vector_1_coords, vector_4_coords, vector_bottom_4_coords, vector_bottom_1_coords,
                             color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_opacity=0.5,
                             joint_type=LineJointType.ROUND)
        plane_left = Polygon(vector_3_coords, vector_4_coords, vector_bottom_4_coords, vector_bottom_3_coords,
                             color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_opacity=0.5,
                             joint_type=LineJointType.ROUND)
        plane_right = Polygon(vector_1_coords, vector_2_coords, vector_bottom_2_coords, vector_bottom_1_coords,
                              color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_opacity=0.5,
                              joint_type=LineJointType.ROUND)
        plane_bottom = Polygon(vector_bottom_1_coords, vector_bottom_2_coords, vector_bottom_3_coords,
                               vector_bottom_4_coords,
                               color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_opacity=0.5,
                               joint_type=LineJointType.ROUND)

        matrix = np.array([[1, 0, 1], [0, 1, 0], [0, 0, 1]])
        matrix_inverse = np.array([[1, 0, -1], [0, 1, 0], [0, 0, 1]])

        math_text_string = (r"A = \begin{bmatrix}" +
                            str(matrix[0][0]) + r"&" + str(matrix[0][1]) + r"&" + str(matrix[0][2]) + r"\\" +
                            str(matrix[1][0]) + r"&" + str(matrix[1][1]) + r"&" + str(matrix[1][2]) + r"\\" +
                            str(matrix[2][0]) + r"&" + str(matrix[2][1]) + r"&" + str(matrix[2][2]) + r"\\" +
                            r"\end{bmatrix}")

        inverse_matrix_string = (r"A = \begin{bmatrix}" +
                                 str(matrix_inverse[0][0]) + r"&" + str(matrix_inverse[0][1]) + r"&" +
                                 str(matrix_inverse[0][2]) + r"\\" +
                                 str(matrix_inverse[1][0]) + r"&" + str(matrix_inverse[1][1]) + r"&" +
                                 str(matrix_inverse[1][2]) + r"\\" +
                                 str(matrix_inverse[2][0]) + r"&" + str(matrix_inverse[2][1]) + r"&" +
                                 str(matrix_inverse[2][2]) + r"\\" +
                                 r"\end{bmatrix}")

        # I have to play with colors and placement because many animations don't work as the text is fixed in the frame
        matrix_text = MathTex(math_text_string, color="#0e1116").shift(np.array([-3.5, 2.5, 0]))
        inverse_matrix_text = MathTex(inverse_matrix_string, color="#0e1116").shift(np.array([3.5, 2.5, 0]))

        self.add(matrix_text, inverse_matrix_text)
        self.camera.add_fixed_in_frame_mobjects(matrix_text, inverse_matrix_text)

        vector_1 = Vector(vector_1_coords, color=YELLOW)
        vector_2 = Vector(vector_2_coords, color=YELLOW)
        vector_3 = Vector(vector_3_coords, color=YELLOW)
        vector_4 = Vector(vector_4_coords, color=YELLOW)
        vector_5 = Vector(vector_5_coords, color=YELLOW)
        vector_6 = Vector(vector_6_coords, color=YELLOW)
        vector_7 = Vector(vector_7_coords, color=YELLOW)
        vector_8 = Vector(vector_8_coords, color=YELLOW)
        self.play(
            Create(vector_1),
            Create(vector_2),
            Create(vector_3),
            Create(vector_4),
            Create(vector_5),
            Create(vector_6),
            Create(vector_7),
            Create(vector_8)
        )
        self.play(
            Create(plane_top)
        )
        self.add_transformable_mobject(plane_top)
        self.play(
            Uncreate(vector_1),
            Uncreate(vector_2),
            Uncreate(vector_3),
            Uncreate(vector_4),
            Uncreate(vector_5),
            Uncreate(vector_6),
            Uncreate(vector_7),
            Uncreate(vector_8),
        )
        self.play(
            matrix_text.animate.set_color(WHITE),
        )

        self.moving_mobjects = []  # A well-known workaround
        self.apply_matrix(matrix)

        self.play(
            matrix_text.animate.set_color("#0e1116"),
            inverse_matrix_text.animate.set_color(WHITE)
        )

        self.moving_mobjects = []  # A well-known workaround
        self.apply_matrix(matrix_inverse)

        # A hack to smoothly rotate the scene
        for x in range(39):
            self.renderer.camera.set_phi((x + 1) * 2 * DEGREES)
            self.wait(0.1)

        self.play(
            Create(plane_back),
            Create(plane_left),
            Create(plane_right),
            Create(plane_bottom),
            Create(plane_front)
        )
        self.add_transformable_mobject(plane_top, plane_front, plane_back, plane_left, plane_right, plane_bottom)
        self.play(
            matrix_text.animate.set_color(WHITE),
            inverse_matrix_text.animate.set_color("#0e1116")
        )

        self.moving_mobjects = []  # A well-known workaround
        self.apply_matrix(matrix)

        self.play(
            matrix_text.animate.set_color("#0e1116"),
            inverse_matrix_text.animate.set_color(WHITE)
        )

        self.moving_mobjects = []  # A well-known workaround
        self.apply_matrix(matrix_inverse)

        self.wait()
