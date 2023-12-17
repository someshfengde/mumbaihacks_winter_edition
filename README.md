# StyleSynth - MumbaiHacks Winter Edition 2023

## Introduction

Welcome to StyleSynth, a Flutter application with a Flask backend that leverages the power of Fashion GAN to find similar fashion items. This submission is for the MumbaiHacks Winter Edition 2023 hackathon.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Demo Video](#demo-video)
4. [Backend](#backend)
5. [Frontend](#frontend)
6. [Getting Started](#getting-started)
7. [Dependencies](#dependencies)


## Overview

StyleSynth is a fashion recommendation application that utilizes a Flask backend with a Fashion GAN (Generative Adversarial Network) to find similar fashion items from a dataset. The frontend, built with Flutter, offers a clean and intuitive user interface for a seamless user experience.

## Features

- **Fashion GAN Integration**: Powered by a backend server using Fashion GAN with a Flask API, StyleSynth finds similar fashion items based on the input image.
  
- **ResNet50 Backbone**: The Fashion GAN model is trained with a ResNet50 backbone, enhancing its ability to identify and recommend similar products effectively.

- **Clean UI**: The Flutter frontend provides a visually appealing and user-friendly interface, ensuring a smooth and enjoyable interaction for users.

## Demo Video
https://github.com/someshfengde/mumbaihacks_winter_edition_2023/assets/42097653/49ec7fa5-3dea-401f-8d95-f391747c7582

Check out our demo video to see StyleSynth in action. This video showcases the application's features, including image input, recommendation generation, and the overall user experience.


## Backend

The backend is implemented using Flask, providing a robust API for communication with the Fashion GAN model. The Fashion GAN backend is responsible for processing image inputs, extracting features using ResNet50, and finding similar fashion items from the dataset.

## Frontend

The Flutter frontend offers a clean and intuitive UI for users to interact with StyleSynth. Users can upload images of fashion items by either selecting them from their gallery ir clicking them on the go, and the application will provide recommendations based on the Fashion GAN backend.

## Getting Started

To run the StyleSynth application locally, follow these steps:

1. Clone the repository: `git clone git@github.com:someshfengde/mumbaihacks_winter_edition_2023.git`
2. Navigate to the project directory: `cd mumbaihacks_winter_edition_2023`
3. Install dependencies for the backend and frontend.
4. Configure the Flask backend to connect with the Fashion GAN model.
5. Run the Flutter application on your preferred device or emulator.

## Dependencies

- Flask
- Flutter
- Fashion GAN
- ResNet50
- find other dependencies in the `pip_requirements.txt` and `pubspec.yaml` files. 
