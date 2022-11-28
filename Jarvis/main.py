from Jarvis.utils.BaseFunctionality import greetings, welcome, get_location
from gui.gui import create_gui

"""
This project is aiming to be a home monitor with voice control

# Currently available: 
    Voice to Text convert
    Weather check
    Text to Speech
# TODO: 
    2. Semantic Analysis (To get rid off stupid key word detection) 
    3. Classify the text into tasks or just random talk (two weeks)
    4. Build the Sensors for Temperature, Moisture, Sound, Light intensity
    5. Read info from surrounding env (...)
    6. Data Processing for the surrounding env data 
    7. Build House Model (IDK what to do with it but just list here first )
    8. Smart Control lights .... and other products based on the surrounding env (like turning on the light)
    9. Build Docker Image (This is aiming for make this project published)
    10. Image Processing
        a. Capture the front door visual
        b. Face detection and Recognising (simple classification should be fine)
        c. Height and weight prediction
    11. NLP:
        a. The system should be able to understand different languages
        b. Slice the voice into different layers (background sound, user voice) 
        c. Analysis the voice frequency of the users (To know who is controlling, better access control)
    More can be added later on 
          
"""

city = "Wellington"
country = "nz"
RECONIZEDTEXT = ""


if __name__ == "__main__":
    welcome()
    # greetings()
    # create_gui()
