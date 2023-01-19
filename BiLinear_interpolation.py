from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math
import cv2
import os
import argparse

def dir_path(string) -> str:
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

all_img_abs = []

def read_folder(folder_path: str):
    img_list = os.listdir(folder_path)
    #count = 0
    for img in img_list:
        if img.endswith("jpg") or img.endswith("png"):
            #print(folder_path + "\\"+ img)
            img_abs_path = folder_path + "\\" + img
            all_img_abs.append(img_abs_path)
    #print(all_img_abs)
    return all_img_abs


def setup_bilinear_folder(folder_path) -> None:
    bilinear_folder_path = folder_path + "_bilinear"
    
    if not os.path.exists(bilinear_folder_path):
        os.makedirs(bilinear_folder_path)
    else:
        print("file exists")


def setup_bilinear_gamma_folder(folder_path) -> None:
    bilinear_folder_path = folder_path + "_bilinear_gamma"
    
    if not os.path.exists(bilinear_folder_path):
        os.makedirs(bilinear_folder_path)
    else:
        print("file exists")
    

def BiLinear_interpolation(img,dstH,dstW):
    scrH,scrW,_=img.shape
    img=np.pad(img,((0,1),(0,1),(0,0)),'constant')
    retimg=np.zeros((dstH,dstW,3),dtype=np.uint8)
    for i in range(dstH):
        for j in range(dstW):
            scrx=(i+1)*(scrH/dstH)-1
            scry=(j+1)*(scrW/dstW)-1
            x=math.floor(scrx)
            y=math.floor(scry)
            u=scrx-x
            v=scry-y
            retimg[i,j]=(1-u)*(1-v)*img[x,y]+u*(1-v)*img[x+1,y]+(1-u)*v*img[x,y+1]+u*v*img[x+1,y+1]
    return retimg

def BiLinear_img_save(path_list: list):
    for path in path_list:
        head, img_name = os.path.split(path)
        save_path = head + "_bilinear" + "\\" + img_name
        #print(save_path)
        
        image=np.array(Image.open(path))

        image=BiLinear_interpolation(image,image.shape[0]*2,image.shape[1]*2)
        image=Image.fromarray(image.astype('uint8')).convert('RGB')
        #print(image)
        image.save(save_path)


def gamma_transfer(forder_path):
    #print(forder_path)
    bilinear_forder_path = forder_path + "_bilinear"
    path_list = os.listdir(bilinear_forder_path)
    for path in path_list:
        print(path)
        head, img_name = os.path.split(path)
        save_path = head + "_bilinear_gamma" + "\\" + img_name
        
        #abs_path = os.path.abspath(path)
        #print(abs_path)
        #img = cv2.imread(path)
        #print(img)
        '''
        if len(img.shape) == 3:
            img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = 255*np.power(img/255, 1.5)
        img = np.around(img)
        img[img>255] = 255
        out_img = img.astype(np.uint8)
        cv2.imwrite(save_path, out_img)
        '''



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Lightweight human pose estimation python demo.
                       This is just for quick results preview.
                       Please, consider c++ demo for the best performance.''')
    parser.add_argument('--folder', type=dir_path, help='path to input image(s) folder')
    args = parser.parse_args()

    setup_bilinear_folder(args.folder)
    all_img_abs = read_folder(args.folder)
    BiLinear_img_save(all_img_abs)
    #setup_bilinear_gamma_folder(args.folder)
    #gamma_transfer(args.folder)
    

    '''
    im_path='defaultPrimary-1_streamType_u3.jpg'
    image=np.array(Image.open(im_path))

    image=BiLinear_interpolation(image,image.shape[0]*2,image.shape[1]*2)
    image=Image.fromarray(image.astype('uint8')).convert('RGB')
    #print(image)
    image.save('BiLinear_interpolation_sharpen_output.jpg')
    '''