from manim import *
import numpy as np

class RankVisualization(ThreeDScene):
    def construct(self):
        # Set up the scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Title
        title = Text("Linear Transformations and Rank").scale(0.8)
        title.to_corner(UL).shift(RIGHT)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        
        # Create 3D axes
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=8
        )
        
        # Add axis labels
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        z_label = axes.get_z_axis_label("z")
        
        self.play(Create(axes), Write(x_label), Write(y_label), Write(z_label))
        
        # Create a 3D cube as the original object to transform
        cube = Cube(side_length=2, fill_color=BLUE, fill_opacity=0.3)
        self.play(Create(cube))
        self.wait(1)
        
        # Add explanation text at the bottom right corner (away from the visualization)
        explanation = Text("Original 3D Space", font_size=24)
        explanation.to_corner(DR)
        self.add_fixed_in_frame_mobjects(explanation)
        self.play(Write(explanation))
        self.wait(1)
        
        # ---------- Full Rank (Rank 3) Transformation ----------
        # Replace the explanation
        self.play(FadeOut(explanation))
        full_rank_title = Text("Full Rank (Rank = 3) Transformation", font_size=24)
        full_rank_title.to_corner(DR)
        self.add_fixed_in_frame_mobjects(full_rank_title)
        self.play(Write(full_rank_title))
        
        # Display the matrix
        full_rank_matrix = [
            [0.8, 0.1, 0.3],
            [0.2, 0.9, 0.1],
            [0.1, 0.3, 0.7]
        ]
        
        matrix_tex = MathTex(
            r"A = \begin{bmatrix} " + 
            r"0.8 & 0.1 & 0.3 \\ " +
            r"0.2 & 0.9 & 0.1 \\ " +
            r"0.1 & 0.3 & 0.7 " +
            r"\end{bmatrix}"
        )
        matrix_tex.to_corner(DL)
        self.add_fixed_in_frame_mobjects(matrix_tex)
        self.play(Write(matrix_tex))
        
        # Details about the transformation
        rank_info = Text("• Determinant ≠ 0\n• Maps R³ to R³\n• Preserves dimension", font_size=20)
        rank_info.next_to(full_rank_title, UP, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(rank_info)
        self.play(Write(rank_info))
        
        # Apply the transformation
        self.play(ApplyMatrix(full_rank_matrix, cube))
        self.wait(2)
        
        # Clean up for the next transformation
        self.play(
            FadeOut(full_rank_title),
            FadeOut(rank_info),
            FadeOut(matrix_tex)
        )
        
        # ---------- Rank 2 Transformation ----------
        # Create a new cube for the next transformation
        self.play(FadeOut(cube))
        cube2 = Cube(side_length=2, fill_color=GREEN, fill_opacity=0.3)
        self.play(Create(cube2))
        
        # Add explanation for rank 2
        rank2_title = Text("Rank 2 Transformation", font_size=24)
        rank2_title.to_corner(DR)
        self.add_fixed_in_frame_mobjects(rank2_title)
        self.play(Write(rank2_title))
        
        # Display the matrix for rank 2
        rank2_matrix = [
            [1, 0.5, 0],
            [0.5, 0.25, 0],
            [0, 0, 0.8]
        ]
        
        matrix_tex2 = MathTex(
            r"B = \begin{bmatrix} " + 
            r"1 & 0.5 & 0 \\ " +
            r"0.5 & 0.25 & 0 \\ " +
            r"0 & 0 & 0.8 " +
            r"\end{bmatrix}"
        )
        matrix_tex2.to_corner(DL)
        self.add_fixed_in_frame_mobjects(matrix_tex2)
        self.play(Write(matrix_tex2))
        
        # Details about the transformation
        rank_info2 = Text("• Determinant = 0\n• Maps R³ to a plane\n• Loses one dimension", font_size=20)
        rank_info2.next_to(rank2_title, UP, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(rank_info2)
        self.play(Write(rank_info2))
        
        # Create another matrix that will collapse to rank 2
        # This simulates a rank 2 transformation by flattening in one direction
        collapse_matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0.01]  # Almost zero to show the collapse
        ]
        
        self.play(ApplyMatrix(collapse_matrix, cube2))
        self.wait(1)
        
        # Apply another transformation to show how it stays in a plane
        shear_matrix = [
            [1, 0.5, 0],
            [0.5, 1, 0],
            [0, 0, 1]
        ]
        
        self.play(ApplyMatrix(shear_matrix, cube2))
        self.wait(2)
        
        # Clean up for the next transformation
        self.play(
            FadeOut(rank2_title),
            FadeOut(rank_info2),
            FadeOut(matrix_tex2)
        )
        
        # ---------- Rank 1 Transformation ----------
        # Create a new cube for the next transformation
        self.play(FadeOut(cube2))
        cube3 = Cube(side_length=2, fill_color=RED, fill_opacity=0.3)
        self.play(Create(cube3))
        
        # Add explanation for rank 1
        rank1_title = Text("Rank 1 Transformation", font_size=24)
        rank1_title.to_corner(DR)
        self.add_fixed_in_frame_mobjects(rank1_title)
        self.play(Write(rank1_title))
        
        # Display the matrix for rank 1
        rank1_matrix = [
            [1, 2, 3],
            [0.5, 1, 1.5],
            [0.25, 0.5, 0.75]
        ]
        
        matrix_tex3 = MathTex(
            r"C = \begin{bmatrix} " + 
            r"1 & 2 & 3 \\ " +
            r"0.5 & 1 & 1.5 \\ " +
            r"0.25 & 0.5 & 0.75 " +
            r"\end{bmatrix}"
        )
        matrix_tex3.to_corner(DL)
        self.add_fixed_in_frame_mobjects(matrix_tex3)
        self.play(Write(matrix_tex3))
        
        # Details about the transformation
        rank_info3 = Text("• Determinant = 0\n• Maps R³ to a line\n• Loses two dimensions", font_size=20)
        rank_info3.next_to(rank1_title, UP, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(rank_info3)
        self.play(Write(rank_info3))
        
        # First flatten in one direction (simulate part of rank 1 transformation)
        collapse_matrix1 = [
            [1, 0, 0],
            [0, 0.01, 0],  # Almost zero
            [0, 0, 1]
        ]
        
        self.play(ApplyMatrix(collapse_matrix1, cube3))
        
        # Then flatten in another direction to get a line (rank 1)
        collapse_matrix2 = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0.01]  # Almost zero
        ]
        
        self.play(ApplyMatrix(collapse_matrix2, cube3))
        
        # Apply a final stretching to emphasize the line
        stretch_matrix = [
            [2, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        
        self.play(ApplyMatrix(stretch_matrix, cube3))
        self.wait(2)
        
        # ---------- Rank 0 Transformation (Zero Matrix) ----------
        # Clean up
        self.play(
            FadeOut(rank1_title),
            FadeOut(rank_info3),
            FadeOut(matrix_tex3)
        )
        
        # Create a new cube
        self.play(FadeOut(cube3))
        cube4 = Cube(side_length=2, fill_color=YELLOW, fill_opacity=0.3)
        self.play(Create(cube4))
        
        # Add explanation for rank 0
        rank0_title = Text("Rank 0 Transformation (Zero Matrix)", font_size=24)
        rank0_title.to_corner(DR)
        self.add_fixed_in_frame_mobjects(rank0_title)
        self.play(Write(rank0_title))
        
        # Display the zero matrix
        matrix_tex4 = MathTex(
            r"D = \begin{bmatrix} " + 
            r"0 & 0 & 0 \\ " +
            r"0 & 0 & 0 \\ " +
            r"0 & 0 & 0 " +
            r"\end{bmatrix}"
        )
        matrix_tex4.to_corner(DL)
        self.add_fixed_in_frame_mobjects(matrix_tex4)
        self.play(Write(matrix_tex4))
        
        # Details about the transformation
        rank_info4 = Text("• Maps everything to origin\n• Completely collapses space", font_size=20)
        rank_info4.next_to(rank0_title, UP, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(rank_info4)
        self.play(Write(rank_info4))
        
        # Apply transformation that collapses everything to the origin
        zero_matrix = [
            [0.001, 0, 0],  # Almost zero
            [0, 0.001, 0],  # Almost zero
            [0, 0, 0.001]   # Almost zero
        ]
        
        self.play(ApplyMatrix(zero_matrix, cube4))
        self.wait(2)
        
        # Final summary
        self.play(
            FadeOut(rank0_title),
            FadeOut(rank_info4),
            FadeOut(matrix_tex4),
            FadeOut(cube4)
        )
        
        summary = VGroup(
            Text("Linear Transformation Rank Summary:", font_size=28),
            Text("• Rank 3: Transforms 3D space to 3D space", font_size=24),
            Text("• Rank 2: Collapses 3D space to a plane", font_size=24),
            Text("• Rank 1: Collapses 3D space to a line", font_size=24),
            Text("• Rank 0: Collapses everything to a point", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        summary.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(summary)
        self.play(Write(summary))
        
        self.wait(3)