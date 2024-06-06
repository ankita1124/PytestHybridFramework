import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.loggen()



    def test_login_ddt(self, setup):
        self.logger.info("*************** Verifying Login test ******************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
                assert True
                self.driver.close()
                self.logger.info("***************  Login test is passed ******************")
        else:
                self.driver.save_screenshot("./Screenshots/"+"test_login.png")
                self.driver.close()
                self.logger.info("***************  Login test is failed ******************")
                assert False










