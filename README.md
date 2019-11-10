# OptiTrack-Calibration
## English
### Abstract
Calibration program to compute intrinsic and extrinsic parameters of projector using OptiTrack System.

1. Input necessary parameters values in [`setting.py`](./setting.py).

1. Get correspondences between 2-dim point on projector window and 3-dim point in world coordinate.
2-dim point is obtained with mouse cursor and 3-dim point is measured by Motive, OptiTrack.

1. Using the correspondences above, the program calibrate projector with the core computation from OpenCV [`calibrateCamera`](https://docs.opencv.org/3.4.5/d9/d0c/group__calib3d.html#ga3207604e4b1a1758aa66acb6ed5aa65d).

### Preparation
- Install Python3 ([Reference](https://realpython.com/installing-python/)).
- Install Python modules `opencv-python` and `NatNetClient`.
    ```Bash
    pip install opencv-python
    pip install NatNetClient
    ```
- Install [Motive](https://optitrack.com/products/motive/) by OptiTrack.

### How to use
1. Make sure OptiTrack cameras are connected and recognized in Motive.

1. Enter the following parameters in [`setting.py`](./setting.py).
    - `PointsAlreadyGot`: Whether you already have correspondences (`boolean`).

    - `WIDTH, HEIGHT`: Projector resolution [pixel].
    
    - `SCREEN_WIDTH, SCREEN_HEIGHT`: Physical projected size [mm]. 
    They don't have to be very accurate.

    - `FOCAL_LENGTH`: Physical distance between projector and projected target [mm]. 
    They don't have to be very accurate.
    
    - `Ox, Oy`: The top-left position of the projection window on the running computer [pixel].
    
    - `CALIB_OBJ`: The name of calibration object registered in Motive.
    The calibration object needs to be registered in Motive as rigidbody for Motive to obtain 3-dim position and rotation.
    It is set as `CalibObj` as default.
    
    - `DIR_NAME`: Directory name in which the result is saved.
    This `DIR_NAME` is also used for each output files, e.g., `camera_matrix_DIR_NAME.txt` is an output file to store camera matrix.

1. Run [`calib.py`](./calib.py).
    ```bash
    python calib.py
    ```

1. Get correspondences if you set `PointsAlreadyGot` to `False` as follows;
    1. Move the mouse cursor onto the projection window.

    1. Move `CalibObj` and mouse cursor so their centers are both overlapped.

    1. Left-click. 
    It shows obtained 2-dim and 3-dim positions if it successes, otherwise it shows `CalibObj is missing`.

    1. Iterate the above procedures until getting around 20 correspondences.

    1. Enter an arbitrary key to start the computation.

1. The result are stored in `DIR_NAME`.



## 日本語
### 概要
プロジェクタのキャリブレーション（内部パラメータ・外部パラメータ）のプログラム。
大まかな処理の流れは以下の通り。
1. 必要なパラメータを [`setting.py`](./setting.py) 入力する。

1. プロジェクタウィンドウ上の二次元座標と世界三次元座標の対応点の組を取得する。
二次元座標はマウスカーソルで、三次元座標はOptiTrack社のMotiveで取得する。

1. 取得した対応点の組を用いてOpenCVの [`calibrateCamera`](https://docs.opencv.org/3.4.5/d9/d0c/group__calib3d.html#ga3207604e4b1a1758aa66acb6ed5aa65d) でプロジェクタのキャリブレーションを行う。
中の計算は[こちらのサイト](https://kamino.hatenablog.com/entry/opencv_calibrate_camera)が参考になる。

### インストール
- Python 3 (と pip) をインストールする（[参考](https://realpython.com/installing-python/)）。
- Pythonのモジュール `opencv-python` と `NatNetClient` をインストールする。
    ```Bash
    pip install opencv-python
    pip install NatNetClient
    ```

### 使い方
1. OptiTrack社のカメラが接続され、Motive上でも認識されていることを確認する。

1. 以下のパラメータを [`setting.py`](./setting.py) に入力する。
    - `PointsAlreadyGot`: すでに対応組があるかどうか。

        `False` : まだ対応点の組を取得しておらず、手動で今から取得する必要がある場合。
        
        `True` : すでに対応点の組の取得が終わっていて、ファイルの格納されている時。

    - `WIDTH, HEIGHT`: プロジェクタの解像度 [pixel]
    
    - `SCREEN_WIDTH, SCREEN_HEIGHT`: 投影範囲の実際の大きさ [mm]。大まかな値で良い。

    - `FOCAL_LENGTH`: プロジェクタと投影面の大まかな距離[mm]。大まかな値で良い。
    
    - `Ox, Oy`: プロジェクタウィンドウの左上端の位置 [pixel]。
    
    - `CALIB_OBJ`: キャリブレーション用の物体のMotive上の登録名。
    Motiveでは三次元位置姿勢を取得するのにrigidbodyとして登録する必要があり、そのrigidbodyの名前を入れる。
    Defaultでは`CalibObj`となっている。
    
    - `DIR_NAME`: 結果を格納するディレクトリの名前。
    この`DIR_NAME`はそれぞれのファイルにも名前がつく。
    例えば、カメラ行列を格納するファイルは `camera_matrixDIR_NAME.txt`となる。

1. [`calib.py`](./calib.py)を実行する.
    ```bash
    python calib.py
    ```

1. `PointsAlreadyGot`で`False`とした場合は以下のようにして対応組を取得する。
    1. マウスカーソルをウィンドウ上に動かす。

    1. `CalibObj`をプロジェクタと投影面の間の適当な位置に持ってきて、マウスカーソルと`CalibObj`の中心が一致するように両者の位置を調整する。

    1. 一致したら左クリックする。
    もし、無事に対応点の組が取得できた場合はカーソルの二次元座標と`CalibObj`の三次元座標がコンソールに表示される。
    対応組が取得できなかった場合は`CalibObj is missing`とコンソールに表示される。

    1. これを繰り返して20組程度の対応組を取得する。

    1. 任意のキーを押して対応組の取得を終了する。

1. 計算結果が`DIR_NAME`に格納される。

