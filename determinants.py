
from manim import *

class DeterminantAsArea(Scene):
    def construct(self):
        # Introduction title
        title = Text("Determinant as Area Visualization").scale(0.8)
        subtitle = Text("The determinant represents the area spanned by transformed basis vectors", font_size=24).next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Create coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            axis_config={"include_tip": True},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        self.play(Create(axes), Create(axes_labels))
        
        # Define original basis vectors
        vec_i = Vector([1, 0], color=RED)
        vec_j = Vector([0, 1], color=GREEN)
        
        # Label the basis vectors
        i_label = MathTex(r"\vec{i}").next_to(vec_i.get_end(), DOWN)
        j_label = MathTex(r"\vec{j}").next_to(vec_j.get_end(), LEFT)
        
        # Draw original basis vectors
        self.play(Create(vec_i), Create(vec_j))
        self.play(Write(i_label), Write(j_label))
        
        # Create unit square using basis vectors
        unit_square = Polygon(
            np.array([0, 0, 0]), 
            np.array([1, 0, 0]), 
            np.array([1, 1, 0]), 
            np.array([0, 1, 0]),
            color=BLUE,
            fill_opacity=0.3
        )
        
        self.play(Create(unit_square))
        
        # Add label for the area
        area_label = MathTex(r"\text{Area} = 1").to_edge(UP)
        det_label = MathTex(r"\det(I) = 1").next_to(area_label, DOWN)
        
        self.play(Write(area_label), Write(det_label))
        self.wait(1)
        
        # Define a series of transformations with increasing complexity
        transformations = [
            {
                "matrix": [[2, 0], [0, 1]],
                "desc": "Scaling in x-direction: det = 2",
                "color": BLUE_C
            },
            {
                "matrix": [[1, 0], [0, 2]],
                "desc": "Scaling in y-direction: det = 2",
                "color": PURPLE_C
            },
            {
                "matrix": [[2, 0], [0, 2]],
                "desc": "Uniform scaling: det = 4",
                "color": TEAL_C
            },
            {
                "matrix": [[0, 1], [1, 0]],
                "desc": "Reflection: det = -1",
                "color": ORANGE
            },
            {
                "matrix": [[1, 1], [0, 1]],
                "desc": "Shear: det = 1",
                "color": YELLOW_C
            },
            {
                "matrix": [[2, 1], [1, 1]],
                "desc": "General transformation: det = 1",
                "color": MAROON_C
            }
        ]
        
        for t in transformations:
            # Clear previous transformed vectors and parallelogram
            self.play(
                FadeOut(area_label),
                FadeOut(det_label),
                FadeOut(unit_square),
                FadeOut(i_label),
                FadeOut(j_label)
            )
            
            # Calculate the transformed basis vectors
            matrix = np.array(t["matrix"])
            new_i = matrix[:, 0]  # First column
            new_j = matrix[:, 1]  # Second column
            det_value = np.linalg.det(matrix)
            
            # Create transformed basis vectors
            transformed_i = Vector(new_i, color=RED)
            transformed_j = Vector(new_j, color=GREEN)
            
            # Label the transformed basis vectors
            i_label = MathTex(r"T(\vec{i})").next_to(transformed_i.get_end(), DOWN)
            j_label = MathTex(r"T(\vec{j})").next_to(transformed_j.get_end(), LEFT)
            
            # Create parallelogram representing transformed unit square
            # Ensure all vertices are proper 3D arrays for Manim
            parallelogram = Polygon(
                np.array([0, 0, 0]), 
                np.array([new_i[0], new_i[1], 0]), 
                np.array([new_i[0] + new_j[0], new_i[1] + new_j[1], 0]), 
                np.array([new_j[0], new_j[1], 0]),
                color=t["color"],
                fill_opacity=0.3
            )
            
            # Display matrix
            matrix_tex = MathTex(
                r"T = \begin{bmatrix} " + 
                f"{t['matrix'][0][0]} & {t['matrix'][0][1]} \\\\ " +
                f"{t['matrix'][1][0]} & {t['matrix'][1][1]}" +
                r"\end{bmatrix}"
            ).to_corner(UL)
            
            # Display description
            desc_text = Text(t["desc"], font_size=24).to_edge(UP)
            
            # Display area
            area_label = MathTex(r"\text{Area} = " + f"{abs(det_value):.2f}").next_to(desc_text, DOWN)
            det_label = MathTex(r"\det(T) = " + f"{det_value:.2f}").next_to(area_label, DOWN)
            
            # Animate the transformation
            self.play(
                Transform(vec_i, transformed_i),
                Transform(vec_j, transformed_j),
                Write(matrix_tex)
            )
            self.play(
                Write(i_label),
                Write(j_label),
                Create(parallelogram)
            )
            self.play(
                Write(desc_text),
                Write(area_label),
                Write(det_label)
            )
            
            # If determinant is negative, indicate orientation change
            if det_value < 0:
                orientation_text = Text("Orientation Reversed", color=RED, font_size=24).to_edge(DOWN)
                self.play(Write(orientation_text))
                self.wait(1)
                self.play(FadeOut(orientation_text))
            else:
                self.wait(1)
            
            # Clean up for next transformation
            self.play(FadeOut(matrix_tex), FadeOut(desc_text))
        
        # Final explanation
        conclusion = VGroup(
            Text("The determinant of a transformation matrix:", font_size=30),
            Text("• Gives the area scaling factor", font_size=24),
            Text("• Sign indicates orientation change", font_size=24),
            Text("• |det| < 1: Area contracts", font_size=24),
            Text("• |det| > 1: Area expands", font_size=24),
            Text("• det = 0: Area collapses (vectors become linearly dependent)", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DOWN).shift(UP)
        
        self.play(
            FadeOut(parallelogram),
            FadeOut(area_label),
            FadeOut(det_label),
            FadeOut(i_label),
            FadeOut(j_label)
        )
        self.play(Write(conclusion), run_time=2)
        self.wait(2)