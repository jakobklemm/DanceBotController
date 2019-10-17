from tkinter import *
from tkinter import ttk
from threading import Thread
from playsound import *
import pyglet


leftLed = "left_led.wav"
leftAudio = "left.wav"

rightLed = "right_led.wav"
rightAudio = "right.wav"

forwardLed = "forward_led.wav"
forwardAudio = "forward.wav"

backwardsLed = "back_led.wav"
backwardsAudio = "back.wav"

idleLed = "idle_led.wav"
idleAudio = "init.wav"


def sound(path):
    playsound(path, True)

    """
    music = pyglet.media.load(path)
    music.play()

    """


def end():
    window.destroy()


window = Tk()

# playsound.playsound(forwards_led, True)
window.title("DanceBot Controller")
window.resizable(False, False)
window.minsize(450, 450)
window.configure(background='#F2F2F2')

header = Label(window, text="DanceBot Controller V1")
header.place(relx=.5, rely=.1, anchor="c")

author = Label(window, text="© Dominik Keller & Jakob Klemm")
author.place(relx=.79, rely=.98, anchor="c")

left = ttk.Button(window, text="Left")
left.place(relx=.5 - .2, rely=.5, anchor="c")

right = ttk.Button(window, text="Right")
right.place(relx=.5 + .2, rely=.5, anchor="c")

forward = ttk.Button(window, text="Forward")
forward.place(relx=.5, rely=.5 - .2, anchor="c")

backwards = ttk.Button(window, text="Backwards")
backwards.place(relx=.5, rely=.5 + .2, anchor="c")

idle = ttk.Button(window, text="Idle")
idle.place(relx=.5, rely=.5, anchor="c")

close = ttk.Button(window, text="Close", command=end)
close.place(relx=.4, rely=.9, anchor="c")

led = ttk.Checkbutton(window, text="Enable LED's")
led.place(relx=.6, rely=.9, anchor="c")


def checks():
    leds = False
    ledState = led.state()
    if 'selected' in ledState:
        leds = not leds
    leftState = left.state()
    if 'pressed' in leftState:
        if leds:
            sound(leftLed)
        else:
            sound(leftAudio)
    rightState = right.state()
    if 'pressed' in rightState:
        if leds:
            sound(rightLed)
        else:
            sound(rightAudio)
    forwardState = forward.state()
    if 'pressed' in forwardState:
        if leds:
            sound(forwardLed)
        else:
            sound(forwardAudio)
    backState = backwards.state()
    if 'pressed' in backState:
        if leds:
            sound(backwardsLed)
        else:
            sound(backwardsAudio)
    idleState = idle.state()
    if 'pressed' in idleState:
        if leds:
            sound(idleLed)
        else:
            sound(idleAudio)


def main():
    playsound(idleAudio, True)
    t = Thread(target=checks, args=())
    while 1:
        checks()
        window.update()


if __name__ == '__main__':
    main()
