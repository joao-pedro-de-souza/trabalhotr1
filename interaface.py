import tkinter as tk
import math
import random
def functset():
    string=textbox.get("1.0", tk.END).strip()
    Noisefunction.set(string)
    print(Noisefunction.get())
    noise_type.set(False)
    draw_sine_wave()
def parsefunction(x,numeroPontos):
    n=[]
    amp=0
    openbrackets=False
    sum=False
    alredy=False
    offset=""
    freq=0
    for i in range(len(x)):
        cahr =x[i]
        if x[i].isnumeric() and openbrackets==False:
            if amp!=0:
                amp=(10*amp)+int(x[i])
                if x[i-2]=="-":
                    amp=amp*-1
            else:
                amp=int(x[i])
                if i!=0:
                    if x[i-1]=="-" and x[i+1].isnumeric()!=True:
                        amp=amp*-1
        elif x[i]=="c":
            if amp==0:
                amp=1
            function="cos"
        elif x[i]=="e":
            if amp==0:
                amp=1
            function="sen"
        elif x[i]=="(":
            openbrackets=True
        elif x[i]==")" and i!=len(x)-1:
            if freq==0:
                freq=1
            openbrackets=False
            sum=False
            alredy=False
        elif x[i]=="p":
            if x[i-1].isnumeric():
                offset=3.14*int(x[i-1])
            else:
                offset=3.14
        elif x[i].isnumeric()==True and openbrackets==True and (x[i+1]=="x" or x[i+1].isnumeric() )and alredy==False and sum==False:
            j=1
            freq=int(x[i])
            while x[i+j].isnumeric() :
                alredy=True
                freq=freq*10+int(x[i+j])
                j=j+1
        elif x[i]=='+' and openbrackets==True:
            sum=True
        elif x[i].isnumeric()==True and sum==True:
            if offset=="":
                offset=int(x[i])
            else:
                offset=(10*offset)+int(x[i])
        elif( (x[i]=="+" or x[i]=="-") and openbrackets==False) or (i==(len(x)-1)):
            if freq==0:
                freq=1
            n.append({"amp":amp,"freq":freq,"offset":offset,"function":function})
            num=0
            amp=0
            openbrackets=False
            sum=False
            offset=""
            freq=0
    print(n)
    wave=functionvalue(x=numeroPontos,function=n)
    return wave
def num(x,function):
    table=[]
    for i in range(x):
        if function["offset"]=="":
            function["offset"]=0
        if function["function"]=="cos":
            y=math.cos((i*function["freq"]/100)+function["offset"])*function["amp"]*10

            table.append(y)
        else:
            y=math.sin((i*function["freq"]/100)+function["offset"])*function["amp"]*10
            table.append(y)
    return table    
def functionvalue(x,function):
    Table=[]
    results=[]
    result=0
    Results=[]
    for i in range(len(function)):
        table=num(x,function=function[i])
        Table.append(table)
    for i in range(x):
        result=0
        for j in range(len(Table)):

            result=Table[j][i]+result
        results.append(result)
        
    for i in range(len(results)):
        Results.append(results[i])
    return Results
def update_Freq(value):
    """ Update the label with the current slider  """
    Freq_var.set(f"Frequencia")
    Freq_value.set(value)
    noise_type.set(True)
    draw_sine_wave()
def update_Amp(value):
    """ Update the label with the current slider  """
    Amp_var.set(f"Amplitude")
    Amp_value.set(value)
    noise_type.set(True)
    draw_sine_wave()
def update_Offset(value):
    """ Update the label with the current slider  """
    Offset_var.set(f"offset")
    Offset_value.set(value)
    noise_type.set(True)
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
    #sliders
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
    #button
    textbox.place(x=sliderFreq_x,y=sliderFreq_y+190)
    sendButton.place(x=sliderFreq_x,y=sliderFreq_y+220)

    canvas.create_text(sliderFreq_x+15, sliderFreq_y - 15,text="Noise",font=("Helvetica", min(canvas_width, canvas_height) // 1000),fill="black",tags="text")
def draw_sine_wave():
    canvas.delete("lines")
    if noise_type.get()==True:
        freq=int(Freq_value.get())
        amp=int(Amp_value.get())
        Offset=int(Offset_value.get())
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
    else:
        offset = canvas.winfo_height() // 2
        widht=canvas.winfo_width() 
        if offset==0:
            offset=200
            widht=150
        points = []
        NoiseAmp=[]
        primalWave=parsefunction(x=Noisefunction.get(),numeroPontos=int ((widht/2)-50,))  
        for x in range((int ((widht/2)-50))):
                y = ((primalWave[x]*canvas.winfo_height()/1000 + offset))-canvas.winfo_height()/4
                noiseamp=(primalWave[x])
                NoiseAmp.append(noiseamp)
                n=(x+10)
                points.append((n, y))
    # Flatten the list of points into a single list of coordinates
#    noise = [coord for point in points for coord in point]
       # Draw the sine wave 

    Wave=[]
  
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

    canvas.create_line(points, fill='blue', smooth=True,tags="lines")
#   canvas.create_line(wave, fill='blue', smooth=True,tags="lines")
#    canvas.create_line(reciever, fill='blue', smooth=True,tags="lines")
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
##Creating the box for the noise function
Noisefunction=tk.StringVar()
textbox=tk.Text(width=30,height=1)
sendButton=tk.Button(text="send",command=functset)
noise_type=tk.BooleanVar()
noise_type.set(True)
## Creating the bitstream typing 
Bitstream=tk.StringVar()
Bitstream_textBox=tk.Text()
Bitstream_sendButton=tk.Button()
##Creating the selectors da camada fisica
draw_center_lines()
update_time()

# Start the Tkinter event loop
root.mainloop()
