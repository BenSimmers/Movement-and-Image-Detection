# Movement-and-Image-Detection
Image and movement detection in python using multiple python libraries


## Libraries Needed

For testing_motion_coords.py:

```
from typing import Counter, ItemsView
import cv2
import numpy as np
from numpy.lib.polynomial import roots
import pandas as pd
from tkinter import *
from collections import Counter
from openpyxl import *
```

For testing_motion.py
```
import cv2, time, pandas
from datetime import datetime
```

For translator.py
```
from tkinter import *
from PIL import ImageTk, Image #will need pip install
from tkinter import filedialog
from pytesseract import pytesseract #will need pip install
from googletrans import Translator #will need pip install
```

## What are These??
```
These programs were developed as a fun personal project and to learn something new and cool
```
```
Both programs act very similar to one another. One file will track the x and y coordinates of
whatever is moving in camera view.
```
```
The other file will use multiple camera windows to track movements based on timestamps. Each timestamp
is recorded when movement is detected.
```
```
The final file translator.py primarily focuses on image detection and determining readable text.
```

## What can they be used for??
Not much at the moment</br>
However, in theory if there is enough of the correct analysis is made towards the data, an assessment could be made focusing on movement of people and objects.
