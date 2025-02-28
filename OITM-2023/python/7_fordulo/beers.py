from pathlib import Path
from fastbook import *
from fastai.vision.widgets import *
import pickle
import pathlib

# Betöltjük a modellt
plt = platform.system()
if plt == 'Linux' or plt == "Darwin":
    pathlib.WindowsPath = pathlib.PosixPath

learn_inf = load_learner('export.pkl')

# Azonosítjuk a képeket
image_files = get_image_files('.')

# Összegyűjtjük a korsót ábrázoló képek azonosító számait
sum_of_ids = 0
for image_file in image_files:
    # Előrejelzés a képre
    pred, pred_idx, probs = learn_inf.predict(image_file)
    #print(image_file.name, pred, probs[pred_idx])
    # Ha a kép egy korsót ábrázol, hozzáadjuk az azonosító számát az összeghez
    if pred == 'glass_small':
        id = int(image_file.name.split('_')[1].split('.')[0])
        sum_of_ids += id

print("Az összeg: ", sum_of_ids)
