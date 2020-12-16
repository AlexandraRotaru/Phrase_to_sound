import tkinter as tk

import playsound
from gtts import gTTS
from random import randint


def generateRandomName():
    ch = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
    randomName = ""

    for i in range(randint(5, 15)):
        randomName += ch[randint(0, len(ch) - 1)]

    return randomName


def play():
    phrase = phrase_typed.get().strip()

    if phrase:
        speech = gTTS(phrase, lang='en', slow=False)
        randomName = generateRandomName()
        path = "/Users/alexandra-beatricerotaru/Desktop/Phrase_to_sound/output/" + randomName + ".mp3"

        speech.save(path)

        playsound.playsound(path)


def userInterface():
    global phrase_typed

    window = tk.Tk()

    frame = tk.Frame(window)
    frame.pack(padx=30, pady=30)

    title = tk.Label(frame,
                     text="Phrase to sound Application",
                     foreground="red")
    title.pack()

    instruction = tk.Label(frame,
                           text="Enter a phrase.")
    instruction.pack()

    phrase_typed = tk.Entry(frame)
    phrase_typed.pack()

    play_button = tk.Button(frame,
                            text="Play",
                            command=play)
    play_button.pack()

    # mainloop() is used when your application is ready to run. mainloop() is an infinite loop used to run the
    # application, wait for an event to occur and process the event as long as the window is not closed.
    window.mainloop()


if __name__ == "__main__":
    userInterface()
