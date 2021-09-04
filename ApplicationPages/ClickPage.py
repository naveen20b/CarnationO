from ApplicationUtils.ApplicationUtilities import ApplicationUtilities


class ClickPage(ApplicationUtilities):
    def __init__(self, driver):
        super().__init__(driver)

    def clickform(self):
        print("In Click Form --------------------------------------------------")

        self.click("clickButton_XPATH")

