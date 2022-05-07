import os
import time
print("Loading Archeon...")
os.system('clear')
print("""

                             ▄▄                                    
      ██                    ███                                    
     ▄██▄                    ██                                    
    ▄█▀██▄   ▀███▄███ ▄██▀██ ███████▄   ▄▄█▀██  ▄██▀██▄▀████████▄  
   ▄█  ▀██     ██▀ ▀▀██▀  ██ ██    ██  ▄█▀   ████▀   ▀██ ██    ██  
   ████████    ██    ██      ██    ██  ██▀▀▀▀▀▀██     ██ ██    ██  
  █▀      ██   ██    ██▄    ▄██    ██  ██▄    ▄██▄   ▄██ ██    ██  
▄███▄   ▄████▄████▄   █████▀████  ████▄ ▀█████▀ ▀█████▀▄████  ████▄

                Automated Arch Linux Installer                                                         
                github.com/WooxHimself/Archist
""")

print("""
========================
    INITIAL SETUP
========================

If you select anything wrong, press CTRL+C and restart the script.


""")

username = input("Enter your username for this system: ").lower()
hostnameprompt = input("Enter your hostname (computer name) for this system: ")
print("")
os.system("fdisk -l")
print("")
driveselect = input("Enter the drive you want to install Arch Linux on (on example /dev/sda): ")
print("")
if "/dev/" not in driveselect:
    print("ERROR! INVALID DISK CHOICE!")
    os.system("fdisk -l")
    driveselect = input("Enter the drive you want to install Arch Linux on (on example /dev/sda): ")
else:
    pass

partition1 = f"{driveselect}1"
partition2 = f"{driveselect}2"
partition3 = f"{driveselect}3"

ssdcheck = input("Is the selected drive an SSD? (y/N)")
if ssdcheck == "y" or ssdcheck == "Y":
    mntopt = "noatime,compress=zstd,ssd,commit=120"
else:
    mntopt = "noatime,compress=zstd,commit=120"


print("")
#print("""
#
#[1] btrfs - BEST, but more complicated
#[2] ext4 - Great for new users
#[3] ext3 - Older, unstable, not recommended
#
#""")
#
#drivefs = input("What filesystem do you want to use? (1, 2 or 3): ")
#if drivefs == '1':
#    filesys = "btrfs"
#elif drivefs == '2':
#    filesys = "ext4"
#elif drivefs == '3':
#    filesys = "ext3"
print("Encrypting the drive means nobody won't be able to read/write data on the drive without a password")
print("Also means your data will be completely lost if you forgot your password and you'll need to format it.")
print("May be useful for laptop users")
encryption = input(f"Would you like to encrypt your drive? ({driveselect}) (y/N):")
if encryption == 'y' or encryption == 'Y':
    encryptstate = "YES"
else:
    encryptstate = "NO"

print("""
en - English
cz - Czech
de - Deutsch
es - Espanol/Spanish
fr - French
gr - Greek
hu - Hungarian
it - Italian
lt - Latin
ua - Ukrainan
ru - Russian
uk - United Kingdom

(or enter any other from the list on Arch Wiki)
""")
keymap = input("Enter your keymap (Keyboard layout)")
timezone = input("Enter your timezone (on example America/Chicago or Europe/London): ")
print("""

[1] linux - Classic kernel      <<< RECOMMENDED!
[2] linux-hardened - Security hardened kernel, more upstream kernel hardening features
[3] linux-zen - Custom ZEN kernel, used by gamers, may perform worse
[4] linux-lts - (L)ong(T)erm(S)upport Kernel


""")

kernelselect = input("What kernel would you like to use? (1, 2, 3 or 4): ")

if kernelselect == '1':
    kerneltype = 'Linux'
elif kernelselect == '2':
    kerneltype = 'Hardened'
elif kernelselect == '3':
    kerneltype = 'ZEN'
elif kernelselect == '4':
    kerneltype = 'LTS'

if kerneltype == 'Linux':
    krnl = "linux linux-firmware"
elif kerneltype == 'Hardened':
    krnl = "linux-hardened linux-hardened-headers"
elif kerneltype == 'ZEN':
    krnl = "linux-zen linux-zen-headers"
elif kerneltype == 'LTS':
    krnl = "linux-lts"

print("""

[1] Nvidia
[2] AMD
[3] INTEL

If you're using a VM, you can skip this step by pressing [ENTER]
""")

gpu = input("What is your GPU manufacturer? (1-3): ")

if gpu == "1":
    gputype = "NVidia"
    gpupackages = "nvidia-dkms"
elif gpu == "2":
    gputype = "AMD"
    gpupackages = "xf86-video-amdgpu"
elif gpu == "3":
    gputype = "INTEL"
    gpupackages = "xf86-video-intel"
elif gputype = "":
    gputype = "VirtualMachine"
    gpupackages = ""


print("LAST QUESTION")
print("""

[1] Minimal - Only required packages will be installed, after installation you will boot into tty console | Installation will take ~5 minutes
[2] Classic - Some packages will be installed like desktop, web browser, text editor and other every-day use apps | Installation will take ~10-15 minutes
[3] Ultimate - Everything from both types will be here, along with other apps | Installation will take ~30-45 minutes

""")
installtype = input("What type of installation do you require? (1, 2 or 3): ")
if installtype == '2' or installtype == '3':
    print("""

[1] KDE Plasma - Great choice for users coming from Windows         <<<< RECOMMENDED
[2] XFCE - Lightweight Desktop good for both low-end and high-end hardware      <<<< RECOMMENDED
[3] Cinnamon - Like XFCE, but with more functions not as lightweight
[4] i3 - Window Manager aimed for advanced users, not recommended for new Unix/Linux users
[5] GNOME - Classic Desktop, similar to KDE Plasma      <<< RECOMMENDED
[6] LxQt - Very lightweight Desktop, can be used with Window Managers.
[7] Openbox - Also really lightweight desktop/window manager, but harder to use and configure
    
    """)
    desktop = input("What desktop/wm would you like to use? (1-7): ")
