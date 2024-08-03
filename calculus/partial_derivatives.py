#!/usr/bin/env python3
from manim import *  # 0.18.0

config.background_color = ManimColor("#0e1116")


class MyScene(ThreeDScene):
    def construct(self):
        # Defaults
        MathTex.set_default(font_size=36)

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()

        axes = ThreeDAxes(
            x_range=[-3.2, 3.2, 1],
            y_range=[-3.2, 3.2, 1],
            z_range=[-3.2, 3.2, 1],
            x_length=None,
            y_length=None,
            z_length=None
        )
        labels = axes.get_axis_labels()

        self.add(axes, labels)

        # --------------------------------------------------------------------------------------------------------------
        # Calculating
        def func(x, y):
            return np.cos(x) * np.sin(y)

        def partial_der_x_func(x, y):
            return -np.sin(x) * np.sin(y)

        dot_coords = np.array([0.5, -1, func(0.5, -1)])

        m = partial_der_x_func(dot_coords[0], dot_coords[1])
        c = dot_coords[2] - m * dot_coords[0]

        print("a = " + str(dot_coords))
        print("m = " + str(m))
        print("c = " + str(c))

        def tangent_line_func(x, y):
            return m * x + c

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        surface = axes.plot_surface(func, fill_opacity=0.5, u_range=[-3.2, 3.2], v_range=[-3.2, 3.2])
        plane = (Square(side_length=6.4, color=GREY, fill_opacity=0.7, stroke_color=GREY, stroke_opacity=0.5)
                 .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0]))
                 .shift(np.array([0, axes.point_to_coords(dot_coords)[1], 0])))
        intersection = axes.plot_surface(func, checkerboard_colors=None, stroke_width=2, stroke_color=RED,
                                         u_range=[-3.2, 3.2], v_range=[dot_coords[1], dot_coords[1]])

        total_shift = np.array([2.7, 0, 0])

        tangent_line = (axes.plot_surface(tangent_line_func, checkerboard_colors=None, stroke_width=2,
                                          stroke_color=YELLOW, u_range=[dot_coords[0] - 1, dot_coords[0] + 1],
                                          v_range=[dot_coords[1], dot_coords[1]])
                        .shift(total_shift))

        dot = Dot3D(axes.point_to_coords(dot_coords), radius=0.05).shift(total_shift)

        dot_text = (
            MathTex(r"a [" + str(dot_coords[0]) + "," + str(dot_coords[1]) + "," + str(round(dot_coords[2], 3)) + "]")
            .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0]))
            .next_to(dot, direction=RIGHT + IN, buff=0.1))

        all_graphics_group = VGroup(axes, labels, surface, plane, intersection)

        function_text = (MathTex(r"f(x,y) = cos(x) sin(y)", color=ManimColor('#29ABCA'))
                         .shift(np.array([-4, 3, 0])))

        derivative_text = (MathTex(r"\frac{\partial}{\partial x}f(x,y) = -sin(x) sin(y)")
                           .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0])))

        m_text = (MathTex(r"m = \frac{\partial}{\partial x}f(" + str(dot_coords[0])
                          + "," + str(dot_coords[1]) + r") \approx " + str(round(m, 3)))
                  .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0])))

        c_formula_text = (MathTex(r"c = z_{a} - m * x_{a}")
                          .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0])))

        c_calculation_text = (MathTex(r"c = " + str(round(dot_coords[2], 3)) + "-" + str(round(m, 3)) + "*" +
                                      str(dot_coords[0]) + r"\approx" + str(round(c, 3)))
                              .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0])))

        z_formula_text = (MathTex(r"z = m * x + c", color=YELLOW)
                          .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0])))

        z_calculated_text = (MathTex(r"z = " + str(round(m, 3)) + "x" + str(round(c, 3)),
                                     color=YELLOW)
                             .rotate(angle=90 * DEGREES, axis=np.array([1, 0, 0])))

        (VGroup(derivative_text, m_text, c_formula_text, c_calculation_text, z_formula_text, z_calculated_text)
         .arrange(IN)
         .shift(np.array([-4, 0, 0.5])))

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.set_camera_orientation(phi=50 * DEGREES, theta=90 * DEGREES, frame_center=axes.get_origin())

        self.add_fixed_in_frame_mobjects(function_text)
        self.add(surface)

        # 1 turn in 10 seconds
        self.begin_ambient_camera_rotation(rate=PI / 5)

        self.wait(3)
        self.play(
            Create(plane),
            Create(intersection)
        )
        self.wait(1)

        self.stop_ambient_camera_rotation()

        self.play(
            phi.animate.set_value(90 * DEGREES),
            theta.animate.set_value(270 * DEGREES),
            Uncreate(surface),
            Unwrite(plane)
        )
        self.play(
            all_graphics_group.animate.shift(total_shift)
        )
        self.play(
            Create(dot),
            Write(dot_text)
        )

        self.play(Write(derivative_text))
        self.play(Write(m_text))
        self.play(Write(c_formula_text))
        self.play(Write(c_calculation_text))
        self.play(Write(z_formula_text))
        self.play(Write(z_calculated_text))

        self.wait()
        self.play(Create(tangent_line))

        self.wait(5)
