import launchpad_py as launchpad
from time import sleep


def main():

    lp = launchpad.LaunchpadMk2()
    if lp.Open(0):
        print("Launchpad Mk2")
        mode = 'mk2'

    while True:
        buts = lp.ButtonStateXY()
        
        if buts != []:
            x = buts[0]
            y = buts[1]
            p = buts[2]

            if p == 0:
                lp.LedCtrlXYByCode(x,y,0)
            else:
                lp.LedCtrlXYByCode(x,y,60)    


        
            

        if buts == [8,8,0]:
            break

    lp.Reset()
    lp.Close()





if __name__ == '__main__':
    main()