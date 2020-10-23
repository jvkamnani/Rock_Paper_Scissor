import shutil
import random
import os

WORKING_DIRECTORY = os.getcwd()

SOURCE_URL = WORKING_DIRECTORY + '/pictures from webcam/'
SOURCE_ROCK_URL = SOURCE_URL + 'rock/'
SOURCE_SCISSOR_URL = SOURCE_URL + 'scissor/'
SOURCE_PAPER_URL = SOURCE_URL + 'paper/'

DESTINATION_VALID_URL = WORKING_DIRECTORY + '/valid_data/'
DESTINATION_VALID_ROCK_URL = DESTINATION_VALID_URL + 'rock/'
DESTINATION_VALID_SCISSOR_URL = DESTINATION_VALID_URL + 'scissor/'
DESTINATION_VALID_PAPER_URL = DESTINATION_VALID_URL + 'paper/'


DESTINATION_TRAIN_URL =  WORKING_DIRECTORY + '/train_data/'
DESTINATION_TRAIN_ROCK_URL = DESTINATION_TRAIN_URL + 'rock/'
DESTINATION_TRAIN_SCISSOR_URL = DESTINATION_TRAIN_URL + 'scissor/'
DESTINATION_TRAIN_PAPER_URL = DESTINATION_TRAIN_URL + 'paper/'


paper_files = os.listdir(SOURCE_PAPER_URL)
scissor_files = os.listdir(SOURCE_SCISSOR_URL)
rock_files = os.listdir(SOURCE_ROCK_URL)

random.shuffle(paper_files)
random.shuffle(scissor_files)
random.shuffle(rock_files)


train_val_split = 10 # for every 9 training images there will be 1 validation image 

for i in range(len(paper_files)):
    if i % train_val_split ==0:
        shutil.copyfile(SOURCE_PAPER_URL + paper_files[i], DESTINATION_VALID_PAPER_URL + paper_files[i])
    else:
        shutil.copyfile(SOURCE_PAPER_URL + paper_files[i], DESTINATION_TRAIN_PAPER_URL + paper_files[i])

for i in range(len(rock_files)):
    if i % train_val_split ==0:
        shutil.copyfile(SOURCE_ROCK_URL + rock_files[i], DESTINATION_VALID_ROCK_URL + rock_files[i])
    else:
        shutil.copyfile(SOURCE_ROCK_URL + rock_files[i], DESTINATION_TRAIN_ROCK_URL + rock_files[i])

for i in range(len(scissor_files)):
    if i % train_val_split ==0:
        shutil.copyfile(SOURCE_SCISSOR_URL + scissor_files[i], DESTINATION_VALID_SCISSOR_URL + scissor_files[i])
    else:
        shutil.copyfile(SOURCE_SCISSOR_URL + scissor_files[i], DESTINATION_TRAIN_SCISSOR_URL + scissor_files[i])