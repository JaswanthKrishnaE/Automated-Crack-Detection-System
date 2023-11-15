# Automated Crack Detection System

## Overview
This project focuses on recognizing diseases in guava fruits using a convolutional neural network. It utilizes a custom model with a convolutional architecture to classify different disease classes.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Folder Structure](#folder-structure)
6. [Dataset](#dataset)
5. [Results](#results)

## Introduction
Cracks in walls represent a serious concern for the structural stability of buildings, and their early detection is crucial to prevent further damage and costly repairs. Traditional methods, like manual inspections, are not only time-consuming but also subjective, relying on human judgment and susceptible to errors.

In response to these challenges, our project introduces an innovative solution through an automated crack detection system. By leveraging object detection and classification techniques, we aim to enhance the efficiency and accuracy of crack identification in building structures.

The system not only detects cracks but also distinguishes them from other common surface irregularities, such as scratched paint. This distinction is essential for prioritizing and addressing structural concerns effectively.

The advantages of our automated approach include rapid detection, reduced reliance on human judgment, and the potential for real-time monitoring. As we advance towards a safer and more sustainable built environment, this technology serves as a valuable tool in ensuring the longevity and integrity of buildings.

## Installation
To set up the project, follow these steps:

### 1. Create a Virtual Environment
```bash
# open your project directory and Create a virtual environment
python -m venv venv
```
### 2. Activate the virtual environment
```ash 
# On Windows
venv\Scripts\activate
```
```bash
# On macOS/Linux
source venv/bin/activate
```
### 3. Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
## Usage
To use the trained model through laptop camera 
```bash
python main.py
```
## Folder Structure

The project is organized with the following folder structure:

- **Automated Crack Detection System.pptx**: Presentation slides for the ICPS project.

- **main.py**: The main Python script that executes the crack detection system.

- **models**: Directory containing saved models or model-related files.

- **myenv**: Virtual environment directory to isolate project dependencies.

- **notebooks**: Directory for Jupyter notebooks used for analysis or testing.

- **README.md**: The main documentation file providing an overview of the project, its purpose, and how to use it.

- **requirements.txt**: File listing project dependencies for easy installation.

- **test images**: Directory containing images used for testing or evaluation.

- **test.ipynb**: Jupyter notebook for testing or demonstrating specific functionalities.

## Dataset

- [Wall Crack Detection Dataset](https://app.roboflow.com/indian-institute-of-information-technology-sricity/wall-crack-detection-drpsp/1)
  - Description: This dataset includes images for wall crack detection.

- [Wall Crack Classification Dataset](https://app.roboflow.com/indian-institute-of-information-technology-sricity/wall-crack-classification/3)
  - Description: This dataset includes images for wall crack detection.

## Results

The results of the crack detection system, along with detailed insights and visualizations, are presented in the [Automated Crack Detection System](https://github.com/JaswanthKrishnaE/Automated-Crack-Detection-System/blob/jaswanth/Automated%20Crack%20Detection%20System.pptx). Please refer to the slides for a comprehensive overview of the project outcomes.

## Trained Models
The trained models are stored in the `models` directory. These models have been fine-tuned to accurately classify different types of surface irregularities, including cracks and scratched paint.

Feel free to explore the presentation slides and the `models` directory for a deeper understanding of the project results.

