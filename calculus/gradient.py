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

        def partial_der_y_func(x, y):
            return np.cos(x) * np.cos(y)

        dot_coords = np.array([0.5, -1, func(0.5, -1)])

        partial_der_x_in_dot = partial_der_x_func(dot_coords[0], dot_coords[1])
        partial_der_y_in_dot = partial_der_y_func(dot_coords[0], dot_coords[1])

        # Make it a unit vector
        scale = 1 / np.sqrt(np.power(partial_der_x_in_dot, 2) + np.power(partial_der_y_in_dot, 2))

        print("der x = " + str(partial_der_x_in_dot))
        print("der y = " + str(partial_der_y_in_dot))
        print("scale = " + str(scale))

        gradient_vector_coords = dot_coords + scale * np.array([partial_der_x_in_dot, partial_der_y_in_dot, 0])

        # --------------------------------------------------------------------------------------------------------------
        # Plotting
        surface = axes.plot_surface(func, fill_opacity=0.5, u_range=[-3.2, 3.2], v_range=[-3.2, 3.2])
        dot = Dot3D(axes.point_to_coords(dot_coords), radius=0.05)
        gradient_vector = Arrow(
            axes.point_to_coords(dot_coords), axes.point_to_coords(gradient_vector_coords),
            buff=0,
            color=RED,
        )

        function_text = MathTex(r"f(x,y) = cos(x) sin(y)", color=ManimColor('#29ABCA'))
        partial_der_x_text = MathTex(r"\frac{\partial}{\partial x}f(x,y) = -sin(x) sin(y)")
        partial_der_y_text = MathTex(r"\frac{\partial}{\partial y}f(x,y) = cos(x) cos(y)")
        gradient_text = MathTex(r"\nabla f(x,y) = \begin{bmatrix}"
                                r"\frac{\partial}{\partial x}f(x,y)\\\\"
                                r"\frac{\partial}{\partial y}f(x,y)"
                                r"\end{bmatrix}")

        gradient_calculated_text = MathTex(r"\nabla f(" + str(dot_coords[0]) + "," + str(dot_coords[1])
                                           + r") \approx "
                                             r"\begin{bmatrix}"
                                           + str(round(partial_der_x_in_dot, 3)) + r"\\\\"
                                           + str(round(partial_der_y_in_dot, 3))
                                           + r"\end{bmatrix}", color=RED)

        (VGroup(function_text, partial_der_x_text, partial_der_y_text, gradient_text, gradient_calculated_text)
         .arrange(DOWN)
         .shift(np.array([-7, 0, 0])))

        # A hack to correctly rotate the camera around shifted axes
        VGroup(axes, labels, surface, dot, gradient_vector).shift(np.array([-2.5, 0, 0]))

        # --------------------------------------------------------------------------------------------------------------
        # Animation
        self.set_camera_orientation(phi=50 * DEGREES, theta=90 * DEGREES, frame_center=axes.get_origin())

        self.add_fixed_in_frame_mobjects(function_text, partial_der_x_text, partial_der_y_text, gradient_text,
                                         gradient_calculated_text)
        self.add(gradient_vector, dot, surface)

        # 1 turn in 10 seconds
        self.begin_ambient_camera_rotation(rate=PI / 5)

        self.wait(10)
        self.stop_ambient_camera_rotation()
