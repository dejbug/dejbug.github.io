# Time

I am on the clock. Waiting for my friend to call so we can go help her get some furniture from A to B. (B being a much nicer place than A.)

# Waiting

I don't really know what to do with myself while waiting. I can't really concentrate on anything. I can't say I like the feeling. I feel pointless.

# But anyway

There's things I need to do but I keep getting distracted left and right (by things I'd rather do). I decided to just let the distractions happen. Let the chaos in. If I were a bit more organized it wouldn't be so disorientating. Or if my working memory were made of firmer stuff. I probably should be taking notes, like these here "blogs". Aids to memory. Weblogs -> Memlogs.

# Home sweet home

I've done my duty and now I'm back and showered and relaxed. The time is mine again. There will be no distractions. I had been looking forward to a little heavy lifting though, but all of it was so unrewardingly easy that I unironically regretted getting off the couch for this. Walking there was more exhausting to me, psychologically, than the manual labor awaiting me there. It's all those other folks out there... with their cars and the commotion and the noise. I can't believe that people are able to thrive out there. It's a witch's brew of mind-altering ingredients. I'm on an adrenaline high while I'm out among those lunatics so I feel completely numb when I get home. I don't like leaving home. There's really nothing out there for me anymore. It's come to a point where I no longer want to hang out with my friends. It's interesting how different it is in the chess club. It's a completely different atmosphere. I don't even notice the time passing. And I have new friends there too. I've grown old, that's all.

# UNIX Philosophy

I need to remind myself to write smaller, dedicated tools in such a way that they can be easily combined. https://en.wikipedia.org/wiki/Unix_philosophy

# TOC Issue

There's a problem with my `toc.js` on "FFfA"(Firefox for Android). I noticed it after rereading last night's blog in bed. When scrolling the page back upwards, FFfA will show the address bar so that the `clientHeight` is smaller than when scrolling down while reading. This is wreaking havoc with my positioning. Maybe using `svh` versus `lvh` units is a simple fix? The entire re-positioning feels rather fiddly.

# Bluetooth on the radar

I had got myself a fitness watch. Cue for laughter. A cheap one just to have a closer look at one. It's been lying around for a while now and it's time to put it to some use. Hopefully an unintended one. But first things first.

# Oh Cathy, oh Alison, oh Phillipa, oh Sue

```java
[bluetooth]# scan le
Discovery started
[CHG] Controller 00:1A:7D:DA:71:12 Discovering: yes
[NEW] Device E9:1C:7D:82:E5:6B ID131Color HR
```

Something is self-advertising with `ID131Color HR`. The images that come up in the search are a perfect match. So it's official name is "LETSCOM ID115PHR Health & Fitness Tracker" https://letsfit.com/products/letscom-fitness-trackers-hr-activity-tracker-with-heart-rate-monitor-step-counter-sleep-monitor-for-women-men

Apparently it was meant to be paired with the VeryFitPro app https://play.google.com/store/apps/details?id=com.veryfit2hr.second (instead of the Letsfit app https://play.google.com/store/apps/details?id=com.honbow.letsfit ?) but I might be able to use Gadgetbridge

https://f-droid.org/en/packages/nodomain.freeyourgadget.gadgetbridge/

or do some damage with something like DaFlasher (a DaFit-based devices flasher)
https://play.google.com/store/apps/details?id=com.atcnetz.paatc.patc
https://hackaday.com/2020/05/02/cheap-smartwatch-hacking-to-run-your-own-code/
if indeed it is DaFit based.

And boy-o have these guys here gone the extra mile in testing the thing. https://www.techgearlab.com/reviews/wearable-tech/fitness-tracker/letscom-id115plus-hr They seem to be saying that it's basically an illuminated plastic bracelet.

It has a couple sensors though and can vibrate. I'd be happy to turn it into a pomodoro timer. https://en.wikipedia.org/wiki/Pomodoro_Technique

# Smart Watch

What I really need is a cheap programmable watch like

PineTime
https://wiki.pine64.org/index.php/PineTime
https://hackaday.com/2019/10/07/ask-hackaday-whats-the-perfect-hacker-smart-watch/

