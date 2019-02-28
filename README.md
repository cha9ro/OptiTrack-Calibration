# OptiTrack-Calibration
Projector calibration with Motive by OptiTrack for Unity.
Mostly used for projection mapping system.

## Instllation
- Install Python 3 (and pip)
- Install opencv-python and NatNetClient
    ```
    pip install opencv-python
    pip install NatNetClient
    ```

## How to use
1. Make sure OptiTrack's IR emitter/cameras are connected.

1. Enter the required information about your system in ```setting.py```
    - ```PointsAlreadyGot```: Set ```False``` if you haven't got any data. Only if you want to compute the parameter based on the data you got in advance, set ```True```.
    - ```WIDTH, HEIGHT```: Resolution of projection image [pixel]
    - ```SCREEN_WIDTH, SCREEN_HEIGHT```: The approximate size of the projected screen/target [mm]
    - ```FOCAL_LENGTH```: The approximate distance between the projector and projected screen [mm]
    - ```Ox, Oy```: The upper-left position of the projection window [pixel].
    - ```CALIB_OBJ```: The name of calibration object registered as rigidbody in Motive
    - ```DIR_NAME```: Directory name in which the computed data is saved. This ```DIR_NAME``` is added to the each file name, i.g. ```camera_matrixDIR_NAME.txt```

1. Run ```calib.py```.
    ```
    python calib.py
    ```

1. Move the cursor and CalibObj so that the cursor and CalibObj's center overlap, at which left click. When the coordinates pair is successfully saved it shows the saved coordinates. Otherwise it shows "CalibObj is missing."

1. Get corresponding pairs as many as 20.

1. Hit any keys to compute the projector parameters.
