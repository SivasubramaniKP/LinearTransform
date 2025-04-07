from manim import *

class GeometricTransformations(Scene):
    def construct(self):
        # Introduction title
        title = Text("2D Geometric Transformations", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # Create a square as our demonstration shape
        square = Square(side_length=2, color=BLUE)
        square.move_to(ORIGIN)
        
        # Add coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": GREY}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": GREY_C,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5
            }
        )
        
        self.play(Create(grid), Create(axes), Write(axes_labels))
        self.play(Create(square))
        
        # Add initial shape label
        original_label = Text("Original Shape", font_size=24).next_to(square, DOWN, buff=0.5)
        self.play(Write(original_label))
        self.wait(1)
        
        # 1. Translation
        title_translation = Text("Translation", font_size=36).to_edge(UP)
        self.play(FadeOut(original_label), Write(title_translation))
        
        # Vector for translation
        arrow = Arrow(start=square.get_center(), end=square.get_center() + RIGHT * 3, color=YELLOW)
        vector_label = Text("(3, 0)", font_size=24).next_to(arrow, UP)
        self.play(Create(arrow), Write(vector_label))
        
        # Perform translation
        translated_square = square.copy().shift(RIGHT * 3)
        translated_square.set_color(GREEN)
        
        self.play(TransformFromCopy(square, translated_square))
        translation_label = Text("Translated Shape", font_size=24).next_to(translated_square, DOWN, buff=0.5)
        self.play(Write(translation_label))
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(arrow),
            FadeOut(vector_label),
            FadeOut(translation_label),
            FadeOut(translated_square),
            FadeOut(title_translation)
        )
        
        # 2. Scaling
        title_scaling = Text("Scaling", font_size=36).to_edge(UP)
        self.play(Write(title_scaling))
        
        # Scale factors
        scale_label = Text("Scale by (1.5, 0.5)", font_size=24).to_edge(UP, buff=1.5)
        self.play(Write(scale_label))
        
        # Perform scaling
        scaled_square = square.copy().scale(1.5, about_point=ORIGIN)
        scaled_square.stretch(1/3, 1, about_point=ORIGIN)  # Make it a rectangle
        scaled_square.set_color(ORANGE)
        
        self.play(TransformFromCopy(square, scaled_square))
        scaling_label = Text("Scaled Shape", font_size=24).next_to(scaled_square, DOWN, buff=0.5)
        self.play(Write(scaling_label))
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(scale_label),
            FadeOut(scaling_label),
            FadeOut(scaled_square),
            FadeOut(title_scaling)
        )
        
        # 3. Rotation
        title_rotation = Text("Rotation", font_size=36).to_edge(UP)
        self.play(Write(title_rotation))
        
        # Rotation angle
        angle_value = 45
        angle_label = Text(f"Rotate by {angle_value}°", font_size=24).to_edge(UP, buff=1.5)
        self.play(Write(angle_label))
        
        # Perform rotation
        rotated_square = square.copy().rotate(angle_value * DEGREES, about_point=ORIGIN)
        rotated_square.set_color(RED)
        
        # Add arc to show rotation angle
        arc = Arc(
            radius=0.5,
            angle=angle_value * DEGREES,
            color=YELLOW
        ).move_to(ORIGIN)
        
        self.play(Create(arc))
        self.play(TransformFromCopy(square, rotated_square))
        rotation_label = Text("Rotated Shape", font_size=24).next_to(rotated_square, DOWN, buff=0.5)
        self.play(Write(rotation_label))
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(angle_label),
            FadeOut(rotation_label),
            FadeOut(rotated_square),
            FadeOut(arc),
            FadeOut(title_rotation)
        )
        
        # 4. Shearing
        title_shearing = Text("Shearing", font_size=36).to_edge(UP)
        self.play(Write(title_shearing))
        
        # Shear factors
        shear_label = Text("Shear by (0.5, 0) along x", font_size=24).to_edge(UP, buff=1.5)
        self.play(Write(shear_label))
        
        # Perform shearing
        sheared_square = square.copy()
        shear_matrix = np.array([
            [1, 0.5, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        sheared_square.apply_matrix(shear_matrix)
        sheared_square.set_color(PURPLE)
        
        self.play(TransformFromCopy(square, sheared_square))
        shearing_label = Text("Sheared Shape", font_size=24).next_to(sheared_square, DOWN, buff=0.5)
        self.play(Write(shearing_label))
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(shear_label),
            FadeOut(shearing_label),
            FadeOut(sheared_square),
            FadeOut(title_shearing)
        )
        
        # 5. Reflection
        title_reflection = Text("Reflection", font_size=36).to_edge(UP)
        self.play(Write(title_reflection))
        
        # Reflection line
        reflection_line = Line([-3, 0, 0], [3, 0, 0], color=YELLOW)
        reflection_label = Text("Reflect across x-axis", font_size=24).to_edge(UP, buff=1.5)
        self.play(Create(reflection_line), Write(reflection_label))
        
        # Perform reflection
        reflected_square = square.copy()
        reflection_matrix = np.array([
            [1, 0, 0],
            [0, -1, 0],
            [0, 0, 1]
        ])
        reflected_square.apply_matrix(reflection_matrix)
        reflected_square.set_color(TEAL)
        
        self.play(TransformFromCopy(square, reflected_square))
        reflecting_label = Text("Reflected Shape", font_size=24).next_to(reflected_square, DOWN, buff=0.5)
        self.play(Write(reflecting_label))
        self.wait(1)
        
        # Clean up individual elements
        self.play(
            FadeOut(reflection_line),
            FadeOut(reflection_label),
            FadeOut(reflecting_label)
        )
        
        # Show all transformations together
        self.play(FadeOut(title_reflection))
        
        final_title = Text("All Transformations", font_size=36).to_edge(UP)
        self.play(Write(final_title))
        
        # Recreate all transformed shapes
        translated_square = square.copy().shift(RIGHT * 3).set_color(GREEN)
        scaled_square = square.copy().scale(1.5, about_point=ORIGIN).stretch(1/3, 1, about_point=ORIGIN).set_color(ORANGE)
        rotated_square = square.copy().rotate(angle_value * DEGREES, about_point=ORIGIN).set_color(RED)
        sheared_square = square.copy().apply_matrix(shear_matrix).set_color(PURPLE)
        reflected_square = square.copy().apply_matrix(reflection_matrix).set_color(TEAL)
        
        # Show all transformations at once
        self.play(
            TransformFromCopy(square, translated_square),
            TransformFromCopy(square, scaled_square),
            TransformFromCopy(square, rotated_square),
            TransformFromCopy(square, sheared_square),
            TransformFromCopy(square, reflected_square)
        )
        
        # Label each transformed shape
        translated_label = Text("Translation", font_size=16).next_to(translated_square, DOWN, buff=0.3)
        scaled_label = Text("Scaling", font_size=16).next_to(scaled_square, DOWN, buff=0.3)
        rotated_label = Text("Rotation", font_size=16).next_to(rotated_square, DOWN, buff=0.3)
        sheared_label = Text("Shearing", font_size=16).next_to(sheared_square, DOWN, buff=0.3)
        reflected_label = Text("Reflection", font_size=16).next_to(reflected_square, DOWN, buff=0.3)
        original_label = Text("Original", font_size=16).next_to(square, DOWN, buff=0.3)
        
        self.play(
            Write(translated_label),
            Write(scaled_label),
            Write(rotated_label),
            Write(sheared_label),
            Write(reflected_label),
            Write(original_label)
        )
        
        self.wait(2)
        
        # Conclusion
        self.play(
            FadeOut(translated_square),
            FadeOut(scaled_square),
            FadeOut(rotated_square),
            FadeOut(sheared_square),
            FadeOut(reflected_square),
            FadeOut(square),
            FadeOut(translated_label),
            FadeOut(scaled_label),
            FadeOut(rotated_label),
            FadeOut(sheared_label),
            FadeOut(reflected_label),
            FadeOut(original_label),
            FadeOut(grid),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(final_title)
        )
        
        # End screen
        end_title = Text("2D Geometric Transformations", font_size=36)
        subtitle = Text("Translation, Scaling, Rotation, Shearing, Reflection", font_size=24).next_to(end_title, DOWN)
        
        self.play(Write(end_title), Write(subtitle))
        self.wait(2)