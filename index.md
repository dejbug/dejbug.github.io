# Time

I am on the clock. Waiting for my friend to call so we can go help her get some furniture from A to B. B being a much nicer place than A.

# Waiting

I don't really know what to do with myself while waiting. I can't really concentrate on anything. I can't say I like the feeling. I feel pointless.

# But anyway

There's things I need to do but I keep getting distracted left and right. I decided to just let the distraction happen. Let the chaos in. If I were just bit more organized it wouldn't be so disorientating.

# Back home

I've done my duty and now I'm back and showered and relaxed. The day is mine again. There will be no distractions. I had been looking forward to a little heavy lifting but all of it was so unrewardingly easy that I regretted getting out of bed. Walking there was more exhausting to me than the actual job awaiting me there. It's the people out there with their cars and the commotion and the noise. I can't believe that people thrive out there. It's a witch's brew of mindaltering ingredients. I'm on an adrenaline high while I'm out there. I feel numb when I get home. I don't like leaving home. There's really nothing out there for me, nothing at all. I like my friends but this is not worth that.

# TOC Issue

There's a problem with my `toc.js` on Firefox for Android. I noticed it after publishing last night's blog and re-reading it in bed. When scrolling the page back upwards, FFfA will show the address bar, so the `clientHeight` is smaller than when scrolling down while reading. This will wreak havoc with my positioning. I need to test this. Maybe using `svh` versus `slh` units is a simple fix.

# Bluetooth on the radar

I've got myself a fitness watch. Cue for laughter. A cheap one just to have a closer look at one. It's been lying around for a while now and its time to put it to some use. Hopefully an unintended one. But first...

# I love you but I forgot your name

