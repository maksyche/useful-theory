#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=False,
            include_foreground_plane=False,
            *kwargs
        )

    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        # The scene itself
        vector_v_coords = np.array([0, 1])
        matrix = np.array([[1, -1], [2, -1]])
        vector_x_coords = np.dot(np.linalg.inv(matrix), vector_v_coords)

        # It will fail if b is zero, but works for this case:
        # ax + by - c = 0
        # by = c - ax
        # y = (c - ax) / b
        #
        # Manual check:
        # x - y = 0
        # y = x
        equation1 = FunctionGraph(
            lambda x: (vector_v_coords[0] - (matrix[0][0] * x)) / matrix[0][1],
            stroke_opacity=0.5,
            color=WHITE
        )

        # Manual check:
        # 2x - y = 1
        # y = 2x - 1
        equation2 = FunctionGraph(
            lambda x: (vector_v_coords[1] - (matrix[1][0] * x)) / matrix[1][1],
            stroke_opacity=0.5,
            color=WHITE
        )

        math_text_equation = MathTex(
            r"\begin{cases}" +
            "(" + str(matrix[0][0]) + r")x_{1} + (" + str(matrix[0][1]) + r")x_{2}=" + str(vector_v_coords[0]) + r"\\" +
            "(" + str(matrix[1][0]) + r")x_{1} + (" + str(matrix[1][1]) + r")x_{2}=" + str(vector_v_coords[1]) + r"\\" +
            r"\end{cases}"
        )
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

        # Manual input only
        math_text_equation_simplified = MathTex(
            r"\begin{cases}" +
            r"x_{1} - x_{2} = 0 \\" +
            r"2x_{1} - x_{2} = 1\\" +
            r"\end{cases}"
        )
        math_text_equation_simplified[0][1:3].set_color(RED)
        math_text_equation_simplified[0][4:6].set_color(RED)
        math_text_equation_simplified[0][7].set_color(ORANGE)
        math_text_equation_simplified[0][8].set_color(YELLOW)
        math_text_equation_simplified[0][9:11].set_color(RED)
        math_text_equation_simplified[0][12:14].set_color(RED)
        math_text_equation_simplified[0][15].set_color(ORANGE)

        (VGroup(math_text_equation, math_text_equation_simplified)
         .arrange(DOWN).shift(np.array([-4, 2, 0])))

        background_rectangle_equation = BackgroundRectangle(math_text_equation, color=config.background_color,
                                                            fill_opacity=0.7, buff=0.1)
        background_rectangle_equation_simplified = BackgroundRectangle(math_text_equation_simplified,
                                                                       color=config.background_color,
                                                                       fill_opacity=0.7, buff=0.1)

        equation1_label = MathTex(r"x_{1} - x_{2} = 0")
        equation1_label[0][0:2].set_color(RED)
        equation1_label[0][3:5].set_color(RED)
        equation1_label[0][6].set_color(ORANGE)

        equation2_label = MathTex(r"2x_{1} - x_{2} = 1")
        equation2_label[0][0].set_color(YELLOW)
        equation2_label[0][1:3].set_color(RED)
        equation2_label[0][4:6].set_color(RED)
        equation2_label[0][7].set_color(ORANGE)

        equation1_label.rotate(45 * DEGREES).shift(np.array([2.5, 2, 0]))
        equation2_label.rotate(63 * DEGREES).shift(np.array([1.4, 2.7, 0]))

        self.play(
            Create(background_rectangle_equation),
            Create(background_rectangle_equation_simplified),
            Write(math_text_equation),
            Write(math_text_equation_simplified)
        )
        self.play(Create(self.add_vector(vector_v_coords, animate=False, color=ORANGE)))
        self.play(Create(equation1))
        self.play(Write(equation1_label))
        self.play(Create(equation2))
        self.play(Write(equation2_label))
        self.play(Create(self.add_vector(vector_x_coords, animate=False, color=RED)))
        self.wait(3)
