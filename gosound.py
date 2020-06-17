def go(sound: str, play_sec: tuple):
    """
    sound:str = path to file | directory:/folder/folder2/file
    play_sec:tuple = (1.4:int/float, 5:int/float)

    /////////////////////////////////////////////////////////
    HINTS:
    
    In variable play_sec decimal float numbers must be less than 3 digits.

    Lib working only in WINDOWS OS.

    /////////////////////////////////////////////////////////
    """
    from ctypes import c_buffer, windll
    from random import random
    from sys    import getfilesystemencoding

    def winCommand(*command):
        buf = c_buffer(255)
        command = ' '.join(command).encode(getfilesystemencoding())
        errorCode = int(windll.winmm.mciSendStringA(command, buf, 254, 0))

    alias = 'playsound_' + str(random())
    winCommand('open "' + sound + '" alias', alias)
    winCommand('set', alias, 'time format milliseconds')
    winCommand('play', alias, f'from {str(int(play_sec[0]*1000))} to {str(int(play_sec[1]*1000))}')

if __name__ == '__main__':
    print("V1.0 | SUPPORT OS: \n1)Windows\n/Author: @BTDIZP/GitHub rep: ")