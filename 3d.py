from manim import *
import numpy as np

class LinearTransformations3D(ThreeDScene):
    def construct(self):
        # Set the camera orientation for better 3D view
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            z_length=10
        )
        
        # Add labels to axes
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = axes.get_z_axis_label("z")
        
        self.play(Create(axes), Write(x_label), Write(y_label), Write(z_label))
        
        # Create a 3D cube
        cube = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.5)
        self.play(Create(cube))
        self.wait(1)
        
        # Display title for each transformation
        title = Text("3D Linear Transformations").to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create matrices for different transformations
        scaling_matrix = [
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        
        # Use LaTeX fractions for rotation matrices
        rotation_x_matrix = [
            [1, 0, 0],
            [0, r"\frac{1}{2}", r"-\frac{\sqrt{3}}{2}"],
            [0, r"\frac{\sqrt{3}}{2}", r"\frac{1}{2}"]
        ]
        
        rotation_y_matrix = [
            [r"\frac{1}{\sqrt{2}}", 0, r"\frac{1}{\sqrt{2}}"],
            [0, 1, 0],
            [r"-\frac{1}{\sqrt{2}}", 0, r"\frac{1}{\sqrt{2}}"]
        ]
        
        # For computation, we still need numerical values
        rotation_x_matrix_numeric = [
            [1, 0, 0],
            [0, np.cos(PI/3), -np.sin(PI/3)],
            [0, np.sin(PI/3), np.cos(PI/3)]
        ]
        
        rotation_y_matrix_numeric = [
            [np.cos(PI/4), 0, np.sin(PI/4)],
            [0, 1, 0],
            [-np.sin(PI/4), 0, np.cos(PI/4)]
        ]
        
        shear_matrix = [
            [1, 0.5, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        
        # Function to display matrix
        def show_matrix(matrix, name):
            # Check if the matrix elements are strings (LaTeX) or numbers
            matrix_tex_elements = []
            for row in matrix:
                row_elements = []
                for element in row:
                    if isinstance(element, str):
                        row_elements.append(element)
                    else:
                        row_elements.append(str(element))
                matrix_tex_elements.append(" & ".join(row_elements))
            
            matrix_tex_str = r"\begin{bmatrix} " + \
                             r" \\ ".join(matrix_tex_elements) + \
                             r" \end{bmatrix}"
            
            matrix_tex = MathTex(matrix_tex_str)
            matrix_title = Text(name).next_to(matrix_tex, UP)
            
            # Position matrix at the bottom center
            matrix_tex.to_edge(DOWN, buff=1)
            matrix_title.next_to(matrix_tex, UP)
            
            self.add_fixed_in_frame_mobjects(matrix_tex, matrix_title)
            self.play(Write(matrix_title), Write(matrix_tex))
            return matrix_tex, matrix_title
        
        # Scaling transformation
        matrix_tex, matrix_title = show_matrix(scaling_matrix, "Scaling Matrix")
        self.play(ApplyMatrix(scaling_matrix, cube))
        self.wait(1)
        self.play(FadeOut(matrix_tex), FadeOut(matrix_title))
        
        # Rotation around x-axis
        matrix_tex, matrix_title = show_matrix(rotation_x_matrix, "X-Axis Rotation Matrix")
        self.play(ApplyMatrix(rotation_x_matrix_numeric, cube))
        self.wait(1)
        self.play(FadeOut(matrix_tex), FadeOut(matrix_title))
        
        # Rotation around y-axis
        matrix_tex, matrix_title = show_matrix(rotation_y_matrix, "Y-Axis Rotation Matrix")
        self.play(ApplyMatrix(rotation_y_matrix_numeric, cube))
        self.wait(1)
        self.play(FadeOut(matrix_tex), FadeOut(matrix_title))
        
        # Shear transformation
        matrix_tex, matrix_title = show_matrix(shear_matrix, "Shear Matrix")
        self.play(ApplyMatrix(shear_matrix, cube))
        self.wait(1)
        self.play(FadeOut(matrix_tex), FadeOut(matrix_title))
        
        # Reset the cube to demonstrate composite transformations
        self.play(FadeOut(cube))
        new_cube = Cube(side_length=2, fill_color=GREEN, fill_opacity=0.5)
        self.play(Create(new_cube))
        
        # Composite transformation
        
        
        self.wait(2)