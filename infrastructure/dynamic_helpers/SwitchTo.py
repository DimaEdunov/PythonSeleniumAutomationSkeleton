class SwitchTo(object):

    # Is set by 'setter_switch_to' setter method
    def __init__(self, switch_to_first_screen, switch_to_second_screen, driver):
        print("Inside 'SwitchTo' constructor")
        self.switch_to_first_screen = switch_to_first_screen
        self.switch_to_second_screen = switch_to_second_screen
        self.driver = driver

    def switch_to(self, screen_number):
        print("Log : Switching to screen number")

        if screen_number == "0":
            self.driver.switch_to.window(self.switch_to_first_screen)
        elif screen_number == "1":
            self.driver.switch_to.window(self.switch_to_second_screen)
        else:
            print("Error : Please insert '0' or '1' into 'switch_to' method")