or Open-SmartWatch
https://open-smartwatch.github.io/
https://hackaday.com/2021/04/08/an-open-source-smart-watch-youd-actually-wear/

or even BangleJS https://banglejs.com/ (which seems very inefficient, with JS and always-on LCD, and how they don't even mention average battery life for normal use).

I need the thing so I can make my parents' home a little smarter. For example, I would like to make sure my parents dont' forget to turn off the stove before leaving the house. I want my father, who is becoming sedentary due to his bad knees, to have a dashboard-like overview of every critical device that is running in their house. Stuff like that.

# Bluetooth

I'm looking for bluetooth libs for Python to do some tests. ____bluepy____ https://github.com/IanHarvey/bluepy looks abandoned but ____bleak____ https://github.com/hbldh/bleak seems like the way to go. https://bleak.readthedocs.io/

Found a nice-looking tutorial https://people.csail.mit.edu/albert/bluez-intro/ for Bluez https://github.com/bluez/bluez .

https://www.bluetooth.com/blog/a-developers-guide-to-bluetooth/

# Partial upgrades are unsupported

My repositories have changed so I'm upgrading the system. There was an issue with `ruby-rexml`. I had to `pacman -Qo` https://wiki.archlinux.org/title/Pacman#%22Failed_to_commit_transaction_(conflicting_files)%22_error to check whether the files belonged to a tracked package before deleting them. I don't use Ruby and only had it installed to try out Jekyll because GH Pages was harping on about it. Obviously I don't think much of it. I like my bespoke solution better. The Ruby crowd is an interesting bunch but I don't see the point in learning any of it now.

# Alias

I have an alias set so I don't forget to do a "full" upgrade: `pacman -Syu`.  https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported I've just had to add an alias for `pacman -Sy archlinux-keyring` as well.

# Todo

DaFit Fitness Tracker firmware update protocol: https://gist.github.com/atc1441/32c940522ba7470a56c23922341ca25a . This guy! https://gist.github.com/atc1441 . But always beware of bricking your device: https://gist.github.com/atc1441/d0a3c1f5ee69ab901bccba4eb47a6e4e .

# Stuff

Espruino is a JavaScript interpreter for microcontrollers. It can fit into devices with as little as 128kB Flash and 8kB RAM.
https://github.com/espruino
http://www.espruino.com/Order
https://www.espruino.com/Reference
https://webbluetoothcg.github.io/web-bluetooth/

Espruino oscilloscope example https://github.com/espruino/webaudio-oscilloscope

The ground-breaking bluetooth beacon - An Open Source JavaScript microcontroller you can program and debug wirelessly http://www.puck-js.com/

The World's first Open Source Hackable Smart Watch
https://banglejs.com/
https://shop.espruino.com/banglejs2

nRF52832 Bluetooth Low Energy Module
https://www.adafruit.com/product/4077
https://www.nordicsemi.com/Products/nRF52832

The fastest, most flexible 2D WebGL renderer https://pixijs.com/
https://pixijs.download/v7.3.0-rc.2/docs/index.html



# Intermission

I've tried Gadgetbridge https://f-droid.org/en/packages/nodomain.freeyourgadget.gadgetbridge/ but it wants too many permissions and, worst of all, keeps nagging. https://codeberg.org/Freeyourgadget/Gadgetbridge

F-Droid wouldn't update Feeder nor Forkyz so I duckducked https://forum.f-droid.org/t/updates-not-updating/20386 and they referred to https://dontkillmyapp.com/huawei . Still no luck. Might have to update F-Droid itself.


# TIL

Something called the Open Collective https://opencollective.com/ .

Also it bothers me that Location has to be on for Bluetooth LE scanning to work.

https://android.stackexchange.com/questions/160479/why-do-i-need-to-turn-on-location-services-to-pair-with-a-bluetooth-device#186471

https://issuetracker.google.com/issues/37060483

https://issuetracker.google.com/issues/169936948

