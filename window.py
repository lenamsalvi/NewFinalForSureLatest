import tkinter as tk

WIDTH = 600
HEIGHT = 400
DEFAULT_FONT = ("Helvetica", 16)


class LandscapeDesignApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Main window setup
        self.title("Autonomous Landscape Design")
        self.geometry(f"{WIDTH}x{HEIGHT}")

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

        control_frame_button = tk.Button(
            self.control_frame, text="Button", command=self.on_button_click
        )
        control_frame_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    def on_button_click(self):
        print("Button clicked")


if __name__ == "__main__":
    app = LandscapeDesignApp()
    app.mainloop()
