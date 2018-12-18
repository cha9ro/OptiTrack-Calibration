import numpy as np
import cv2
import natnetclient as natnet
from setting import *

# Global variables
n = 0
imgInp = []
objInp = []


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
    # Initialize the parameters
    camera_matrix[0][0] = FOCAL_LENGTH/(SCREEN_WIDTH/WIDTH)
    camera_matrix[1][1] = FOCAL_LENGTH/(SCREEN_HEIGHT/HEIGHT)
    camera_matrix[0][2] = WIDTH/2
    camera_matrix[1][2] = HEIGHT/2
    camera_matrix[2][2] = 1

    ######## values before computation##############
    print("-----initial parameters-----")
    # print("retval")
    # print(retval)
    print("camera_matrix")
    print(camera_matrix)
    print("dist_coefs")
    print(dist_coefs)
    print("rvecs")
    print(rvecs)
    print("tvecs")
    print(tvecs)
    print("-----input data-----")
    print("objPoints")
    print(objPoints)
    print("imgPoints")
    print(imgPoints)
    print("-----------------")
    ################################################

    # Calculate the parameters
    retval,camera_matrix,dist_coefs,rvecs,tvecs = cv2.calibrateCamera([objPoints], [imgPoints], size, camera_matrix, dist_coefs, flags = cv2.CALIB_USE_INTRINSIC_GUESS)

    # Write file of extrinsic parameters (R matrix)
    R = np.zeros((3,3), dtype=np.float32)
    rvec = np.array([rvecs[0][0], rvecs[0][1], -rvecs[0][2]], dtype=np.float32)
    cv2.Rodrigues(rvec, R)

    # t_world: translate vector based on world coordinate
    Rinv = np.linalg.inv(R)
    t_world = np.dot(Rinv, tvecs[0])

    # Extrinsic paramters (R|t)
    r = np.zeros(3, dtype=np.float32)
    R = np.concatenate([R, [r]])
    tvec = np.array([tvecs[0][0], tvecs[0][1], -tvecs[0][2], 1], dtype=np.float32)
    tvec = np.transpose([tvec])
    Rt = np.concatenate([R, tvec], axis=1)


    # write files of np array (directly from OpenCV parameters)
    f = open(RETVAL_FILENAME, "w")
    f.write(str(retval))
    f.close()
    np.savetxt(CAMERA_MATRIX_FILENAME, camera_matrix, fmt = '%.08f', delimiter = ',', newline = '\n')
    np.savetxt(TVECS_FILENAME, tvecs[0], fmt = '%.08f', delimiter=',', newline='\n')
    np.savetxt(RVECS_FILENAME, rvecs[0], fmt = '%.08f', delimiter=',', newline='\n')
    np.savetxt(DIST_FILENAME, dist_coefs, fmt = '%.08f', delimiter=',', newline='\n')

    np.savetxt(EXTRINSIC_FILENAME, Rt, fmt = '%.08f', delimiter=',', newline='\n')
    np.savetxt(TVEC_WORLD_FILENAME, t_world, fmt = '%.08f', delimiter=',', newline='\n')

    ####### check the computed values ##########
    print("retval")
    print(retval)
    print("camera_matrix")
    print(camera_matrix)
    print("dist_coefs")
    print(dist_coefs)
    print("rvecs")
    print(rvecs[0])
    print("tvecs")
    print(tvecs[0])
    print("extrinsic")
    print(Rt)
    ############################################

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
        calibObjPos = getObjPos(CALIB_OBJ)
        if calibObjPos != None:
            n += 1
            imgInp.append([x, y])
            objInp.append(calibObjPos)
            print (n, "(x,y)=(%d,%d), (X,Y,Z)=(%f,%f,%f)" % (x,y,calibObjPos[0], calibObjPos[1], calibObjPos[2]))
        else:
            print ('CalibObj is not tracked')

def getObjPos(ObjName):
    client = natnet.NatClient(client_ip = '127.0.0.1', data_port = 1511, comm_port = 1510)
    obj = client.rigid_bodies[ObjName]
    if obj.seen:
        x = obj.position[0]
        y = obj.position[1]
        z = obj.position[2]
        objPos = [x, y, z] # make a line
        return objPos
    else:
        return None


if __name__ == '__main__':
    main()