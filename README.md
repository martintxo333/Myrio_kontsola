# MyRIO Console Project

This project turns the **NI myRIO** device used in the *Industrial Informatics* course at the **University of the Basque Country (EHU)** into an **interactive game console**.

The goal of the project is to demonstrate practical knowledge of **Python**, **hardware interaction**, and **real-time input/output handling** using the sensors and peripherals available on the myRIO platform.

> **Original idea and implementation by:** Martin Maiz  
> **Academic purpose:** Evaluation of Python programming skills in the Industrial Informatics course

---

## Project Overview

The program transforms the NI myRIO into a small console featuring **four interactive mini-games**, all controlled through:

- Digital buttons
- RGB LED
- Light sensor
- Temperature sensor
- Accelerometer

A main menu allows the user to choose and replay games as many times as desired.

---

## Included Mini-Games

### Reflex Game
- A random RGB LED turns on and then off after a delay.
- The player must press a button **as fast as possible** once the LED turns off.
- Early presses are penalized.
- Best reaction time is stored as a record.
- 
---

### Light Guessing Game
- The myRIO light sensor measures ambient brightness (0–100%).
- The player must guess the correct value.
- Feedback is given using RGB LEDs:
  - 🔵 Too low
  - 🔴 Too high
  - 🟢 Correct
- Completion time is recorded.
  
---

### Temperature Guessing Game
- Similar to the light game, but using the temperature sensor.
- The player guesses the current temperature in °C.
- RGB LED feedback indicates whether the guess is too high or too low.
- Fastest correct attempt is stored.
  
---

### Skier Game (Accelerometer-Based)
- A reflex and coordination game controlled by **tilting the myRIO**.
- The player must tilt left or right to avoid obstacles.
- The allowed reaction time decreases every round.
- Incorrect tilt direction ends the game.
  
---

## Features

- Interactive main menu
- Real-time sensor interaction
- RGB LED visual feedback
- Reaction time measurement
- Score and record tracking
- Input validation and error handling
- Modular code structure using functions

---

## Requirements

- NI myRIO device
- Python environment compatible with myRIO
- `myrio_base` library
- Physical access to:
  - Buttons
  - RGB LED
  - Light sensor
  - Temperature sensor
  - Accelerometer

> **Hardware Note:**  
> The RGB LED, the two digital buttons, the temperature sensor, and the light sensor are **not built-in components of the NI myRIO**.  
> They belong to an **external MXP board designed by my teacher** and are connected to the **MXP Port A** of the myRIO device.

---

## How to Run

1. Connect the NI myRIO to your computer.
2. Ensure the `myrio_base` library is correctly installed.
3. Run the Python script:
   ```bash
   python Myrio_martin.py

---

## Academic Purpose
This project was developed as an original work to demonstrate understanding of:

- Python programming
- Hardware-software interaction
- Embedded systems logic
- Sensor data handling
- User-oriented program design
- 
---

## Author
Martin Maiz Negredo

---

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for license rights and limitations.
