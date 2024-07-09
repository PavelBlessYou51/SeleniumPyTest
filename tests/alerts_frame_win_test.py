from pages.alerts_frame_windows_page import BrowserWindowPage


class TestAlertsFrameWindow:
    class TestBrowserWindow:
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "The new tab has not opened"

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_window()
            assert text_result == 'This is a sample page', "The new window has not opened"
