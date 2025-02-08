#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_red(rgb_image):
    
    r_weight=np.array([1,0,0]).reshape(1,1,3)#[[[1,0,0]]]
    red=rgb_image*r_weight
    return red

def to_green(rgb_image):
    
    g_weight=np.array([0,1,0]).reshape(1,1,3)#[[[1,0,0]]]
    green=rgb_image*g_weight
    return green

def to_blue(rgb_image):
    
    b_weight=np.array([0,0,1]).reshape(1,1,3)#[[[1,0,0]]]
    blue=rgb_image*b_weight
    return blue

def to_grayscale(rgb_image):
    
    weight=[0.2126,0.7152,0.0722]
    grey=np.dot(rgb_image,weight)
    return grey



def main():
    rgb_image=plt.imread("src/painting.png")
    
    grey=to_grayscale(rgb_image)
    plt.imshow(grey,cmap='gray')
    plt.show()
    
    red=to_red(rgb_image)
    green=to_green(rgb_image)
    blue=to_blue(rgb_image)
    
    fig,ax=plt.subplots(3,1)
    ax[0].imshow(red)
    ax[1].imshow(green)
    ax[2].imshow(blue)
    plt.show()
    

if __name__ == "__main__":
    main()
