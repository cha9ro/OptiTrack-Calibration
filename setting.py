##########################################
# If corresponding point set is already got
# (If it's the first time, set 'False')
PointsAlreadyGot = False

# Resolution of projection window
WIDTH = 1920
HEIGHT = 1080

# Projection screen size [mm]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Distance between projector and projection screen [mm]
FOCAL_LENGTH = 1300

# Top-left image position of projection window
Ox = 1920
Oy = 0

# Name of rigidbody used for calibration object
CALIB_OBJ = 'CalibObj'

# Directory Name (This is added to the end of the each file name ex: camera_matrixDIR_NAME.txt )
DIR_NAME = 'TEST'

# File names of the parameters (output)
EXTENSION = '.txt'
CAMERA_MATRIX_FILENAME = DIR_NAME + '/' + \
    'camera_matrix' + DIR_NAME + EXTENSION
TVECS_FILENAME = DIR_NAME + '/' + 'tvecs' + DIR_NAME + EXTENSION
RVECS_FILENAME = DIR_NAME + '/' + 'rvecs' + DIR_NAME + EXTENSION
EXTRINSIC_FILENAME = DIR_NAME + '/' + 'extrinsic' + DIR_NAME + EXTENSION
DIST_FILENAME = DIR_NAME + '/' + 'dist_coefs' + DIR_NAME + EXTENSION
RETVAL_FILENAME = DIR_NAME + '/' + 'retval' + DIR_NAME + EXTENSION
TVEC_WORLD_FILENAME = DIR_NAME + '/' + 'tWorld' + DIR_NAME + EXTENSION

# File names of the input data
IMG_INPUT_FILE = DIR_NAME + '/' + 'imgInput' + DIR_NAME + EXTENSION
OBJ_INPUT_FILE = DIR_NAME + '/' + 'objInput' + DIR_NAME + EXTENSION
##########################################
