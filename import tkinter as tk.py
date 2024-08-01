import tkinter as tk

# Global variable to store slider value
slider_value = tk.DoubleVar()  # Use DoubleVar for float values, IntVar for integer values

def update_slider_value(value):
    """ Update the slider_value global variable with the slider's current value """
    slider_value.set(float(value))  # Set the value of the global variable

def print_slider_value():
    """ Print the current value of the slider_value variable """
    print(f"Current slider value: {slider_value.get()}")

# Create the main application window
root = tk.Tk()
root.title("Slider Example")

# Set an initial size for the window
root.geometry("300x150")

# Create a slider widget
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_slider_value)
slider.pack(pady=20)

# Create a button to print the slider value
button = tk.Button(root, text="Print Slider Value", command=print_slider_value)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
