import pigo
import time
import random

'''
MR. A's Final Project Student Helper
'''

class GoPiggy(pigo.Pigo):

    ########################
    ### CONTSTRUCTOR - this special method auto-runs when we instantiate a class
    #### (your constructor lasted about 9 months)
    ########################

    def __init__(self):
        print("Your piggy has be instantiated!")
        # Our servo turns the sensor. What angle of the servo( ) method sets it straight?
        self.MIDPOINT = 90
        # YOU DECIDE: How close can an object get (cm) before we have to stop?
        self.STOP_DIST = 30
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.LEFT_SPEED = 140
        # YOU DECIDE: What left motor power helps straighten your fwd()?
        self.RIGHT_SPEED = 140
        # This one isn't capitalized because it changes during runtime, the others don't
        self.turn_track = 0
        # Our scan list! The index will be the degree and it will store distance
        self.scan = [None] * 180
        self.set_speed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()


    ########################
    ### CLASS METHODS - these are the actions that your object can run
    #### (they can take parameters can return stuff to you, too)
    #### (they all take self as a param because they're not static methods)
    ########################


    ##### DISPLAY THE MENU, CALL METHODS BASED ON RESPONSE
    def menu(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {"n": ("Navigate forward", self.nav),
                "d": ("Dance", self.dance),
                "c": ("Calibrate", self.calibrate),
                "t": ("Turn test", self.turn_test),
                "s": ("Check status", self.status),
                "o": ("Count Obstacles", self.count_obstacles),
                "q": ("Quit", quit)
                }

        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = raw_input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    def count_obstacles(self):
        # run a scan
        self.wide_scan()
        # count how many obstacles I've found
        counter = 0
        # starting state assumes no obstacle
        found_something = False
        # loop through all my scan data
        for x in self.scan:
            # if x is not None and really close
            if x and x < self.STOP_DIST:
                # If I've already found something
                if found_something:
                    print("obstacles continues")
                    # if this is a ne obstacle
                else:
                    # switch my tracker
                    found_something = True
                    print("start of new obstacle")
            # if my data show safe distances...
            if x and x > self.STOP_DIST:
                # if my tracker has been triggered...
                if found_something:
                    print("end of obstacle")
                    # reset tracker
                    found_something = False
                    # increase count of obstacles
                    counter += 1
        print('Total number of obstacles in this scan: ' + str(counter))
        return counter

    def turn_test(self):
        while True:
            ans = raw_input('Turn right, left or stop? (r/l/s): ')
            if ans == 'r':
                val = int(raw_input('/nBy how much?: '))
                self.encR(val)
            elif ans == 'l':
                val = int(raw_input('/nBy how much?: '))
                self.encL(val)
            else:
                break
        self.restore_heading()

    def restore_heading(self):
        print("Now I'll turn back to the starting position")
        # make self.turn_track go back to zero
        if self.turn_track > 0:
            print('I must have turned right a lot now I should turn left')

        elif self.turn_track < 0:
            print('I must have turned left a lot no I should turn tp self.encR(??)')
            abs(self.turn_track)
            self.encR(turn)





    #YOU DECIDE: How does your GoPiggy dance?
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        self.shimmy()
        self.wow()
        self.head_shake()
        # self.back_it_up()

    def shimmy(self):
        print("shimmy")
        for x in range(1):
            self.servo(50)
            self.encR(40)
            self.servo(140)
            self.encL(60)

    def wow(self):
        print("wow")
        for x in range(1):
            self.encR(90)
            self.servo(35)
            self.encL(95)
            self.encR(65)
            self.encF(18)
            self.servo(30)
            self.encL(60)
            self.encB(18)

    def head_shake(self):
        for x in range(6):
            self.servo(30)
            self.servo(150)
        self.servo(self.MIDPOINT)


    ########################
    ### MAIN LOGIC LOOP - the core algorithm of my navigation
    ### (kind of a big deal)
    ########################

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("[ Press CTRL + C to stop me, then run stop.py ]\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        # this is the loop part of the "main logic loop"
        while True:
            if self.quick_check():
                self.cruise()
            answer = self.choose_path()
            if answer == "left":
                self.encL(6)
            elif answer == "right":
                self.encR(6)
    def cruise(self):
        self.fwd()
        while self.is_clear():
            time.sleep(.1)
        self.stop()
        self.encB(3)

    def encR(self, enc):
        pigo.Pigo.encR(self, enc)
        self.turn_track += enc

    def encL(self, enc):
       pigo.Pigo.encL(self, enc)
       self.turn_track -= enc




####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit

##################################################################
######## The app starts right here when we instantiate our GoPiggy

g = GoPiggy()
