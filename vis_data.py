# script helpful for visualizing the data points
import copy
import cv2
import os
from IPython import embed

# input
root_path = './data'


# visualize action
def vis_action(img, start, end):
    """
    center is at middle of image with X axis pointing downward (V) and Y axis pointing right -->
    :param img: img of shape [w,h,c]
    :param start: np array of len 2(x,y) in range(-1,1), normalized start image location
    :param end: np array of len 2(x,y) in range(-1,1), normalized stop image location
    :return: img
    """
    cv2.arrowedLine(img, (start[1], start[0]), (end[1], end[0]), (0, 255, 0), 4)
    return img


lines = open(os.path.join(root_path, 'data.txt'), "rb").readlines()

for line in lines:
    word = line[:-1].split('\t')
    start_img = cv2.imread(os.path.join(root_path, word[0]))
    end_img = cv2.imread(os.path.join(root_path, word[1]))

    start_pt = (int(word[2]), int(word[3]))
    end_pt = (int(word[4]), int(word[5]))
    start_img_with_action = copy.deepcopy(start_img)
    cv2.arrowedLine(start_img_with_action, start_pt, end_pt, (0, 255, 0), 4)

    cv2.imshow("start_img", start_img_with_action)
    cv2.moveWindow("start_img", 40, 488)

    cv2.imshow("end_img", end_img)
    cv2.moveWindow("end_img", 440, 488)
    cv2.waitKey(0)

