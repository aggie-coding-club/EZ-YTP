# EZ-YTP

## Description

EZ YTP is a tool meant to ease the creation of youtube poops by automating the process of sentence mixing. 
The goal is to make it so you can upload a video and some text. The app will then automatically splice the 
video so that the result reads the specified text. This is currently a work in progress.

## Install Instructions

Prerequisites: If you don't have these already download the following:
* Python -- https://www.python.org/downloads/
* Docker -- https://docs.docker.com/get-docker/

1) Clone the github repository to your computer.
2) Navigate to the root folder `EZ-YTP` in the terminal and create a virtual environment. You can do this by running `python3 -m venv .venv` on windows or `source venv/bin/activate` on mac.
    * Activate the virtual environment by running `./venv/Scripts/activate`. If you get an error telling you that you don't have permission to do this run the command again but with admin privileges. You will need to activate the virtual environment anytime you want to work on the project.
    * What the virtual environment does is isolate our project. This helps us make sure we are using the same Python and package versions and also prevents cross contamination with dependencies in other Python projects.
3) Install the python packages we are going to be using for the project by running `pip install -r requirements.txt`.
4) Download the Docker image for Gentle Forced Aligner by running `docker pull lowerquality/gentle` in your terminal.
5) Build a Docker container using the image. To do this, open Docker Desktop and navigate to `Images` tab. Find the `lowerquality/gentle` image. Click `RUN`. This should create a pop-up. Click `Optional Settings` and  give `Local Host` a value of `8765`. Then click `RUN`. Navigate to the `Containers/Apps` tab. You should see your newly created container running. Feel free to stop it. 

## Running Instructions
1) Activate the python virtual environment if it isn't already. You can do this by navigating to the root folder `EZ-YTP` in the terminal and running `./venv/Scripts/activate`on windows or `source venv/bin/activate` on mac.
2) Start running the docker container if it isn't already. You can do this by opening Docker Desktop and navigating to the `Containers/Apps` tab. Then finding the container you created during installation and clicking the run button.
3) At the moment there are only two things that run, `app.py` and `docker_api.py`.
    * `docker_api.py` will call the api for gentle. This takes in an audio file and a transcript. It returns JSON containing information about the phonemes. To run the script run `python docker_api.py` in the terminal within the `src` directory.
    * `app.py` is honestly pretty much a place holder right now. It just returns a webpage containing Hello World. To run it, run `python app.py` in the terminal within the `src` directory. If you want to navigate to the page go to `localhost:5000` while it is running. To stop running the script, press `Ctrl + C` in the terminal.
