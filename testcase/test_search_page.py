from driver.app import App
from page.main_page import MainPage


class TestSearchPage:
    main_page=None

    @classmethod
    def setup_class(cls):
        App.start()
        TestSearchPage.main_page=MainPage()

    def setup(self):
        self.search_page=self.main_page.goto_search()

    def test_get_price(self):
        assert self.search_page.search("alibaba").get_price() > 160

    def test_pdd(self):

        assert self.search_page.search("pdd").get_price() > 10

    def teardown(self):
        self.search_page.cancel()



