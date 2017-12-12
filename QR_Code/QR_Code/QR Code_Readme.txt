****************************************README***************************************

*************************************BARCODE READER***********************************

Follow The below Installation Steps:

1. Update and Upgrade your pi

	sudo apt-get update && sudo apt-get upgrade -y

2. Update the firmware:
	
	sudo rpi-update

Then, Reboot your pi

	sudo reboot

3. Install the below Libraries in order:

	sudo apt-get install python-dev
	sudo apt-get install python-pip
	sudo pip install pillow
	sudo apt-get install python-httplib2

4. Install USB webcam package.

	sudo apt-get install fswebcam

5. Explored if I could change the resolution of the image

	fswebcam -r 1280x720 –-no-banner image2.jpg


6. Install the python Zbar dependencies by executing

	sudo apt-get install python-zbar
	sudo apt-get install libzbar-dev

7. Put the script files from the above URL on Raspberry in a folder, and then from that folder executed:

	python setup.py install –user



*************************************UART COMMUNICATION***********************************
1. Enable the Serial Communication in Raspberry pi

	sudo raspi-config
	
	Then go, Advanced Option-> Serial-> Enable-> Yes-> Reboot
Expand filesystem and enable serial on advanced page, exit and reboot.

	sudo apt-get update

2. Device Tree settings as below:

Add device tree to /boot/config.txt to disable the Raspberry Pi 3 bluetooth.

	sudo nano /boot/config.txt

To disable the blutooth (Paste this below code)

	dtoverlay=pi3-disable-bt  

Save the file, Ctrl + O
Close the editor, Ctrl + X

Reboot the pi

	sudo reboot

3. First make a backup of the file containing kernel parameters cmdline.txt as cmdline_bp.txt

	sudo cp /boot/cmdline.txt /boot/cmdline_bp.txt

4. Edit the file cmdline.txt by removing the parameters containing ‘ttyAMA0‘. ie. ‘console=ttyAMA0,115200’
	
	sudo nano /boot/cmdline.txt

	Save the file, Ctrl + O
	Close the editor, Ctrl + X

4. Reboot the Raspberry pi OS

	sudo reboot

*************************************UART HARDWARE INTERFACE***********************************

1. Connect Your Camera USB into Raspberry pi

2. Connect RX and TX Pin to the Serial Communication. OR Short RX and TX Pin for the Serial Communication Working Test.

3. Finally Run the QR_Uart.py Code file.

4. And Show any QR code infront of your camera.