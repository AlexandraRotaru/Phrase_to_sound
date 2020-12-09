import sys
import os
from gtts import gTTS


def readFiles():
    if os.path.isdir(input) and os.path.isdir(output):
        for root, directories, files in os.walk(input):
            for file in files:
                full_path = os.path.abspath(os.path.join(root, file))

                try:
                    f = open(full_path, "r")
                    line = f.readline()

                    if line:
                        speech = gTTS(line, lang='en', slow=False)
                        path_for_output = os.path.abspath(os.getcwd()) + "/" + output + "/" + file.split(".")[0];
                        speech.save(path_for_output + ".mp3")

                    f.close()

                except:
                    print("The file could not be open.")


if __name__ == "__main__":
    input = sys.argv[1]
    output = sys.argv[2]
    readFiles()
