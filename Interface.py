import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("DS Diagrams")
root.geometry("400x300")

# Create a frame for the fixed upper section
topFrame = tk.Frame(root, height=80, bg="lightgray",relief="solid",borderwidth="2")
topFrame.pack(fill="x", side="top")

# Create a frame for the left section
leftFrame = tk.Frame(root, width=600, bg="lightgray",relief="solid",borderwidth="2")
leftFrame.pack(fill="y", side="left")

# Example content for the fixed frame (e.g., a label)
leftFrame = tk.Label(leftFrame, text="Permanent left Section", bg="lightgray")
leftFrame.pack(pady=20)

# Example content for the fixed frame (e.g., a label)
topFrame = tk.Label(topFrame, text="Permanent Upper Section", bg="lightgray")
topFrame.pack(pady=20)

# Create a frame for the scrollable lower section
verticalScroll = tk.Frame(root)
verticalScroll.pack(fill="both", expand=True, side="bottom")

# Add a canvas to enable scrolling
verticalCanvas = tk.Canvas(verticalScroll)
verticalCanvas.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the canvas
v_scrollbar = ttk.Scrollbar(verticalScroll, orient="vertical", command=verticalCanvas.yview)
v_scrollbar.pack(side="right", fill="y")

# Configure the canvas to work with the scrollbar
verticalCanvas.configure(yscrollcommand=v_scrollbar.set)
verticalCanvas.bind('<Configure>', lambda e: verticalCanvas.configure(scrollregion=verticalCanvas.bbox("all")))

# Create another frame inside the canvas (this will be scrollable)
vScroll_content = tk.Frame(verticalCanvas)

# Add the scrollable content frame to the canvas
verticalCanvas.create_window((0, 0), window=vScroll_content, anchor="nw")

for i in range(20):
    tk.Label(vScroll_content, text=f"Scrollable Item {i+1}").pack(pady=10)

# Run the application
root.mainloop()