import sys
import os
from gtts import gTTS


def readFiles():
    if os.path.isdir(inputDir) and os.path.isdir(outputDir):
        for root, directories, files in os.walk(inputDir):
            for file in files:
                full_path = os.path.abspath(os.path.join(root, file))

                try:
                    f = open(full_path, "r")
                    line = f.readline()

                    if line:
                        speech = gTTS(line, lang='en', slow=False)
                        path_for_output = os.path.abspath(os.getcwd()) + "/" + outputDir + "/" + str(file.split(".")[0])
                        speech.save(path_for_output + ".mp3")

                    f.close()

                except Exception as e:
                    print("Error: " + str(e))


if __name__ == "__main__":
    inputDir = sys.argv[1]
    outputDir = sys.argv[2]
    readFiles()
