# Tkinter Wave simulator

This Python application uses Tkinter to create a graphical user interface for generating and visualizing waves. The application includes sliders to adjust the frequency, amplitude, and offset of the noise, which updates dynamically on a canvas.

## Features

- **Adjustable Sine Wave Parameters:**
  - **Frequency:** Adjust the frequency of the sine wave using a slider.
  - **Amplitude:** Adjust the amplitude (height) of the sine wave.
  - **Offset:** Adjust the vertical offset of the sine wave.

- **Dynamic Updates:** The sine wave redraws dynamically as the sliders are adjusted or the window is resized.

- **Center Lines:** Used to to diferentiate the noise the bitstream and the resulting reciever wave
## Installation

Ensure you have Python installed. You can run the application directly using the provided script if you have Python 3.x and tkinter installed.

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using Python:

    ```sh
    python sine_wave_generator.py
    ```

4. Adjust the sliders to change the frequency, amplitude, and offset of the sine wave.
5. The sine wave will update on the canvas based on the slider values.

## Code Overview

### Global Variables

- `Freq_value`, `Amp_value`, `Offset_value`: `tk.DoubleVar()` instances that store the current values of the sliders.

### Functions

- **`update_Freq(value)`**: Updates the frequency label and value, then redraws the sine wave.
- **`update_Amp(value)`**: Updates the amplitude label and value, then redraws the sine wave.
- **`update_Offset(value)`**: Updates the offset label and value, then redraws the sine wave.
- **`draw_center_lines()`**: Draws horizontal and vertical center lines on the canvas.
- **`on_resize(event)`**: Handles window resizing and updates slider positions and canvas.
- **`draw_sine_wave()`**: Draws the sine wave based on current slider values.
- **`update_time()`**: Updates the canvas with the latest slider values.

### Tkinter Widgets

- **Canvas**: The area where the sine wave is drawn.
- **Sliders**: Allow users to adjust the wave's frequency, amplitude, and offset.
- **Labels**: Display the current slider values.

## Example

When the application runs, you will see three sliders for adjusting the frequency, amplitude, and offset of the sine wave. As you move each slider, the sine wave on the canvas updates to reflect the new values. The center lines on the canvas help visualize the wave's position.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Tkinter documentation and resources for building the GUI.
- Math and random libraries for generating the sine wave and noise.

Feel free to modify and enhance this application as needed. Enjoy experimenting with sine waves!