```bash
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

I need the thing so I can make my parents' home a little smarter. For example, I would like to make sure my parents dont' forget to turn off the stove before leaving the house. I want my father, who is becoming sedentary due to his bad knees, to have a dashboard-like overview of every critical device that is running in his house. Stuff like that.

# Bluetooth

I'm looking for bluetooth libs for Python to do some tests. ____bluepy____ https://github.com/IanHarvey/bluepy looks abandoned but ____bleak____ https://github.com/hbldh/bleak seems like the way to go. https://bleak.readthedocs.io/

Found a nice-looking tutorial https://people.csail.mit.edu/albert/bluez-intro/ for Bluez https://github.com/bluez/bluez .

https://www.bluetooth.com/blog/a-developers-guide-to-bluetooth/

# Partial upgrades are unsupported

My repositories have changed so I'm upgrading the system. There was an issue with `ruby-rexml`. I had to `pacman -Qo` https://wiki.archlinux.org/title/Pacman#%22Failed_to_commit_transaction_(conflicting_files)%22_error to check whether the files belonged to a tracked package before deleting them. I don't use Ruby and only had it installed to try out Jekyll because GH Pages was harping on about it. Obviously I don't think much of it. I like my bespoke solution better. The Ruby crowd is an interesting bunch but I don't see the point in learning any of it now. ///
///
I have an alias set so I don't forget to do a "full" upgrade: `pacman -Syu`.  https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported I've just added an alias for `pacman -Sy archlinux-keyring` as well.


# Todo

DaFit Fitness Tracker firmware update protocol: https://gist.github.com/atc1441/32c940522ba7470a56c23922341ca25a . This guy!: https://gist.github.com/atc1441 . But always beware of bricking your device: https://gist.github.com/atc1441/d0a3c1f5ee69ab901bccba4eb47a6e4e .


# Stuff

Espruino is a JavaScript interpreter for microcontrollers. It can fit into devices with as little as 128kB Flash and 8kB RAM.
https://github.com/espruino
http://www.espruino.com/Order
https://www.espruino.com/Reference
https://webbluetoothcg.github.io/web-bluetooth/

This is cool: https://github.com/espruino/webaudio-oscilloscope

The ground-breaking bluetooth beacon - An Open Source JavaScript microcontroller you can program and debug wirelessly. http://www.puck-js.com/

The World's first Open Source Hackable Smart Watch
https://banglejs.com/
https://shop.espruino.com/banglejs2

nRF52832 Bluetooth Low Energy Module https://www.adafruit.com/product/4077

Create beautiful digital content with the fastest, most flexible 2D WebGL renderer. https://pixijs.com/
https://pixijs.download/v7.3.0-rc.2/docs/index.html



# Intermission

I've tried Gadgetbridge https://f-droid.org/en/packages/nodomain.freeyourgadget.gadgetbridge/ but it wants too many permissions and, worst of all, keeps nagging. https://codeberg.org/Freeyourgadget/Gadgetbridge

Fdroid wouldn't update a Feeder nor Forkyz so I duckducked https://forum.f-droid.org/t/updates-not-updating/20386 and they referred to https://dontkillmyapp.com/huawei .


# TIL

https://opencollective.com/


# Apparently

Apparently https://www.apkmirror.com/ is managed by the https://www.androidpolice.com/ guys: https://android.stackexchange.com/questions/135711/is-apkmirror-com-safe . But it only mirrors free apps and so it didn't have the two apks I wanted to look into.


# First Steps

I've got Nordic Semiconductor's Bluetooth sniffer https://www.nordicsemi.com/Products/Development-tools/nRF-Connect-for-desktop . It bothers me that Location has to be on for Bluetooth LE scanning to work.

It's a great app that I would love to replicate from the console. (I will probably be able to do it quickly with `python-bleak` and not have to write C.) It shows me all the endpoints of my watch.

The most interesting ones are vendor-specific and their function unknown. We can deduce that some will be for heartrate measurements and notifications thereof. Some of those endpoints are writable as well as readable. Seeing how there seems no way to set the clock via the single button on the physical watch, there must be a way to set it by writing to these ports. But in what format? This is where we need to take a look at the apks of the fitness apps that speak to my watch.

# Further Steps

I've downloaded VeryFitPro and Letsfit App from https://apkcombo.com/ which is shady, but I didn't want to install them from the google store and then `adb pull` the apks.

I was reading a bit of background info, overviews about best-practice for reversing android java.

https://www.evilsocket.net/2017/04/27/Android-Applications-Reversing-101/

https://braincoke.fr/blog/2021/03/android-reverse-engineering-for-beginners-decompiling-and-patching/#lab-setup

http://d-kovalenko.blogspot.com/2012/08/debugging-smali-code-with-apk-tool-and.html


# Tools

An open source firmware for the Pinetime https://infinitime.io/

OpenOCD, the Open On-Chip Debugger https://openocd.org/

A tool for reverse engineering Android apk files
https://apktool.org/
https://www.kali.org/tools/apktool/

The Swiss Army knife for 802.11, BLE, IPv4 and IPv6 networks reconnaissance and MITM attacks.
https://github.com/bettercap/bettercap
https://www.kali.org/tools/bettercap/

Dynamic instrumentation toolkit for developers, reverse-engineers, and security researchers. https://frida.re/

Dex to Java decompiler https://github.com/skylot/jadx

Open Source software for automating analysis of suspicious files
https://github.com/idanr1986/cuckoo-droid
http://cuckoo.readthedocs.org/
https://cuckoo-droid.readthedocs.io/en/latest/

https://en.wikipedia.org/wiki/Radare2
https://en.wikipedia.org/wiki/KGDB
https://lldb.llvm.org/

https://godbolt.org/
https://www.onlinegdb.com/


# Misc

https://www.xda-developers.com/edxposed/

https://forum.xda-developers.com/t/magisk-xposed-framework-is-installed-but-not-active-xposedbridge-jar-lacking.4204875/

https://stackoverflow.com/questions/40300515/how-does-snapchat-detect-xposed-framework

https://developer.android.com/training/safetynet/deprecation-timeline

https://developer.android.com/google/play/integrity


! blurb = Is it me or my ego? (Nirvana)
! header-color = greenyellow
! gradient-top = #032
! gradient-bottom = #450
