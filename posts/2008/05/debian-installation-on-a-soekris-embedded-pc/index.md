---
title: "Debian installation on a Soekris embedded PC"
date: 2008-05-16
categories: 
  - "home-automation"
  - "programming"
  - "tools"
---

Ubiquitous home automation will never become a reality unless cheap embedded PCs are available to be the "brains" of the home. Some time ago I came across a company called [Soekris Engineering](http://www.soekris.com/) who make relatively cheap embedded PCs, like the one shown below.

![net4801](http://www.visnet.ch/smartbuildings/wp-content/uploads/2008/05/net4801_bc_front_big.jpg)

This little guy packs a 20Gb CompactFlash harddisk, 128 Mb RAM, and a 266 MHz Intel processor. Of course I managed to hose mine's operating system and had to reinstall it from scratch. Here are the steps I followed to install Debian from my laptop (running Ubuntu 7.10), connected to the Soekris with a null-modem cable.

### Minicom setup

Install the minicom package on the host system, you're going to need it to communicate with the Soekris box during the installation. Here is what my minicom configuration looks like:

![Minicom default configuration](http://www.visnet.ch/smartbuildings/wp-content/uploads/2008/05/minicom-config.png)

I also suggest you run the following before starting minicom:

`export LANG=C`

If you don't you might run into strange error reports from minicom.

The Debian installer will by default talk to the serial line in 9600 bauds, so I suggest you make this the default in the Soekris comBIOS's monitor program. After entering it, enter

`set ConSpeed=9600`

and reboot. Change the setting in minicom too.

### DHCP setup

We're going to start a Debian installer through PXE, so first we need a DHCP server configured to provide the right file. Install the dhcp3-server package on the host system. Configure it by appending something similar to /etc/dhcp3/dhcpd.conf:

`subnet 192.168.0.0 netmask 255.255.255.0 { option domain-name "visnet.ch"; option domain-name-servers 192.168.0.1; option routers 192.168.0.1; range 192.168.0.4 192.168.0.4; option host-name "misterhouse"; next-server 192.168.0.69; option root-path "/var/lib/tftpboot"; filename "/pxelinux.0"; }`

Start the DHCP server.

### TFTP setup

Install the tftpd-hpa package on the host system. Start the server with:

`in.tftpd -l -s /var/lib/tftpboot/`

### Download Debian installer

Download the most recent Debian installer from the [Debian download site](http://ftp.nl.debian.org/debian/dists/etch/main/installer-i386/current/images/netboot/netboot.tar.gz). Untar it to /var/lib/tftpboot. Change the pxelinux.cfg symlink to point to the serial-9600 configuration:

`drwxr-xr-x 3 root root 4096 2008-02-28 01:28 debian-installer lrwxrwxrwx 1 root root 32 2008-05-09 21:45 pxelinux.0 -> debian-installer/i386/pxelinux.0 lrwxrwxrwx 1 root root 46 2008-05-09 22:00 pxelinux.cfg -> debian-installer/i386/pxelinux.cfg.serial-9600`

### Boot the Soekris

You're now ready to boot the Soekris box. Enter the comBIOS' monitor program and enter: `boot f0`

And go through the installation process. Since the installer will download packages from mirror locations you should turn off the DHCP server on the host system, and let the Debian installer configure itself with your LAN's DHCP server.

I called my system misterhouse@visnet.ch, since I intend to use it to run the open-source [MisterHouse](http://misterhouse.sourceforge.net/) home automation program.

You will at some point be asked how you want to partition the 20 Gb disk. If you leave the default settings, you run the risk of not being able to boot because of an "Error 18" from GRUB. See [here](http://lists.soekris.com/pipermail/soekris-tech/2007-November/013378.html) for an explanation. That's why you should make the first partition a small (about 100 Mb) bootable partition mounted at /boot. The rest of the disk can be split between a 400 Mb swap space and all the rest.

Your setup should look something like this:

![Debian installer partitions setup](http://www.visnet.ch/smartbuildings/wp-content/uploads/2008/05/debian-installer-partitions.png)

When prompted, say yes to install GRUB on the master boot record.

You will also be asked what types of software to install. For a standalone, headless mini-server like this, I configured it like this:

![Debian software types](http://www.visnet.ch/smartbuildings/wp-content/uploads/2008/05/debian-installer-server.png)

### Conclusion

That's pretty much it. When you're all done the installer will prompt you to reboot the system, which will then boot into Debian. Login with the username you provided during setup. I strongly recommend you install a SSH server or you won't be able to login other than by the serial console:

`aptitude install openssh-server`

That should be it. Enjoy your new home automation central system.
