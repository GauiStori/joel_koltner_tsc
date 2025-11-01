# joel_koltner_tsc
Joel Koltners Tektronics Screen dump utility (Py-WxWidgets)


For Linux
apt install python3-wxgtk4.0 wl-clipboard

If testing hook up two USB-RS232 converters and a nullmodem cable.

Run TSC.py and use /dev/ttyUSB0
Run 
csa803_sendbuf.py /dev/ttyUSB1 csa803_test_image.bin

and an image will be uploaded in 20 secs instead of 60 secs for the instrument.
For repeated testing you can set the baudrate to 115200 for both programs and 
the upload will take <2 secs.


