import tkinter as tk
from enum import Enum

WH_SCALE = 0.6
DEFAULT_FONT = ("Helvetica", 16)


class PaletteOptions(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
    WHITE = "WHITE"
    BLACK = "BLACK"
    GRAY = "GRAY"


class LandscapeDesignApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Auto-scale window based on screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = int(screen_width * WH_SCALE)
        window_height = int(screen_height * WH_SCALE)
        window_x_pos = (screen_width - window_width) // 2
        window_y_pos = (screen_height - window_height) // 2

        # Main window setup
        self.title("Autonomous Landscape Design")
        self.geometry(f"{window_width}x{window_height}+{window_x_pos}+{window_y_pos}")

        # Build UI components
        self.create_content_frame()
        self.create_control_frame()

    def create_content_frame(self):
        self.content_frame = tk.Frame(
            self, highlightbackground="white", highlightthickness=2
        )
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        content_frame_label = tk.Label(
            self.content_frame, text="Content Frame Label", font=DEFAULT_FONT
        )
        content_frame_label.pack(pady=20)

    def create_control_frame(self):
        self.control_frame = tk.Frame(
            self, highlightbackground="white", highlightthickness=2
        )
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        control_frame_label = tk.Label(
            self.control_frame, text="Control Frame Label", font=DEFAULT_FONT
        )
        control_frame_label.pack(pady=20)

        button_frame = tk.Frame(self.control_frame)
        button_frame.pack(anchor="center")

        for color in PaletteOptions:
            control_frame_button = tk.Button(
                button_frame,
                text=f"Change to {color.name}",
                command=lambda color=color: self.generate_palette(color),
            )
            control_frame_button.pack(side=tk.LEFT, padx=10, pady=10)

    def generate_palette(self, color):
        self.content_frame.config(bg=color.value)
        print(f"# TEST - Generate a {color.name} palette")


if __name__ == "__main__":
    app = LandscapeDesignApp()
    app.mainloop()
