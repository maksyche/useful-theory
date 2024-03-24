#!/usr/bin/env python3
from manim import *  # 0.18.0


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
            x_range=(-2.4, 2.4),
            y_range=(-0.1, 1.25),
            x_length=12.8,
            y_length=3.6,

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

        VGroup(plane, axes_labels).shift(np.array([0, -1.5, 0]))
        self.add(plane, axes_labels)

        # The scene itself
        vector_a_coords = np.array([1, 0, 0])
        vector_a = plane.get_vector(np.array(vector_a_coords), color=RED)
        vector_a_label = MathTex(r"\hat{a}", color=RED).next_to(vector_a, direction=UP, buff=0.01)

        vector_b_coords = np.array([1, 0, 0])
        vector_b = plane.get_vector(np.array(vector_b_coords), color=BLUE)
        vector_b_label = MathTex(r"\hat{b}", color=BLUE).next_to(vector_b, direction=DOWN, buff=0)

        parallelogram = Polygon(
            vector_a.get_start(), vector_a.get_end(),
            # A hack because of the scaled and shifted plane
            vector_a.get_end() + np.array([vector_a.get_length(), 0, 0]), vector_b.get_end(),
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0.5
        )

        theta_tracker = ValueTracker(0)

        math_text = (MathTex(r"|\hat{a} \times \hat{b}| = |\hat{a}| * |\hat{b}| * \sin(\theta) =  1 * 1 * \sin"
                             + str(round(theta_tracker.get_value()))
                             + r"^{\circ} = "
                             + str(round(np.sin(theta_tracker.get_value() * DEGREES), 2)))
                     .next_to(plane, direction=UP, buff=2))

        self.add(vector_a, vector_b, vector_a_label, vector_b_label, parallelogram, math_text)

        # Required to calculate rotations against the default location
        vector_a_copy = vector_a.copy()
        vector_a_label_copy = vector_a_label.copy()

        vector_a.add_updater(
            lambda x: x.become(
                vector_a_copy.copy().rotate(theta_tracker.get_value() * DEGREES, about_point=plane.get_origin())
            )
        )
        vector_a_label.add_updater(
            lambda x: x.become(
                vector_a_label_copy.copy()
                .rotate(theta_tracker.get_value() * DEGREES, about_point=plane.get_origin())
                .rotate(-theta_tracker.get_value() * DEGREES)  # Preserve orientation of the sign
            )
        )
        math_text.add_updater(
            lambda x: x.become(
                MathTex(r"|\hat{a} \times \hat{b}| = |\hat{a}| * |\hat{b}| * \sin\theta =  1 * 1 * \sin"
                        + str(round(theta_tracker.get_value()))
                        + "^{\\circ} = "
                        + str(round(np.sin(theta_tracker.get_value() * DEGREES), 2)))
                .next_to(plane, direction=UP, buff=2)
            )
        )
        parallelogram.add_updater(
            lambda x: x.become(Polygon(
                vector_a.get_start(), vector_a.get_end(),
                # A hack because of the scaled and shifted plane
                vector_a.get_end() + np.array([vector_a.get_length(), 0, 0]), vector_b.get_end(),
                color=YELLOW, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0.5)
            )
        )

        # A hack with value=0.1. Angles don't work if set to 0
        self.play(theta_tracker.animate().set_value(0.1))
        theta = Angle.from_three_points(
            vector_a.get_end(), plane.get_origin(), vector_b.get_end(),
            other_angle=True, color=YELLOW
        )
        self.add(theta)
        theta.add_updater(
            lambda x: x.become(
                Angle.from_three_points(
                    vector_a.get_end(),
                    # A hack with the middle point, because it doesn't want to create angles for 180
                    plane.coords_to_point(0, -0.001),
                    vector_b.get_end(),
                    other_angle=True
                )
            )
        )

        self.play(theta_tracker.animate(run_time=2, rate_func=smoothererstep).set_value(90))
        self.wait(0.5)
        self.play(theta_tracker.animate(run_time=2, rate_func=smoothererstep).set_value(180))
        self.wait(0.5)

        # A hack with value=0.1. Angles don't work if set to 0
        self.play(theta_tracker.animate(run_time=3, rate_func=smoothererstep).set_value(0.1))
