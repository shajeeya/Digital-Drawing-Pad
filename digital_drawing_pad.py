
import tkinter as tk
from tkinter import messagebox


class DigitalDrawingPad:

    def __init__(self, root):

        self.root = root
        self.root.title("Digital Drawing Pad")
        self.root.geometry("1000x700")
        self.root.minsize(750, 550)
        self.root.configure(bg="#F0F3F8")

        # Drawing variables
        self.selected_color = "black"
        self.brush_size = 5
        self.eraser_mode = False

        self.previous_x = None
        self.previous_y = None

        # Header
        header = tk.Label(
            root,
            text="DIGITAL DRAWING PAD",
            font=("Arial", 24, "bold"),
            bg="#E8EEF7",
            fg="#233047",
            pady=18
        )
        header.pack(fill=tk.X)

        # Toolbar
        toolbar = tk.Frame(
            root,
            bg="#E8EEF7",
            pady=15
        )
        toolbar.pack(fill=tk.X)

        # Color buttons
        colors = [
            ("Red", "red"),
            ("Blue", "blue"),
            ("Green", "green"),
            ("Black", "black"),
            ("Yellow", "yellow")
        ]

        for name, color in colors:

            button = tk.Button(
                toolbar,
                text=name,
                font=("Arial", 10, "bold"),
                fg=color,
                bg="white",
                width=8,
                command=lambda c=color, n=name:
                    self.select_color(c, n)
            )

            button.pack(side=tk.LEFT, padx=5)

        # Brush size label
        tk.Label(
            toolbar,
            text="Brush Size:",
            font=("Arial", 11, "bold"),
            bg="#E8EEF7"
        ).pack(side=tk.LEFT, padx=(15, 5))

        # Brush thickness slider
        self.size_slider = tk.Scale(
            toolbar,
            from_=1,
            to=30,
            orient=tk.HORIZONTAL,
            length=130,
            bg="#E8EEF7",
            command=self.change_size
        )

        self.size_slider.set(5)
        self.size_slider.pack(side=tk.LEFT)

        # Eraser button
        eraser_button = tk.Button(
            toolbar,
            text="Eraser",
            font=("Arial", 10, "bold"),
            bg="white",
            width=9,
            command=self.use_eraser
        )
        eraser_button.pack(side=tk.LEFT, padx=5)

        # Clear canvas button
        clear_button = tk.Button(
            toolbar,
            text="Clear Canvas",
            font=("Arial", 10, "bold"),
            bg="#FCE4E4",
            fg="#B22222",
            command=self.clear_canvas
        )
        clear_button.pack(side=tk.LEFT, padx=5)

        # Drawing canvas
        self.canvas = tk.Canvas(
            root,
            bg="white",
            cursor="cross",
            highlightthickness=2,
            highlightbackground="#BCC8D8"
        )

        self.canvas.pack(
            fill=tk.BOTH,
            expand=True,
            padx=20,
            pady=15
        )

        # Mouse events
        self.canvas.bind(
            "<Button-1>",
            self.start_drawing
        )

        self.canvas.bind(
            "<B1-Motion>",
            self.draw
        )

        self.canvas.bind(
            "<ButtonRelease-1>",
            self.stop_drawing
        )

        # Status bar
        self.status = tk.Label(
            root,
            text="Ready to draw!",
            font=("Arial", 10),
            bg="#DCE4F0",
            fg="#233047",
            anchor="w",
            padx=15,
            pady=8
        )

        self.status.pack(fill=tk.X)

    # Select drawing color
    def select_color(self, color, name):

        self.selected_color = color
        self.eraser_mode = False

        self.status.config(
            text=name + " color selected"
        )

    # Adjust brush thickness
    def change_size(self, value):

        self.brush_size = int(float(value))

        self.status.config(
            text="Brush size: " + str(self.brush_size)
        )

    # Activate eraser
    def use_eraser(self):

        self.eraser_mode = True
        self.status.config(text="Eraser selected")

    # Start drawing
    def start_drawing(self, event):

        self.previous_x = event.x
        self.previous_y = event.y

    # Freehand drawing
    def draw(self, event):

        if self.previous_x is not None:

            color = "white" if self.eraser_mode else self.selected_color

            self.canvas.create_line(
                self.previous_x,
                self.previous_y,
                event.x,
                event.y,
                fill=color,
                width=self.brush_size,
                capstyle=tk.ROUND,
                smooth=True
            )

        self.previous_x = event.x
        self.previous_y = event.y

    # Stop drawing
    def stop_drawing(self, event):

        self.previous_x = None
        self.previous_y = None

    # Clear entire canvas
    def clear_canvas(self):

        self.canvas.delete("all")

        self.status.config(
            text="Canvas cleared"
        )


# Main program
if __name__ == "__main__":

    root = tk.Tk()

    app = DigitalDrawingPad(root)

    root.mainloop()
