import launchpad_py as launchpad
from time import sleep


class key:          # top row keys

    up_r = [0,0,0]      # up relased
    down_r = [1,0,0]        # down relased
    left_r = [2,0,0]        # left relased
    right_r = [3,0,0]       # right relased
    session_r = [4,0,0]        # session relased
    user1_r = [5,0,0]       # user1 relased
    user2_r = [6,0,0]       # user2 relased
    mixer_r = [7,0,0]       # mixer relased

def main():
    lp = launchpad.LaunchpadMk2()               # defines launchpad as lp
    if lp.Open(0):                  # checks if launchpad works
        print("Launchpad Mk2")          
        mode = "Mk2"            # DO NOT TOUCH THIS


    # Checks For Button Press

    x = 3
    y = 4
    
    lp.LedCtrlXYByCode(3,4,60)

    while True:

        buts = lp.ButtonStateXY()
        if buts == [8,8,0]:             # quits the program
            break

        if buts == key.up_r:
            lp.Reset()
            y -= 1
            lp.LedCtrlXYByCode(x,y,30)

        if buts == key.down_r:
            lp.Reset()
            y += 1
            lp.LedCtrlXYByCode(x,y,30)

        if buts == key.left_r:
            lp.Reset()
            x -= 1
            lp.LedCtrlXYByCode(x,y,30)

        if buts == key.right_r:
            lp.Reset()
            x += 1
            lp.LedCtrlXYByCode(x,y,30)        

    lp.Reset()          # resets launchpad grid
    lp.Close()          # closes pygame and program


if __name__ == '__main__':          # main loop
    main()