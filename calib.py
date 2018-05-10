import numpy as np
import cv2
import natnetclient as natnet
from setting import *

# Global variables
n = 0
imgInp = []
objInp = []
# File name
IMG_INPUT_FILE = "imgInput.txt"
OBJ_INPUT_FILE = "objInput.txt"

def main():
    if not PointsAlreadyGot:
        # create img
        whiteImg = np.zeros((HEIGHT, WIDTH, 3), dtype = np.uint8)
        whiteImg.fill(255)

        # create window
        WINDOW_NAME = "window" # window name
        cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(WINDOW_NAME, whiteImg)
        cv2.moveWindow(WINDOW_NAME, Ox, Oy)
        cv2.setMouseCallback(WINDOW_NAME, onMouse)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # write input file
        writeInput(IMG_INPUT_FILE, imgInp)
        writeInput(OBJ_INPUT_FILE, objInp)

    # read input files
    imgPoints = readData(IMG_INPUT_FILE)
    objPoints = readData(OBJ_INPUT_FILE)

    # convert to vector of vector
    imgPoints = np.array(imgPoints, "float32")
    objPoints = np.array(objPoints, "float32")

    # camera calibrate
    camera_matrix = np.zeros((3,3), "float32")
    dist_coefs = np.zeros(4,"float32")
    rvecs = np.zeros(3, "float32")
    tvecs = np.zeros(3, "float32")
    size = (WIDTH, HEIGHT)
    camera_matrix[0][0] = 1600
    camera_matrix[1][1] = 1600
    camera_matrix[0][2] = 1000
    camera_matrix[1][2] = 500
    camera_matrix[2][2] = 1
    retval,camera_matrix,dist_coefs,rvecs,tvecs = cv2.calibrateCamera([objPoints],[imgPoints],size,camera_matrix,dist_coefs, flags = cv2.CALIB_USE_INTRINSIC_GUESS)

    f = open("retval.txt", "w")
    f.write(str(retval))
    f.close()
    f = open("camera_matrix.txt", "w")
    for i in range(3):
        for j in range(3):
            f.write(str(camera_matrix[i][j]) + ',')
        f.write('\n')
    f.close()
    f = open("dist_coefs.txt", "w")
    for i in range(len(dist_coefs)):
        f.write(str(dist_coefs[i]) + ',')
    f.close()
    f = open("rvecs.txt", "w")
    for i in range(len(rvecs)):
        f.write(str(rvecs[i]) + ',')
    f.close()
    f = open("tvecs.txt", "w")
    for i in range(len(tvecs)):
        f.write(str(tvecs[i]) + ',')
    f.close()

    #################
    print("retval")
    print(retval)
    print("camera_matrix")
    print(camera_matrix)
    print("dist_coefs")
    print(dist_coefs)
    print("rvecs")
    print(rvecs)
    print("tvecs")
    print(tvecs)
    #################

def writeInput(fileName, array):
    f = open(fileName, "w")
    for i in range(len(array)):
        for j in range(len(array[0])):
            f.write(str(array[i][j]) + ',')
        f.write('\n')
    f.close()

def readData(fileName):
    # initialize array to store info in
    array = []

    # read file
    f = open(fileName, "r")
    data = f.read()
    f.close()

    # store in array
    data = data.split('\n')
    data.remove('')
    for line in data:
        points = line.split(',')
        points.remove('')
        inp_temp = []
        for point in points:
            inp_temp.append(float(point))
        array.append(inp_temp)

    return array

def onMouse(event, x, y, flags, param):
    global n
    if event == cv2.EVENT_LBUTTONDOWN:
        n += 1
        calibObjPos = getObjPos(CALIB_OBJ)
        imgInp.append([x, y])
        objInp.append(calibObjPos)
        print (n, "(x,y)=(%d,%d), (X,Y,Z)=(%f,%f,%f)" % (x,y,calibObjPos[0], calibObjPos[1], calibObjPos[2]))

def getObjPos(ObjName):
    client = natnet.NatClient(client_ip = '127.0.0.1', data_port = 1511, comm_port = 1510)
    obj = client.rigid_bodies[ObjName]
    objPos = [val * 1000 for val in obj.position] # [m] -> [mm]
    return objPos


if __name__ == '__main__':
    main()