import numpy as np
import cv2
import pathlib
import os, shutil

overOnebbox = False

def check_one_box(bboxes_count):
    global overOnebbox
    if bboxes_count > 1:
        overOnebbox = True
    else:
        overOnebbox = False


def setup(path_list: list) -> None:
    for path in path_list:
        abs_path = os.path.abspath(path)
        head, img_name = os.path.split(abs_path)
        grandparent_folder_abspath, folder = os.path.split(head)
        other_folder_path = grandparent_folder_abspath + "\\" + folder + "_tmp" + "\\"

        if not os.path.exists(other_folder_path + 'Front'):
            os.makedirs(other_folder_path + 'Front')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Front_Left'):
            os.makedirs(other_folder_path + 'Front_Left')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Front_Right'):
            os.makedirs(other_folder_path + 'Front_Right')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Side_Left'):
            os.makedirs(other_folder_path + 'Side_Left')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Side_Right'):
            os.makedirs(other_folder_path + 'Side_Right')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Back'):
            os.makedirs(other_folder_path + 'Back')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Back_Left'):
            os.makedirs(other_folder_path + 'Back_Left')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Back_Right'):
            os.makedirs(other_folder_path + 'Back_Right')
        else:
            print("file exists")
        if not os.path.exists(other_folder_path + 'Others'):
            os.makedirs(other_folder_path + 'Others')
        else:
            print("file exists")
        

def grouping_method(path_list: list, image_data_list: list) -> None:
    global overOnebbox
    for path, image_data in zip(path_list, image_data_list):
        abs_path = os.path.abspath(path) 
        head, img_name = os.path.split(abs_path)
        grandparent_folder_abspath, folder = os.path.split(head)
        other_folder_path = grandparent_folder_abspath + "\\" + folder + "_tmp" + "\\"

        if overOnebbox == False:
            if (len(image_data)) == 18:
                if (np.all(image_data[:, 0] > 0)):
                    destination_path = other_folder_path + "Front"
                    shutil.copy(abs_path, destination_path) 
                    print("Front")
                if (image_data[0][0]) > 0 and (image_data[16][0]) < 0:
                    if (image_data[14][0]) < 0:
                        destination_path = other_folder_path + "Side_Left"
                        shutil.copy(abs_path, destination_path)  
                        print("Side_Left")
                    else:
                        destination_path = other_folder_path + "Front_Left"
                        shutil.copy(abs_path, destination_path)                     
                        print("Front_Left")

                if (image_data[0][0]) > 0 and (image_data[17][0]) < 0:
                    if (image_data[15][0]) < 0:
                        destination_path = other_folder_path + "Side_Right"
                        shutil.copy(abs_path, destination_path) 
                        print("Side_Right")
                    else:
                        destination_path = other_folder_path + "Front_Right"
                        shutil.copy(abs_path, destination_path)
                        print("Front_Right")
                if (image_data[0][0]) < 0 and (image_data[14][0]) < 0 and (image_data[15][0]) < 0:
                    #print(image_data[2,:])
                    #print(image_data[5,:])
                    if (image_data[5,:][1] - image_data[2,:][1])/(image_data[5,:][0] - image_data[2,:][0]) < 0: 
                        if abs(image_data[5,:][1] - image_data[2,:][1]) <= 5 or abs(image_data[5,:][0] - image_data[2,:][0]) <= 5:
                            destination_path = other_folder_path + "Back"
                            shutil.copy(abs_path, destination_path)
                            print("Back")
                        else:
                            destination_path = other_folder_path + "Back_Left"
                            shutil.copy(abs_path, destination_path)
                            print("Back_Left")
                    if (image_data[5,:][1] - image_data[2,:][1])/(image_data[5,:][0] - image_data[2,:][0]) > 0:
                        if abs(image_data[5,:][1] - image_data[2,:][1]) <= 5 or abs(image_data[5,:][0] - image_data[2,:][0]) <= 5:
                            destination_path = other_folder_path + "Back"
                            shutil.copy(abs_path, destination_path)
                            print("Back")
                        else:
                            destination_path = other_folder_path + "Back_Right"
                            shutil.copy(abs_path, destination_path)
                            print("Back_Right")
            else:
                print("The number of body points in human pose should be 18 (Openpose 18 keypoints)!")
        else:
            destination_path = other_folder_path + "Others"
            shutil.copy(abs_path, destination_path)  
            print("Can't over one bbox!")

    
    









