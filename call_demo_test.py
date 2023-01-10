import argparse, os, shutil

def read_folder(folder_path: str):
    img_list = os.listdir(folder_path)
    #count = 0
    all_img_abs = []
    for img in img_list:
        if img.endswith("jpg"):
            #print(folder_path + "\\"+ img)
            img_abs_path = folder_path + "\\"+ img
            all_img_abs.append(img_abs_path)
    #print(all_img_abs)
    all_img_abs_string = ' '.join(all_img_abs)
    #print(all_img_abs_string)
    path = "python demo_img.py --images " + all_img_abs_string + " --checkpoint-path ./pretrained_model/checkpoint_iter_370000.pth"
    #print(img_list)
    #count += 1
    #print(path)
    os.system(path)
    #print(count)

def dir_path(string) -> str:
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def main(folder_path: str):
    read_folder(folder_path)

def check_tmp_folder(folder_path: str) -> None:
    tmp_folder_path = folder_path + "_tmp"   
    for folder in list(os.walk(tmp_folder_path)) :
        if not os.listdir(folder[0]):
            os.removedirs(folder[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=dir_path, help='path to input image(s) folder')
    args = parser.parse_args()
    #path = "./6"
    main(args.folder)
    check_tmp_folder(args.folder)