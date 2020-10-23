# Rock Paper Scissors Game via Webcam(Using resnet50 architecture)

## Overview
The following code is a rock paper scissors game that can be played with your webcam. The object detection is does by the resent50 model(parts of the weights are frozen) combined with a fully connected layer.

## How to use the code

First Install the weights for the neural network from this [link](https://drive.google.com/file/d/1jk7SzT4poHpG8FY3TTdqasLeMFSfvmOg/view?usp=sharing) and put in the current repository directory.

Then Run

```
python play.py
```

## Demo
![](https://github.com/jvkamnani/Rock_Paper_Scissor/blob/main/demo/RPS_demo.gif)

## Datasets
[Train Data](https://drive.google.com/drive/folders/17JB4yHeC2_Vw37QUarwfMlXcVte4w143?usp=sharing)

[Validation Data](https://drive.google.com/drive/folders/1l_6quvVydbhYL7sr8LdWz27BwHOhsdry?usp=sharing)

## Depenendencies
```
    -numpy
    -tensorflow
    -opencv
    -imutils
    -shutil
```
## Training with your Own Data

To train with your own data put the data in the training and validation folder and then type.
```
python train.py
```

## Generating data from webcam
To generate data using the webcam run get_data_from_webcam.py and follow the instructions on the screen.
```
python get_data_from_webcam.py
```

## Move and Split Data
To move the data from the webcam folder run move.py. It put's 9-% of the data into the training folder and 10% into the validation folder.

```
python move.py
```
