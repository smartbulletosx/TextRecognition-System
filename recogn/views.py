# coding=utf-8
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

import os
import shutil
import sys
import time

import cv2
import numpy as np
import tensorflow as tf
import pytesseract as pt




def index(request):
    if request.method == 'POST':
        try:
            myfile = request.FILES['myfile']
        except:
            return render(request, 'res.html', {'res' :'Error, file wasn\'t found. Please go back and chose file'})
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        tf.app.run()
        res1 = open('result.txt','rb')
        res = res1.read()
        res1.close()
        os.remove('result.txt')
        return render(request,'res.html', {'res':res.decode('utf-8')})
    return render(request, 'index.html')

