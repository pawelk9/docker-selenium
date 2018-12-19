from framework.webapp import webapp


class DashboardPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = DashboardPage()
        return cls.instance

    def __init__(self):
        self.driver = webapp.get_driver()

        self.url = "tester-account/profile/dashboard"

    def verify_logged_in(self):
        webapp.wait_for_correct_current_url(self.url)


dashboardPage = DashboardPage.get_instance()
