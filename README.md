# Guess the States in India Game

This is an interactive game to test your knowledge of the states in India. The goal is to name all 29 states. When you guess a state correctly, it will be marked on the map of India.

## Features

- Interactive map of India
- Text input for guessing state names
- Displays guessed states on the map
- Saves the list of states you missed for further learning

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Shubham-44/guess-the-states-in-india.git
    ```

2. **Install dependencies**:
    Make sure you have Python installed. Then, install the necessary packages:
    ```sh
    pip install pandas turtle
    ```

3. **Add the image and data files**:
    Make sure you have the `India_state.gif` image and `states_data.csv` file in the same directory as your script. The `states_data.csv` file should contain the state names along with their x and y coordinates on the map.

## How to Play

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Guess the states**:
    - A map of India will appear.
    - Enter the name of a state in the text box.
    - Correct guesses will be marked on the map.
    - Type "Exit" to end the game early. A CSV file named `Learning_States.csv` will be generated, listing the states you missed.

## Data Format

The `states_data.csv` file should have the following structure:

```csv
state,x,y
Andhra Pradesh,100,200
Karnataka,120,220
...
