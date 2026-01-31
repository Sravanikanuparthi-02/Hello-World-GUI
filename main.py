import tkinter as tk

class HelloWorldApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello World - MCA Project")
        self.geometry("500x300")
        self.configure(bg="#ffffff")  # White background for clean look

        # Build UI
        self._create_widgets()

    def _create_widgets(self):
        # --- Navbar style header ---
        header = tk.Frame(self, bg="#333333", height=50)
        header.pack(fill="x")

        title = tk.Label(header, text="My Website Style GUI",
                         font=("Arial", 14, "bold"), fg="white", bg="#333333")
        title.pack(side="left", padx=20, pady=10)

        # --- Main content area ---
        content = tk.Frame(self, bg="#ffffff")
        content.pack(expand=True, fill="both")

        self.label = tk.Label(content, text="Welcome to Hello World GUI Project",
                              font=("Helvetica", 18, "bold"), fg="#333333", bg="#ffffff")
        self.label.pack(pady=40)

        # Styled button (like a web button)
        hello_button = tk.Button(content, text="Say Hello",
                                 command=self._say_hello,
                                 font=("Arial", 12, "bold"),
                                 bg="#232635", fg="white",
                                 activebackground="#45a049",
                                 relief="flat", padx=20, pady=10)
        hello_button.pack(pady=10)

        # --- Footer ---
        footer = tk.Frame(self, bg="#f1f1f1", height=30)
        footer.pack(fill="x", side="bottom")

        footer_label = tk.Label(footer, text="© 2026 GUI Project",
                                font=("Arial", 10), fg="#555555", bg="#f1f1f1")
        footer_label.pack(pady=5)

    def _say_hello(self):
        self.label.config(text="🌐 Hello, World!")

if __name__ == "__main__":
    app = HelloWorldApp()
    app.mainloop()
