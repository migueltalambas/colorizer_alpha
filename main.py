from colorizer import *

colorizer = Colorizer(use_cuda=True, width = 640, height = 480)

colorizer.processImage("uploads\charlie_chaplin.jpg")

#colorizer.processVideo("videos/casablanca_12345.mp4")