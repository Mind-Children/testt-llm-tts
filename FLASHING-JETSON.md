# HOW TO FLASH THE JETSON

## Prepare the Turing Pi 2.5

Make sure the Jetson you want to flash is in slot 2, 3 or 4 (so, not 1). Make sure the NVMe memory is also installed in the corresponding slot.

Switch on the Turing Pi and connect the network cable.

Connect a USB-C cable to the small USB-C port marked `4XNODE USB_DEV`. The other end goes into the host machine.

Go to the Turing Pi page (`http://turingpi.local`) and go to the `Nodes` tab. Edit the nodes and turn off the power to the slot where the Jetson is in.

Go to the `USB` tab and set the USB mode to `Flash` and the connected node to the slot you put the Jetson in.

Go back to the `Nodes` tab, edit the nodes and turn the power to the Jetson back on.

If all goes well, you can now flash the Jetson from your host machine. Confirm by typing on the host machine:

```
lsusb
```

This should mention `NVIDIA Corp. APX` in the list.

## Prepare the Host Machine

Just use Linux. Ubuntu >=20 is fine.

Go here: `https://developer.nvidia.com/embedded/jetson-linux-archive`

Click on the latest Jetpack that supports your Jetson. For me it was 36.4.3. Now download the "Driver Package (BSP)" and the "Sample Root Filesystem".

Unzip the driver package in some sensible place:

```
cd ~
mkdir jetson
cd jetson
tar xpf Downloads/<driver package file>
```

This will create `~/jetson/Linux_for_Tegra`. That's the main important directory from now on.

Unzip the root filesystem:

```
cd ~/jetson/Linux_for_Tegra
mkdir rootfs
sudo tar xpf Downloads/<sample root filesystem>
```

Now for the most important part. Go to `~/jetson/Linux_for_Tegra/bootloader`. Here are all the configuration files for flashing the Jetson.

The Turing Pi 2.5 is compatible with Jetson EXCEPT FOR ONE DETAIL: **It does not have the same flashing electronics as the Jetson SDK board**

To accommodate for this, make sure that `cvb_eeprom_read_size` in the config files is always set to `<0x0>` instead of whatever value it is normally:

```
cd ~/jetson/Linux_for_Tegra/bootloader
grep -R cvb_eeprom_read_size *
```

This outputs a list of files to change. For me it was:

```
generic/BCT/tegra234-mb2-bct-misc-p3767-0000.dts
generic/BCT/tegra234-mb2-bct-misc-p3701-0002-p3711-0000.dts
generic/BCT/tegra234-mb2-bct-misc-p3701-0002-p3740-0002.dts
tegra234-mb2-bct-common.dtsi
tegra234-mb2-bct-misc-p3767-0000.dts
```

Edit each of those files and change the value behind `cvb_eeprom_read_size = ` to `<0x0>`.

## Flash It!

Prepare the firmware:

```
cd ~/jetson/Linux_for_Tegra
sudo ./apply_binaries.sh
sudo ./tools/l4t_flash_prerequisites.sh
```

Create the default username, password and hostname:

```
sudo ./tools/l4t_create_default_user.sh -u rudolph -p santa123 -a -n northpole
```

You'll be asked to accept the license. Use the arrow keys to hilight `<Accept>`, and press Enter.

This would create the user `rudolph` with password `santa123` and the Jetson would be called `northpole`.

Now you're ready to flash the Jetson. Type the following:

```
sudo ./tools/kernel_flash/l4t_initrd_flash.sh --external-device nvme0n1p1 -c tools/kernel_flash/flash_l4t_external.xml -p "-c bootloader/generic/cfg/flash_t234_qspi.xml" --showlogs --network usb0 p3509-a02-p3767-0000 internal
```

This will take a few minutes. Experience tells us that this flashing process is not a very exact science, unfortunately. So, if the process fails somewhere, just try again. If it keeps on failing at the same step multiple times, it might be necessary to head over to NVidia or Turing resources, to figure out what's going on.

Note: if the `p3509-a02-p3767-0000` (the NX Developer Kit) configuration doesn't work for the Orin Nano, use `jetson-orin-nano-devkit` instead. For me both of them worked with the Turing Pi.

## After Sucessful Flashing

Head over to `http://turingpi.local` and go to the `Nodes` tab. Edit the settings and switch off the power to the Jetson you just flashed.

Go to the `USB` tab, and put the USB mode back to `Device`.

Go back to the `Nodes` tab. Edit the settings and switch the power back on.

The Jetson now boots up. Figure out the IP address (check the local router for the new connection).

## Install the Software

Ssh into the Jetson:

```
ssh rudolph@192.168.1.12
```

First, install all the necessary Jetpack components:

```
sudo apt update
sudo apt install nvidia-jetpack
```

Some useful tools to start with:

```
sudo apt install python3-pip
sudo pip3 install -U jetson-stats
sudo nvpmodel -m 0
sudo reboot
```