else:
    pass

if installtype == "2":
    if desktop == '1':
        desktoptoinstall = "xorg xorg-server plasma-desktop kde-applications sddm"
    elif desktop == '2':
        desktoptoinstall = "xorg xorg-server xfce xfce4-goodies lightdm"
    elif desktop == '3':
        desktoptoinstall = "xorg xorg-server cinnamon lightdm"
    elif desktop == '4':
        desktoptoinstall = "xorg xorg-server i3-gaps lightdm"
    elif desktop == '5':
        desktoptoinstall = "xorg xorg-server gnome gnome-tweaks gdm"
    elif desktop == '6':
        desktoptoinstall = "xorg xorg-server lxqt sddm"
    elif desktop == '7':
        desktoptoinstall = "xorg xorg-server openbox lightdm"
    typepackages = "base-devel nano vim git neofetch sudo firefox"

elif installtype == "3":
    elif desktop == '1':
        desktoptoinstall = "xorg xorg-server plasma-desktop kde-applications sddm steam discord lutris wine winetricks"
    elif desktop == '2':
        desktoptoinstall = "xorg xorg-server xfce xfce4-goodies lightdm steam discord lutris wine winetricks"
    elif desktop == '3':
        desktoptoinstall = "xorg xorg-server cinnamon lightdm steam discord lutris wine winetricks"
    elif desktop == '4':
        desktoptoinstall = "xorg xorg-server i3-gaps lightdm steam discord lutris wine winetricks"
    elif desktop == '5':
        desktoptoinstall = "xorg xorg-server gnome gnome-tweaks gdm steam discord lutris wine winetricks"
    elif desktop == '6':
        desktoptoinstall = "xorg xorg-server lxqt sddm steam discord lutris wine winetricks"
    elif desktop == '7':
        desktoptoinstall = "xorg xorg-server openbox lightdm steam discord lutris wine winetricks"


    typepackages = "base-devel nano vim git neofetch sudo discord lutris steam firefox"

print(f"""Please confirm all informations below are correct:

Username: {username}
Hostname: {hostnameprompt}
Selected Drive: {driveselect}
Drive Filesystem: btrfs
Drive Encryption: {encryptstate}
Kernel: {kerneltype}
Keymap: {keymap}
Timezone: {timezone}

""")

print("Please confirm all informations above are correct as they are final and some of them cannot be changed")
print("afterwards without reinstallation.")

allcorrect = input("Is everything correct? (y/N): ")
if allcorrect == 'y' or allcorrect == 'Y':
    print("Thank you! The installation may begin!")
    print(f"WARNING! THE SELECTED DRIVE ({driveselect} WILL BE FORMATTED AND ALL OF IT'S DATA WILL BE LOST!")
    time.sleep(2)
    print(f"FORMATTING {driveselect} IN...")
    print("PRESS CTRL+C TO ABORT")
    time.sleep(0.4)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Formatting...")
    time.sleep(0.3)
    os.system("umount -A --recursive /mnt")
    os.system(f"sgdisk -Z {driveselect}")
    print("Installation has begun, grab a cup of coffee, sit back and relax while the installation finishes")
    print("Any errors will be reported here.")
    print("Thanks for using Archeon!")
    os.system(f"sgdisk -n 1::+512M --typecode=1:ef02 --change-name=1:'BOOT' {driveselect}")
    os.system(f"sgdisk -n 2::+2G --typecode=2:ef00 --change-name=2:'SWAP' {driveselect}")
    os.system(f"sgdisk -n 3::-0 --typecode=3:8300 --change-name=3:'ROOT' {driveselect}")
    os.system(f"mkfs.fat -F32 {partition1}")
    os.system(f"mkswap {partition2}")
    os.system(f"swapon {partition2}")
    os.system(f"mkfs.btrfs {partition3}")
    os.system(f"mount {partition3} /mnt")

    print("=====================")
    print("CREATING SUBVOLUMES")
    print("=====================")
    os.system("btrfs subvolume create /mnt/@")
    os.system("btrfs subvolume create /mnt/@home")
    os.system("btrfs subvolume create /mnt/@var")
    os.system("btrfs subvolume create /mnt/@opt")
    os.system("btrfs subvolume create /mnt/@tmp")
    os.system("btrfs subvolume create /mnt/@.snapshots")

    os.system(f"umount /mnt")
    os.system(f"mount -o {mntopt},subvol=@ {partition3} /mnt")
    os.system("mkdir -p /mnt/{home,var,tmp,.snapshots}")

    os.system(f"mount -o {mntopt},subvol=@home {partition3} /mnt/home")
    os.system(f"mount -o {mntopt},subvol=@opt {partition3} /mnt/opt")
    os.system(f"mount -o {mntopt},subvol=@tmp {partition3} /mnt/tmp")
    os.system(f"mount -o {mntopt},subvol=@.snapshots {partition3} /mnt/.snapshots")
    os.system(f"mount -o subvol=@var {partition3} /mnt/var")
    print("=====================")
    print("INSTALLING BASE SYSTEM")
    print("=====================")

    os.system(f"pacstrap /mnt base {krnl}")
    print("")
    print("=====================")
    print("")
    print("=====================")
