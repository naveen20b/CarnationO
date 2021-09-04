#from TestCases.BaseTest import BaseTest
import pytest
from ApplicationPages.ClickPage import ClickPage

@pytest.mark.usefixtures("get_browser")
class Test_Click:
    # Simple Constant Value based Test Case

    def test_clickButton(self):
        print("Test -------------------------------------------------------------------------------")

        rPage = ClickPage(self.driver)
        rPage.clickform()