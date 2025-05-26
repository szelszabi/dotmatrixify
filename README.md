# dotmatrixify
Transforms pixelart to dot matrix! The Nothing aesthetic is in arms reach!

From:
<br>
![image search api](https://github.com/szelszabi/dotmatrixify/blob/main/input_image/example.png)

To:
<br>
<img src="https://github.com/szelszabi/dotmatrixify/blob/main/output_image/example.png" width="256">

## Usage

You should create a virtual environment for this:
 - The command for that is: `python -m venv env`
 - You can activate by: `source env/bin/activate` (On Linux) Or running `env/bin/Activate.ps1` in PowerShell
 - You can install necessary packages by: `pip install -r requirements.txt`
 - To deactivate a venv you just type in `deactivate` and you are done.

Setting the parameters is kinda rusty right now, will be fixed™ in a future PR.
 - In the main file (dotmatrixify.py) you can set the parameters in the main function such as:
   - Input image file path (JPEG also works, but output won't be transparent)
   - Output image file path
   - Kernel size (The size of an NxN matrix that will be used to do the (yet very simple) convolution), this effectively divides the pictures dimensions by this amount
   - Circle's radius, this effectively multiplies the pictures dimensions by this amount
 - After setting up the parameters, you can run the script and check out the results in the output path!

Have fun using it!
