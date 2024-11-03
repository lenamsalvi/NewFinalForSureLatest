import tkinter as tk

WIDTH = 600
HEIGHT = 400
DEFAULT_FONT = ("Helvetica", 16)


def main():
    # Main setup
    root = tk.Tk()
    root.title("Autonomous Landscape Design")
    root.geometry(f"{WIDTH}x{HEIGHT}")

    # Content structure
    content_frame = tk.Frame(root, highlightbackground="white", highlightthickness=2)
    content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    content_frame_label = tk.Label(
        content_frame, text="Content Frame Label", font=DEFAULT_FONT
    )
    content_frame_label.pack(pady=20)

    # Controls struture
    control_frame = tk.Frame(root, highlightbackground="white", highlightthickness=2)
    control_frame.pack(side=tk.BOTTOM, fill=tk.X)

    control_frame_label = tk.Label(
        control_frame, text="Control Frame Label", font=DEFAULT_FONT
    )
    control_frame_label.pack(pady=20)

    control_frame_button = tk.Button(
        control_frame, text="Button", command=lambda: print("Button clicked")
    )
    control_frame_button.pack(side=tk.BOTTOM, padx=10, pady=10)

    # Main loop
    root.mainloop()


if __name__ == "__main__":
    main()
