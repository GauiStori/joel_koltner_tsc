# joel_koltner_tsc
Joel Koltners Tektronics Screen dump utility (Py-WxWidgets)

The original version work nicely with python2.7 and wxPython 2.8.12.1 which is still 
available but not supported anymore. It is also quite difficult to install on modern Linux
distribution.

The current version is tested with python 3.13 and wxPython 4.2.3 on Windows but it should work on Linux as well.

To run the program install python from https://python.org.
Then run pip install wxPython

For Linux
apt install python3-wxgtk4.0 wl-clipboard

If testing hook up two USB-RS232 converters and a nullmodem cable.

Run TSC.py and use /dev/ttyUSB0
Run 
csa803_sendbuf.py /dev/ttyUSB1 csa803_test_image.bin

and an image will be uploaded in 20 secs instead of 60 secs for the instrument.
For repeated testing you can set the baudrate to 115200 for both programs and 
the upload will take <2 secs.

