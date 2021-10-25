Author: Jake Huneau (huneauja@umich.edu)
Date: 8/24/21


# Extracting AES keys from memory

This project was done for Jake's Master's project course (CIS-695). The goal was to scan the memory of a UEFI system using SMI calls in
order to find AES-128-CBC and AES-256-CBC keys that are still in memory. This was done successfully.

## Building
QEMU and edk2 are the main repos used for this project. Most of the build instructions were adopted from Dr. Bacha.

### QEMU
This was done using qemu version 5.0.1 which was installed with the following steps

1. Install git and other required libraries
```
sudo apt-get install git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
```

2. install qemu libraries
```
sudo apt-get install qemu-system-x86 ovmf
sudo apt install qemu qemu-kvm libvirt-bin  bridge-utils  virt-manager
sudo apt-get install spice-vdagent
sudo apt-get build-dep qemu <-- make sure system update has source code checked, may need to do: sudo apt-get update
```

3. Clone qemu repo
```
git clone https://git.qemu.org/git/qemu.git
```

4. Switch to stable-5.0 branch
```
cd qemu
git checkout stable-5.0
```

5. Build qemu as per https://wiki.qemu.org/Hosts/Linux
```
# Configure QEMU for x86_64 only - faster build (no need to build other architectures)
./configure --target-list=x86_64-softmmu --enable-debug --enable-spice
# Build in parallel
make -j16
```

6. Check version
```
x86_64-softmmu/qemu-system-x86_64 --version
```

Sample output of this looks like
```
QEMU emulator version 5.0.1 (v5.0.1-dirty)
Copyright (c) 2003-2020 Fabrice Bellard and the QEMU Project developers
```

You also need to create an image for the VM in the following way
```
qemu-img create -f qcow2 example.qcow2 16G
cd example.qcow2 ~/images/
```

### EDK2
edk2 is used for building OVMF. The stable-202105 branch was used for this project.

1. Clone the repo
```
git clone --recursive https://github.com/tianocore/edk2
cd edk2
git checkout stable-202105
git pull --recurse-submodules && git submodule update --recursive
```

2. Install needed libraries
```
sudo apt-get install build-essential uuid-dev iasl git gcc-5 nasm
```

3. Compile and setup build tools
```
make -C BaseTools
. edksetup.sh
```

4. Setup build target as according to https://github.com/tianocore/tianocore.github.io/wiki/Common-instructions
```
edit Conf/target.txt with the following:

ACTIVE_PLATFORM       = MdeModulePkg/MdeModulePkg.dsc
TOOL_CHAIN_TAG        = GCC5
TARGET_ARCH           = X64

MAX_CONCURRENT_THREAD_NUMBER = 16   (increase according to how many processors you have)
```

5. Build OVMF
```
OvmfPkg/build.sh -a X64 -D SMM_REQUIRE
```

6. Copy firmware images
```
cp edk2/Build/OvmfX64/DEBUG_GCC5/FV/OVMF* ~/images/
```

This build was automated in `build_ovmf.sh` which wil also remove the previous firmware images to be replaced with the fresh ones.

## Ubuntu
An ubuntu image must also be downloaded and saved ot be used as a shell for OVMF. The instructions from this tutorial were followed:
https://www.collabora.com/news-and-blog/blog/2017/01/16/setting-up-qemu-kvm-for-kernel-development.

1. clone linux
```
git clone --depth=1 git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
cd linux
make x86_64_defconfig
make kvm_guest.config
make -j 8
```

## BitWarden
The testing on bitwarden was done with the master branch of the cli repository on 8/24/21. This can be cloned with the following:
```
git clone https://github.com/bitwarden/cli.git
```

NPM is required to compile this and can be installed with
```
sudo apt-get install npm
```

and then the code can be compiled with
```
npm install
npm run sub:init # initialize the git submodule for jslib
npm run build:watch # watch will recompile the code whenever there are changes
```

You can then run the code in the following way:
```
node ./build/bw.js login
```

The different commands can be found in `src/commands` and the code can be traced from there.

# Running
The following command was used for running the VM using qemu. It can be found in `run_ubuntu.sh`
```
sudo qemu/x86_64-softmmu/qemu-system-x86_64 -m 1G -enable-kvm \
    -machine q35,smm=on \
    -smp cores=16,sockets=1 \
    -global ICH9-LPC.disable_s3=1 \
    -nographic \
    -kernel linux-stable/arch/x86/boot/bzImage \
    -vga qxl \
    -display gtk,show-cursor=on \
    -drive if=pflash,format=raw,readonly,file=images/OVMF_CODE.fd \
    -drive if=pflash,format=raw,file=images/copy_OVMF_VARS.fd \
    -hda images/example.qcow2 \
    --append "root=/dev/sda1 console=ttyS0" \
    -hdc qemu-img.img \
    -debugcon file:debug.log -global isa-debugcon.iobase=0x402 \
```

# Development
All changes for the SMI were done in `edk2/MdeModulePkg/Core/PiSmmCore/PiSmmCore.c` and in the method `SmmEntryPoint` which is triggered
whenever an SMI call is made.

To allow OpenSSL to be compiled and included, the following file must be modified: `edk2/MdeModulePkg/Core/PiSmmCore/PiSmmCore.inf`. In
this file, find the section `[LibraryClasses]` and add `OpensllLib` to the bottom of this section.

There were errors thrown for accessing some illegal memory ranges. This was remedied by modifying `edk2/MdeModulePkg/Core/PiSmmCore/PiSmmIpl.c`.
Around line 852, make the following change to remove a SmmAccess lock:
```
#if 0
  mSmmAccess->Lock (mSmmAccess);
#endif
```
and then around line 864 make the following change
```
#if 0
    SmmIplGuidedEventNotify (...)
#endif
```

# Testing
After making the changes as seen in `PiSmmCore.c`, the changes were tested by booting up the VM with ubuntu and encrypting a large (1.4 GB) file with
the following command
```
openssl enc -aes-256-cbc -nosalt -e -in file.txt -out out.txt.enc \
-K 00112233445566778899AABBCCDDEEFFFFEEDDCCBBAA99887766554433221100 \
-iv 00000000000000000000000000000000
```

While that is running, I change to the qemu console by hitting `Ctrl+a c`. Then in the qemu console, I trigger an SMI with the following command:
`o 0xb2 0x51`. After triggering this, I can watch the log with `tail -F ~/debug.log`. Once a key is found, it is printed to this log.
