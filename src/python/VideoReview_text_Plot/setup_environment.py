from google.colab import drive
import os
from os import listdir
from os.path import isfile, join

import pandas as pd

drive.mount("/content/gdrive")
os.chdir("/content/gdrive/MyDrive/ReviewVideoSummarization")