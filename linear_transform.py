from manim import *

class LinearTransformationScene2D(Scene):
    def construct(self):
        # Set up axes
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-3, 3],
            x_length=8,
            y_length=6,
            tips=False,
            axis_config={"include_numbers": True}
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")
        self.play(Create(axes), Write(labels))

        # Add a square for reference
        square = Polygon(
            axes.c2p(0, 0),
            axes.c2p(1, 0),
            axes.c2p(1, 1),
            axes.c2p(0, 1),
            color=BLUE
        )
        self.play(Create(square))
        matrix = Matrix([[1, 1], [0, 1]])
        matrix.to_corner(UL)  # position at top-left

        self.play(Write(matrix))
        # Define transformation matrix
        matrix = [[1, 1], [0, 1]]  # Shear transformation

        # Apply transformation
        transformed_square = square.copy()
        transformed_square.apply_matrix(matrix)

        # Animate the transformation
        self.play(Transform(square, transformed_square))
        self.wait()
