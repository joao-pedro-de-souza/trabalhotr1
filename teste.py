import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Tkinter Selector Example")

# Define the callback function for the selector
def on_select(event):
    selected_item = combo.get()
    print(f"Selected: {selected_item}")

# Create a label
label = ttk.Label(root, text="Choose an option:")
label.pack(pady=10)

# Create a dropdown menu (combobox)
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
combo = ttk.Combobox(root, values=options, state='readonly')  # Set state to 'readonly'
combo.pack(pady=10)

# Bind the selection event to the callback function
combo.bind("<<ComboboxSelected>>", on_select)

# Set default value (optional)
combo.set("Select an option")

# Run the Tkinter event loop
root.mainloop()
