# Raspberry Pi Project
## Light And Sound
### Student Number 1234567

#### Introduction
The motivation for this project was to create an "audio" and "visual experience".
That is, to create something that exists in real life rather than just an app.
The idea for this project was to make a Raspberry Pi turn on a light and read out a tweet from a designed user.
Then, one the tweet is read out, the light turns off.

### SAFETY!
NOTE: Working with 240 V Mains is dangerous and so all work with the Mains was carried out in class and under teacher supervision only! No work with the Mains was done at home!

### Physical - Construction
The Raspberry Pi is a micro-computer than runs an operating system known as Raspbian (which is a Linux distro).
It was necessary to flash the SD card with Raspbian and save the wi-fi login details to the boot drive as the system would be headless.
It was rather difficult to get the pi connected to the wi-fi network but once connected it was possible to connect to the pi via the terminal.
From here the code could be uploaded and with the use of RC Local the code was set to run every time on boot.
The Pi also has a "hat" which sits on the GPIO pins and could be used as a relay switch.
A light-build socket was wired up to the replay switch and usb powered speaker was connected to the 3.5 mm audio jack with the pi's usb port powering the speaker.

### Virtual - The Code
Tweepy was used to scrape the tweets and Google was used to read the tweets out as it had the nicest voice to it.
However, regardless of which text reader was used they all had a problem. The speaker would cut off the start of the text. This was likely due to the speaker needing time to turn on when text was being ready. The solution was to have the speaker play a very quiet sound before reading the text.
This was the speaker was "woken up" before the text was read.


### Ideas for Version 2
Now that the Pi can read tweets and turn the light on and off it is possible to have it do more with ease.
For example, the Pi could turn the light on or off with a single tweet like "Leave light on" or "Leave light off".
Now that the speaker is working it could be used as a radio via a tweet like "Play radio" or "Stop radio".
The light could even be used for Morse code i.e. if "Morse: Hello World" was tweeted then the Pi could flash out "Hello World" in Morse code.
The "hard" part is done and now it is wide open to add more features in.


### Conclusion
In the end, the project worked. Whenever a tweet was made the Pi would turn the light on, the tweet would be read and then the light would turn off.
What is not seen in the project is the amount of work needed to get the Pi working and wired up.
The physical element was time-consuming but now that it is completed the Pi can be expanded on by simply updating the code.
[https://youtu.be/BuZpbb6ICNs](https://youtu.be/BuZpbb6ICNs)