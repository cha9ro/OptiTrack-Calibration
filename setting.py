##########################################
# If corresponding point set is already got
# (If it's the first time, set 'False')
PointsAlreadyGot = False

# Resolution of projection window
WIDTH = 1920
HEIGHT = 1080

# Projection screen size [mm]
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Distance between projector and projection screen [mm]
FOCAL_LENGTH = 1300

# Top-left image position of projection window
Ox = 3840 # + 1200 #+ 3840
Oy = 0

# Name of rigidbody used for calibration object
CALIB_OBJ = 'CalibObj'

# Directory Name (This is added to the end of the each file name ex: camera_matrixDIR_NAME.txt )
DIR_NAME = '4KStereo'

# File names of the parameters (output)
CAMERA_MATRIX_FILENAME = DIR_NAME + '/' + 'camera_matrix' + DIR_NAME + '.txt'
TVECS_FILENAME = DIR_NAME + '/' + 'tvecs' + DIR_NAME + '.txt'
RVECS_FILENAME = DIR_NAME + '/' + 'rvecs' + DIR_NAME + '.txt'
EXTRINSIC_FILENAME = DIR_NAME + '/' + 'extrinsic' + DIR_NAME + '.txt'
DIST_FILENAME = DIR_NAME + '/' + 'dist_coefs' + DIR_NAME + '.txt'
RETVAL_FILENAME = DIR_NAME + '/' + 'retval' + DIR_NAME + '.txt'
TVEC_WORLD_FILENAME = DIR_NAME + '/' + 'tWorld' + DIR_NAME + '.txt'

# File names of the input data
IMG_INPUT_FILE = DIR_NAME + '/' + 'imgInput' + DIR_NAME + '.txt'
OBJ_INPUT_FILE = DIR_NAME + '/' + 'objInput' + DIR_NAME + '.txt'
##########################################