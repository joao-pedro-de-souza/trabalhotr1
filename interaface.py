import tkinter as tk
import math
import random


def update_Freq(value):
    """ Update the label with the current slider  """
    Freq_var.set(f"Frequencia")
    Freq_value.set(value)
    draw_sine_wave()
def update_Amp(value):
    """ Update the label with the current slider  """
    Amp_var.set(f"Amplitude")
    Amp_value.set(value)
    draw_sine_wave()

def update_Offset(value):
    """ Update the label with the current slider  """
    Offset_var.set(f"offset")
    Offset_value.set(value)
    draw_sine_wave()

def draw_center_lines():
    # Get the current width and height of the canvas
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    # Calculate the center of the canvas
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    
    # Draw the horizontal center line
    canvas.create_line(0, center_y, canvas_width, center_y, fill='black', width=2,tags="center_lines")
    
    # Draw the vertical center line
    canvas.create_line(center_x, 0, center_x, canvas_height, fill='black', width=2,tags="center_lines")

    
def on_resize(event):
    # Get the new width and height of the canvas
    canvas_width = root.winfo_width()
    canvas_height = root.winfo_height()
    

    canvas.config(width=canvas_width, height=canvas_height)
    
    # Redraw the sine wave with the new canvas size
    draw_sine_wave()
    canvas.delete("center_lines")
    canvas.delete("text")
    draw_center_lines()
    slider_length = canvas_width * 0.2  # Slider length as a fraction of the canvas width
    sliderFreq.config(length=int(slider_length))
    sliderFreq_x = ((canvas_width) // 2)+10
    sliderFreq_y = 20  
    sliderFreq.place(x=sliderFreq_x, y=sliderFreq_y+20)
    labelFreq.place(x=sliderFreq_x, y=sliderFreq_y+5) 

    sliderAmp.config(length=int(slider_length))
    sliderFreq_x = ((canvas_width) // 2)+10
    sliderFreq_y = 20  
    sliderAmp.place(x=sliderFreq_x, y=sliderFreq_y+80)
    Amp.place(x=sliderFreq_x, y=sliderFreq_y+65)  
    
    slideOffset.config(length=int(slider_length))
    sliderFreq_x = ((canvas_width) // 2)+10
    sliderFreq_y = 20  
    slideOffset.place(x=sliderFreq_x, y=sliderFreq_y+140)
    Offset.place(x=sliderFreq_x, y=sliderFreq_y+125) 
    
    canvas.create_text(sliderFreq_x+15, sliderFreq_y - 15,text="Noise",font=("Helvetica", min(canvas_width, canvas_height) // 1000),fill="black",tags="text")

def draw_sine_wave():
    canvas.delete("lines")
    freq=int(Freq_value.get())
    amp=int(Amp_value.get())
    Offset=int(Offset_value.get())
    print(amp)
    amplitude = 100*amp/45# Frequency of the sine wave
    frequency = 0.05*(freq)/20 # Frequency of the sine wave
    offset = canvas.winfo_height() // 2
    widht=canvas.winfo_width() 
    if offset==0:
        offset=200
        widht=150
    points = []
    NoiseAmp=[]
    for x in range(int ((widht/2)-50)):
        rand=10 * random.random()
        y = (amplitude * math.sin((frequency * (x))+Offset)*canvas.winfo_height()/1000 + offset + rand)-canvas.winfo_height()/4
        n=x+10
        noiseamp=(amplitude * math.sin((frequency * (x))+Offset)+rand)
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
    canvas.create_line(noise, fill='blue', smooth=True,tags="lines")
    canvas.create_line(wave, fill='blue', smooth=True,tags="lines")
    canvas.create_line(reciever, fill='blue', smooth=True,tags="lines")
def update_time():
    draw_sine_wave()


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


##creating the sliders
width=int(canvas.winfo_width())
sliderFreq = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_Freq)
sliderFreq.place(x=width, y=20)
Freq_var = tk.StringVar()
Freq_var.set(f"Frequencia")
labelFreq = tk.Label(root, textvariable=Freq_var)
labelFreq.place(x=(canvas.winfo_width()/2)+100, y=20)
sliderAmp = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_Amp)
sliderAmp.place(x=width, y=20)
Amp_var = tk.StringVar()
Amp_var.set(f"Amplitude")
Amp = tk.Label(root, textvariable=Amp_var)
Amp.place(x=(canvas.winfo_width()/2)+100, y=20)
slideOffset = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_Offset)
slideOffset.place(x=width, y=20)
Offset_var = tk.StringVar()
Offset_var.set(f"Offset")
Offset = tk.Label(root, textvariable=Offset_var)
Offset.place(x=(canvas.winfo_width()/2)+100, y=20)
Amp_value=tk.DoubleVar()
Freq_value=tk.DoubleVar()
Offset_value=tk.DoubleVar()
draw_center_lines()
update_time()

# Start the Tkinter event loop
root.mainloop()
