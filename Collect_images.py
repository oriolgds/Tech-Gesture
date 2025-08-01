#!/usr/bin/env python
# coding: utf-8

# # Importing libraries

# In[1]:


import cv2  #opencv
import os
import time
import uuid
import sys
import threading

import classes

# ## Setting up the path

# In[2]:


IMAGES_PATH = 'datasets/coco/images'

# ### Generating array from abecedary

# In[3]:


#abecedary = "s"
#labels = [*abecedary]

#labels.append('guerra')
#labels.append('querer')
#labels.append('techgesture')
labels = ['paz']
#labels = ['techgesture']
print(labels)
number_imgs = 50
waitTime = 0.3
firstWaitTime = 3


# ### Useful functions

# In[4]:


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Folder '{path}' created successfully.")
    else:
        print(f"Folder '{path}' already exists.")


# In[5]:


create_dir(IMAGES_PATH)

# In[6]:


cap = cv2.VideoCapture(0)


# ### Capture code

# In[7]:
def camera_window():
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) == ord('w'):
            break
    cap.release()
    cv2.destroyAllWindows()


camera_thread = threading.Thread(target=camera_window)
camera_thread.start()

for label in labels:
    label = label.lower()
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Collecting for {}'.format(label), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2,
                    cv2.LINE_AA)
        cv2.putText(frame, 'Press q', (0, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    print('Collecting images for {}'.format(label))
    time.sleep(firstWaitTime)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        timestamp = time.time()
        imgname = os.path.join(IMAGES_PATH, label + '.' + '{}.jpg'.format(str(timestamp)))
        print(imgname)
        cv2.imshow('frame', frame)
        time.sleep(waitTime)
        cv2.imshow('frame', frame)
        cv2.imwrite(imgname, frame)

# #### Closing

# In[8]:


cap.release()
cv2.destroyAllWindows()

# In[ ]:
