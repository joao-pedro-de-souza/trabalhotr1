import tkinter as tk
import math
import random


def draw_center_lines():
    # Get the current width and height of the canvas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Calculate the center of the canvas
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    
    # Draw the horizontal center line
    canvas.create_line(0, center_y, canvas_width, center_y, fill='black', width=2)
    
    # Draw the vertical center line
    canvas.create_line(center_x, 0, center_x, canvas_height, fill='black', width=2)

    
def on_resize(event):
    # Get the new width and height of the canvas
    canvas_width = root.winfo_width()
    canvas_height = root.winfo_height()
    

    canvas.config(width=canvas_width, height=canvas_height)
    
    # Redraw the sine wave with the new canvas size
    draw_sine_wave()

def draw_sine_wave():
    canvas.delete("all")
    amplitude = 100 + 50 * random.random()  # Amplitude of the sine wave
    frequency = 0.05*random.random()   # Frequency of the sine wave
    offset = canvas.winfo_height() // 2
    widht=canvas.winfo_width() 
    if offset==0:
        offset=200
        widht=150
    points = []
    NoiseAmp=[]
    for x in range(int ((widht/2)-50)):
        rand=10 * random.random()
        y = (amplitude * math.sin(frequency * x)*canvas.winfo_height()/1000 + offset + rand)-canvas.winfo_height()/4
        n=x+10
        noiseamp=(amplitude * math.sin(frequency * x)+rand)
        NoiseAmp.append(noiseamp)
        points.append((n, y))
    
    # Flatten the list of points into a single list of coordinates
    noise = [coord for point in points for coord in point]
    
    amplitude = 100 # Amplitude of the sine wave
    frequency = 0.1  # Frequency of the sine wave
    offset = canvas.winfo_height() // 2
    widht=canvas.winfo_width() 
    if offset==0:
        offset=200
        widht=150
    Wave = []
    WaveAmp=[]
    for x in range(int ((widht/2)-50)):
        y = ((amplitude * math.sin(frequency * x)*canvas.winfo_height()/1000 + offset))+canvas.winfo_height()/5
        waveamp=(amplitude * math.sin(frequency * x))
        WaveAmp.append(waveamp)
        n=x+10
        Wave.append((n, y))
    
    # Flatten the list of points into a single list of coordinates
    wave = [coord for point in Wave for coord in point]

    reciever = []
    offset = canvas.winfo_height() // 2
    widht=canvas.winfo_width() 
    if offset==0:
        offset=200
        widht=150
    for x in range(int((len(wave))/2)):
        y = ((NoiseAmp[x]+WaveAmp[x])*canvas.winfo_height()/2000 + offset)+canvas.winfo_height()/5

        n=x+10+canvas.winfo_width() // 2
        reciever.append((n, y))
    
    # Flatten the list of points into a single list of coordinates
    reciever = [coord for point in reciever for coord in point]
    # Draw the sine wave
    canvas.create_line(noise, fill='blue', smooth=True)
    canvas.create_line(wave, fill='blue', smooth=True)
    canvas.create_line(reciever, fill='blue', smooth=True)
def update_time():
    draw_sine_wave()
    draw_center_lines()
    root.after(1000, update_time)

# Create the main application window
root = tk.Tk()
root.title("Sine Wave")

# Set an initial size for the window
root.geometry("400x300")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=300, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the resize event to the on_resize function
root.bind("<Configure>", on_resize)

# Start the time update loop
update_time()

# Start the Tkinter event loop
root.mainloop()
