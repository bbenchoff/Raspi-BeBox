# Raspi-BeBox
## A Raspberry Pi case that looks like a wee BeBox

![Renders](https://github.com/bbenchoff/Raspi-BeBox/blob/main/Images/Main.png)
![Side view](https://github.com/bbenchoff/Raspi-BeBox/blob/main/Images/Main.jpg)

There are several components of the BeBox, including 3D printed (filament), 3D printed (SLA), circuit boards, and random stuff picked up from Amazon:

### BlinkenPanel
The BlinkenPanel displays CPU usage on 16 LEDs shinging through the front. The [project is shared on OSHPark](https://oshpark.com/shared_projects/XPZorljf). Other components needed for this are:

* Green Square LEDs - Part Number SSL-LX3353GD
* I2C GPIO expander - MCP23017-E/SP
* Resistors of various sort - 0805
* DC Fan 5V - any 30mm fan for a Raspberry Pi

### Front panel
The heart of the BeBox - a front panel with Blinkenlights. This [is available on Shapeways](https://www.shapeways.com/product/FETJ2WU6V/raspi-bebox-face?optionId=224175918) or in the 3D files folder of this repository. Print with gray resin.

### Case Badge
...Comes from [Case Badges](https://www.case-badges.com), have them make a 0.75" square domed badge of the images in the /Graphics folder of this repository

### Interior. 
The case is designed for a Raspberry Pi 4, along with a dual microHDMI adapter board:

* [Buy these adapter boards](https://www.amazon.com/gp/product/B08V5MXLS6)
* [and this USB-C right angle adapter](https://www.amazon.com/gp/product/B086W2LTGY)

Screw bosses are sized for No. 4 screws.


## Assembly

Insert the LEDs in one side of the front panel. The anode (+) goes toward the middle. Bend the cathode (-) out. Fit the PCB with only the anodes of one side installed. Glue is recommended to hold the LEDs in place.

![](https://github.com/bbenchoff/Raspi-BeBox/blob/main/Images/as1.jpg)

Install the other side of the LEDs, anode only.

![](https://github.com/bbenchoff/Raspi-BeBox/blob/main/Images/as2.jpg)

Mount the PCB to the front panel with screws. Solder the anodes of the LEDs. Bend the cathode legs around the PCB to the other LED solder pads.
![](https://github.com/bbenchoff/Raspi-BeBox/blob/main/Images/as3.jpg)
![](https://github.com/bbenchoff/Raspi-BeBox/blob/main/Images/as4.jpg)

That's it! That's the easiest way to assemble this thing. Now write some python for the blinkenlights.
