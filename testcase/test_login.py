from page.main_page import MainPage


class TestLogin:
    def test_phone(self):
        profile=MainPage().goto_profile()
        login=profile.goto_login()
        login.login_phone_fail("15600534760",'1234')
        assert "验证码已过期" in login.get_msg()


    def test_password(self):
        profile = MainPage().goto_profile()
        login = profile.goto_login_by_password()
        login.login_by_password_fail("15600534760", '123456')
        assert "用户名或密码错误" in login.get_msg()


    def test_weibo(self):
        pass

    def test_wechat(self):
        pass

    def test_qq(self):
        pass