"""You can definitely track a device by inferring what Bluetooth devices or Wi-Fi networks are nearby or are currently connected. So even if an app just scans for Bluetooth devices and doesn't utilize GPS or other tracking technologies, it still needed the same Location permission nonetheless." --- https://www.xda-developers.com/android-12-location-scan-nearby-bluetooth-devices/ """

Kudos to these guys:

"""The goal of this project is the creation of an easy to use, mostly plug-and-play, JTAG/SWD debugger for embedded microcontrollers. The project focuses on professional embedded software developers that prefer retaining control over their build systems and testing environments ____instead of relying on highly abstracted vendor tools that give the impression of simplicity at the cost of transparency____. --- https://black-magic.org/ """

Need to check this out. **Contagio** Malware Dump https://contagiodump.blogspot.com/ .

I've stumbled upon **roboflow** just now. In particular this chess object detection blog entry https://blog.roboflow.com/training-a-yolov3-object-detection-model-with-a-custom-dataset/ . Good to know somebody is doing work on this. It's something every chess player who can't afford a DGT board has been thinking of. We still don't have a good tool to flatten chess videos into PGNs. Last time I've pondered doing this was when I was trying to get motivated enough to delve into ML, but players in my club don't really like to have cameras around. A less paranoia-inducing solution would be to use what they have in some cheap (non-mechanical) keyboards (a three-foil-sandwich where the two outer ones get pressed together and a current flows https://www.digikey.com/en/maker/projects/make-a-custom-membrane-keypad-for-arduino/4988a4a4e78a495d8d03212e1e5aee9e https://hackaday.com/2015/01/25/making-membrane-keypads-from-scratch/ ) and to spread that across the board. Also a custom board can be built with IR LEDs and LDRs to detect the presence and absence of pieces. Still, something like this, requiring just a simple camera, definitely would be nice to have. I've booked up on OpenCV years ago but still no motivation. That whole AI craze is swooshing by me. It's ironic, but that's another story.

https://www.kaggle.com/datasets/ninadaithal/chess-pieces-dataset
https://huggingface.co/datasets/jalFaizy/detect_chess_pieces

https://blog.roboflow.com/labelimg/
https://public.roboflow.com/object-detection/chess-full
https://public.roboflow.com/object-detection/chess-full/24

Grown and made in Hokkaido, Japan https://tozandoshop.com/ .

Sad https://www.themoviedb.org/movie/424609 . Fun https://web-japan.org/kidsweb/local/wanko-soba/ . Yummy https://www.justonecookbook.com/cold-noodles/ https://www.bosh.tv/recipes/quick-chick-soba-bowl https://bowlsarethenewplates.com/sesame-soba-noodles/ .

# Apparently

Apparently https://www.apkmirror.com/ is managed by the https://www.androidpolice.com/ guys: https://android.stackexchange.com/questions/135711/is-apkmirror-com-safe . But it only mirrors free apps and so it didn't have the two apks I wanted to look into.

# First Steps First

I've got the Nordic Semiconductor's Bluetooth sniffer https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-desktop .

It's a really nice application that I would love to replicate from the console. (I will probably be able to do it quickly with `python-bleak` but the lib feels more sluggish compared to my C experiments.) This great little sniffer though is showing me all the endpoints of my watch.

```perl
Generic Address
UUID: 0x1800
PRIMARY SERVICE

	Device Name
	UUID: 0x2A00
	Properties: READ, WRITE

	Appearance
	UUID: 0x2A01
	Properties: READ

	Peripheral Preferred Connection Par...
	UUID: 0x2A04
	Properties: READ

Generic Attribute
UUID: 0x1801
PRIMARY SERVICE

	Service Changed
	UUID: 0x2A05
	Properties: INDICATE
	Descriptors:
	Client Characteristic Configuration
	UUID: 0x2902

Unknown Service
UUID: 0x0AF0
PRIMARY SERVICE

	Unknown Characteristic
	UUID: 0x0AF6
	Properties: READ, WRITE

	Unknown Characteristic
	UUID: 0x0AF7
	Properties: NOTIFY, READ
	Descriptors:
	Client Characteristic Configuration
	UUID: 0x2902

	Unknown Characteristic
	UUID: 0x0AF2
	Properties: NOTIFY, READ
	Descriptors:
	Client Characteristic Configuration
	UUID: 0x2902

	Unknown Characteristic
	UUID: 0x0AF1
	Properties: READ, WRITE
```

My watch can only measure heart-rate and step-count and there seems to be no way to set the clock via the single button on the physical watch.

Given that there are so many different watches that a fitness app needs to support, we can deduce that all of this data will go through the same endpoints and that there must be some protocol underlying the exchange.

That protocol being proprietary, this is where we need to take a look at the apks of the fitness app(s) that can speak to my particular watch.

# Further Steps

I've downloaded VeryFitPro and Letsfit App from https://apkcombo.com/ which is shady, but I didn't want to install them from the google store and then `adb pull` the apks. https://www.evilsocket.net/2017/04/27/Android-Applications-Reversing-101/

```shell
> adb shell pm list packages
> adb shell pm path com.android.systemui
> adb pull /system/priv-app/SystemUIGoogle/SystemUIGoogle.apk
```

I was reading a bit of background info, overviews about best-practice for reversing android java.

https://www.evilsocket.net/2017/04/27/Android-Applications-Reversing-101/

https://braincoke.fr/blog/2021/03/android-reverse-engineering-for-beginners-decompiling-and-patching/#lab-setup

http://d-kovalenko.blogspot.com/2012/08/debugging-smali-code-with-apk-tool-and.html

# Tentative Steps

I haven't dabbled with the Android NDK yet and it's time I did. https://developer.android.com/ndk/guides/other_build_systems It might be the proper way in for me because both the (slow, slooooow) Android Studio and the Books I have take too high a vantage point with lots of hand-holding and dubious didactic scaffolding. A **really good** book on anything would start with the absolute minimum app https://github.com/czak/minimal-android-project . A proper Hello World. But to do this people actually need to know what they are doing, instead these books are written quickly, strictly for the money, and by high-functioning imbeciles. Which reminds me:

""" Alienists have frequently come to ... accept idiot as applied to the lowest state, imbecile to the intermediate, and moron (debile) to the state nearest normality. --- https://archive.org/details/developmentofint00bineuoft/page/10/mode/1up """

Sorry, this was my frustration talking. Aspire to be a moron among imbeciles.

Anyway, to get things going, first I want to write a little command line app to call into from the `adb shell`. Which means cross-compiling to `aarch64`. Which means downloading more stuff.

# Layers

There are `lib/` folders in both those apk. There are shared native libraries inside which look like they might contain the real logic of key functionality. This would be great because I could completely ignore anything to do with Android.

As an #aside, I'm worrying about `radare2` for static analysis because it has debugging functionality, so it could try to execute the binaries. Here it doesn't matter since it's on the wrong architecture but, in general, I don't see anything that would make it run things in a sandbox https://book.rada.re/first_steps/commandline_flags.html . I need a good go-to disassembler (though `objdump` with coloring will do). Sure, radare looks great and could be immensly useful but I really need to be reassured here. If only there were an obvious option. Instead, it seems, you need to take constant care to not type the wrong letter. Worst case I'll have to spin up a VM or run it in a codespace. Just to calm the nerves.

```
$ r2 /bin/ls   # open file in read-only
> aaa          # analyse the program (r2 -A)
> afl          # list all functions (try aflt, aflm)
> px 32        # print 32 byte hexdump current block
> s sym.main   # seek to main (using flag name)
> f~foo        # filter flags matching 'foo' (internal |grep)
> iS;is        # list sections and symbols (rabin2 -Ss)
> pdf; agf     # disassembly and ascii-art function graph
> oo+;w hello  # reopen in read-write and write a string
> ?*~...       # interactive filter in all command help
> q            # quit
```

Ok, forgive me sensei. Radare2 with **iaito** is fantastic https://github.com/radareorg/iaito#readme . Not as nice as SoftIce (R.I.P.) but just as good as IDA Free (which doesn't do ARM). https://hex-rays.com/ida-free/

# Strings

I'm looking through `strings lib/arm64-v8a/libVeryFitMulti.so`. Yes, they didn't care to `strip` their binaries. Already the first few lines seem to be function names related to bluetooth (audio) transfer (the Subband Codec Library). https://en.wikipedia.org/wiki/SBC_%28codec%29 , see them used here https://github.com/bluez/bluez/blob/530afa43ec2920347c7092823bec8fd51b019280/android/hal-audio-sbc.c#L243 download old sources here http://www.bluez.org/sbc-13/ . There follows a (C++ mangled) JSON library, an AES crypto library, etc. Then there is a funny typo `jni_attack_thread` (as complement to `jni_detach_thread`), and then we find such strings as this `Java_com_veryfit_multi_nativeprotocol_Protocol_ReceiveDatafromBle` and `protocol_set_alarm_start_sync` which seem promising. By the looks of all the boilerplate they really haven't gone for minimalism here.

# The Evolution of the Arm

I'll have to refresh my RISC reading and comprehension. https://developer.arm.com/documentation/100076/0200/?lang=en At uni they wanted us to buy Nintendos so we could have a nice ARM platform to do our homework on. Instead I began writing an ARM emulator so I didn't have to spend the bucks. Also because I had to learn Java and that was a nice project to learn it for. It worked. Got the highest grade on my MCU exam. Loved the architecture. Barrel shifter and all. And now? Forgot everything. Well almost all, for how could I ever forget the lovely Sophie Wilson? https://en.wikipedia.org/wiki/Sophie_Wilson .

# Strike #3

The problem here is threefold. 1. I have never programmed for Android, so I don't have any pattern recognition there. 2. My ARM days were few and are long past, so I retain no real understanding here. I struggle to remember which is the source and which the target register for many of the operations. I don't know any of the patterns here either. 3. I am just beginning to get interested in Bluetooth. So what follows is conjecture.

# Thoughts

In the Letsfit App at `0x002a0e03` there's a string table. Could be that these strings are sent over BT. That is, maybe the BT functions like a wireless serial interface or something (UART https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter ). Could be they are just used as the keys in the creation of a JSON string with `jni_json_get_init`.

There's an interesting string being used at `0x0016fdb0`: ""clean cur sync data,status"" which certainly looks like a command you'd send over a serial interface. This is what I'm hoping, really. That there's a very simple protocol and then a bunch of command strings on top of that. It's part of the `str._PROTOCOL_HEALTH_` string table which begin at `0x002a7afc`. Could be this is just for internal debug output. Even so, this is a good starting point to try and trace back where the data's coming from.

I've seen what appears to be a JSON parser, using C++'s regex library. https://en.cppreference.com/w/cpp/regex/sub_match Seems they're also using a logging library https://github.com/gabime/spdlog .

# Merits further study

```
protocol_health_exec

send_ble_data_resend

protocol_write_init
protocol_write_set_head
protocol_write_set_cmd_key
protocol_write_data

Java_com_veryfit_multi_nativeprotocol_Protocol_StartSyncConfigInfo

jni_notice_app_tx_data
sbc_decode

vbus_tx_data
```

# Sidenotes

In VeryFitPro they included a zip library https://www.winimage.com/zLibDll/minizip.html . And a jpeg-turbo port https://github.com/Curzibn/Luban-Turbo .

Also this selection of external services is vaguely interesting, probably because I've never heard of most of those providers before.

```
notice_TikTok
notice_Redbus
notice_Dailyhunt
notice_Hotstar
notice_Inshorts
notice_Paytm
notice_Amazon
notice_Flipkart
notice_Prime
notice_Netflix
notice_Gpay
notice_Phonpe
notice_Swiggy
notice_Zomato
notice_Make_My_Trip
notice_Jio_Tv
```

"""
Dailyhunt is an **Indian** content and news aggregator... ///
Hotstar is an **Indian** brand of subscription video on-demand... ///
Inshorts ... we cut the clutter and deliver [news] in 60-word shorts. ///
Paytm is an **Indian** ... company that specializes in digital payments... ///
PhonePe is an **Indian** digital payments and financial services company... ///
Swiggy is an **Indian** online food ordering and delivery platform. ///
Zomato is an **Indian** multinational restaurant aggregator and food delivery company. ///
MakeMyTrip is an **Indian** online travel company... ///
Jio TV is an **Indian** streaming television service...
"""

# Tools

https://www.kali.org/tools/kali-meta/#kali-tools-reverse-engineering
https://www.blackarch.org/reversing.html
https://linuxsecurity.expert/security-tools/linux-reverse-engineering-tools

Free and Open Source Reverse Engineering Platform powered by rizin
https://github.com/rizinorg/cutter


**APKTool** A tool for reverse engineering Android apk files
https://apktool.org/
https://www.kali.org/tools/apktool/ .

**smali/baksmali** is an assembler/disassembler for the dex format used by dalvik, Android's Java VM implementation
https://github.com/JesusFreke/smali .

**jadx** Dex to Java decompiler https://github.com/skylot/jadx .

**bettercap** The Swiss Army knife for 802.11, BLE, IPv4 and IPv6 networks reconnaissance and MITM attacks.
https://github.com/bettercap/bettercap
https://www.kali.org/tools/bettercap/ .

**Frida** Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers https://frida.re/ .

**Androguard** "Reverse engineering and pentesting for Android applications" (static analysis)
https://github.com/androguard/androguard
https://androguard.readthedocs.io/en/latest/ .

**Droidbox** Dynamic analysis of Android apps
https://github.com/pjlantz/droidbox .

**cuckoo-droid** Open Source software for automating analysis of suspicious files
https://github.com/idanr1986/cuckoo-droid
https://cuckoo-droid.readthedocs.io/en/latest/
http://cuckoo.readthedocs.org/ .

Python scriptable Reverse Engineering Sandbox, a Virtual Machine instrumentation and inspection framework based on QEMU https://github.com/Cisco-Talos/pyrebox .

## Disassemblers
**YZDIS** The ultimate, open-source X86 & X86-64 decoder/disassembler library
https://github.com/zyantific/zydis
https://zydis.re/

**Capstone** is a lightweight multi-platform, multi-architecture disassembly framework
https://github.com/capstone-engine/capstone
https://www.capstone-engine.org/
https://pypi.org/project/capstone/ .

Cross platform library which can parse, modify and abstract ELF, PE and MachO formats https://github.com/lief-project/LIEF .

## Debuggers
KGDB https://en.wikipedia.org/wiki/KGDB
LLDB https://lldb.llvm.org/ .

**radare** https://www.radare.org/r/
https://book.rada.re/first_steps/intro.html
https://github.com/radareorg/iaito
https://en.wikipedia.org/wiki/Radare2
.

**REDasm**
https://github.com/REDasmOrg/REDasm
https://github.com/REDasmOrg/REDasm-Library/tree/master
https://redasm.io/roadmap

## Fiddlers
https://godbolt.org/
https://www.onlinegdb.com/ .

## Forensics
**Contagio** Malware Dump https://contagiodump.blogspot.com/ .

**SSDEEP** Fuzzy hashing https://www.kali.org/tools/ssdeep/ .

## OAuth

A zero trust swiss army knife for working with X509, OAuth, JWT, OATH OTP, etc. https://github.com/smallstep/cli .

## Other

**infinitime** An open source firmware for the Pinetime https://infinitime.io/ .

**OpenOCD** the Open On-Chip Debugger https://openocd.org/ .


# Misc

Xposed https://www.xda-developers.com/edxposed/

https://forum.xda-developers.com/t/magisk-xposed-framework-is-installed-but-not-active-xposedbridge-jar-lacking.4204875/

https://stackoverflow.com/questions/40300515/how-does-snapchat-detect-xposed-framework

https://developer.android.com/training/safetynet/deprecation-timeline

https://developer.android.com/google/play/integrity


! blurb = You just ain't receiving. (Bjork)
! header-color = greenyellow
! gradient-top = #032
! gradient-bottom = #450
