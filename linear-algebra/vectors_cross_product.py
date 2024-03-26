#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(ThreeDScene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)
        axes = ThreeDAxes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-3.2, 3.2, 1],
            z_range=[-3.2, 3.2, 1],
            x_length=None,
            y_length=None,
            z_length=None
        )

        self.add(axes)

        # The scene itself
        vector_a_coord = np.array([1, 2, 1])
        vector_a = Arrow3D(ORIGIN, vector_a_coord, color=RED)
        vector_b_coord = np.array([-0.5, 1.5, 0])
        vector_b = Arrow3D(ORIGIN, vector_b_coord, color=BLUE)
        vector_s_coord = np.cross(vector_a_coord, vector_b_coord)
        vector_s = Arrow3D(ORIGIN, vector_s_coord, color=YELLOW, thickness=0.01)
        vector_n = Arrow3D(ORIGIN, vector_s_coord / np.linalg.norm(vector_s_coord), color=LIGHT_BROWN)
        plane = Polygon(ORIGIN, vector_a_coord, vector_a_coord + vector_b_coord, vector_b_coord,
                        color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0.5)

        self.add(vector_a, vector_b, vector_s, vector_n, plane)

        # Proof that Numeric and Geometric methods give the same result
        s_length = np.sqrt(
            np.power(vector_s_coord[0], 2) + np.power(vector_s_coord[1], 2) + np.power(vector_s_coord[2], 2))
        parallelogram_area = (np.sqrt(
            np.power(vector_a_coord[0], 2) + np.power(vector_a_coord[1], 2) + np.power(vector_a_coord[2], 2))
                              * np.sqrt(
                    np.power(vector_b_coord[0], 2) + np.power(vector_b_coord[1], 2) + np.power(vector_b_coord[2], 2))
                              * np.sin(np.arccos(clip(
                    np.dot(vector_a_coord, vector_b_coord) / np.linalg.norm(vector_a_coord) / np.linalg.norm(
                        vector_b_coord),
                    -1, 1))))

        print("Vector s length: " + str(s_length))
        print("Parallelogram area: " + str(parallelogram_area))

        cross_product_text = MathTex(
            r"{{\vec{a}}} \times {{\vec{b}}} = {{\hat{n}}} * |{{\vec{a}}}| * |{{\vec{b}}}| * \sin\theta_{{{a}}{{b}}} "
            r"= {{\vec{s}}}")
        cross_product_text[0].set_color(RED)
        cross_product_text[2].set_color(BLUE)
        cross_product_text[4].set_color(LIGHT_BROWN)
        cross_product_text[6].set_color(RED)
        cross_product_text[8].set_color(BLUE)
        cross_product_text[10].set_color(RED)
        cross_product_text[11].set_color(BLUE)
        cross_product_text[13].set_color(YELLOW)
        length_text = MathTex(
            r"|{{\vec{s}}}| = |{{\vec{a}}}| * |{{\vec{b}}}| * \sin\theta_{{{a}}{{b}}} = {{S}}_{{{a}}{{b}}}}",
        )
        length_text[1].set_color(YELLOW)
        length_text[3].set_color(RED)
        length_text[5].set_color(BLUE)
        length_text[7].set_color(RED)
        length_text[8].set_color(BLUE)
        length_text[10].set_color(YELLOW)
        length_text[12].set_color(RED)
        length_text[13].set_color(BLUE)
        where_text = MathTex(r"\text{where:}")
        where1_text = MathTex(
            r"\theta_{{{a}}{{b}}} \text{ is the angle between } {{\vec{a}}} \text{ and } {{\vec{b}}};",
        )
        where1_text[1].set_color(RED)
        where1_text[2].set_color(BLUE)
        where1_text[4].set_color(RED)
        where1_text[6].set_color(BLUE)
        where2_text = MathTex(
            r"{{\hat{n}}}\text{ is the unit vector perpendicular to both } {{\vec{a}}} \text{, } {{\vec{b}}};",
        )
        where2_text[0].set_color(LIGHT_BROWN)
        where2_text[2].set_color(RED)
        where2_text[4].set_color(BLUE)
        where3_text = MathTex(
            r"{{S}}_{{{a}}{{b}}}} \text{ is the area of the parallelogram formed by }  {{\vec{a}}} \text{, } {{\vec{b}}}.",
        )
        where3_text[0].set_color(YELLOW)
        where3_text[2].set_color(RED)
        where3_text[3].set_color(BLUE)
        where3_text[5].set_color(RED)
        where3_text[7].set_color(BLUE)

        (VGroup(cross_product_text, length_text).arrange(DOWN, center=False, aligned_edge=LEFT)
         .shift(np.array([-7.2, 3.3, 0])))
        (VGroup(where_text, where1_text, where2_text, where3_text).arrange(DOWN, center=False, aligned_edge=LEFT)
         .shift(np.array([-9.2, -1.3, 0])))
        self.add_fixed_in_frame_mobjects(
            cross_product_text, length_text, where_text, where1_text, where2_text, where3_text
        )

        # A hack to correctly rotate the camera around shifted axes
        VGroup(axes, vector_a, vector_b, vector_n, vector_s, plane).shift(np.array([-3, 0, 0]))
        self.set_camera_orientation(phi=75 * DEGREES, frame_center=axes.get_origin())

        # 1 turn in 10 seconds
        self.begin_ambient_camera_rotation(rate=PI / 5)
        self.wait(10)
        self.stop_ambient_camera_rotation()
