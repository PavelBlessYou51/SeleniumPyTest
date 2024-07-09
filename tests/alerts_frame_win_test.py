from pages.alerts_frame_windows_page import BrowserWindowPage, AlertsPage, FramesPage, NestedFramesPage


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

    class TestAlertsPage:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert didn't appear"

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", "Alert didn't appear after 5 seconds"

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_comfirm_alert()
            assert alert_text == "You selected Ok", "Alert didn't appear"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_prompt_alert()
            assert alert_text == "You entered AUTOtest", "Prompt didn't work right"

    class TestFramesPage:
        def test_frame(self, driver):
            frame_page = FramesPage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ('This is a sample page', '500px', '350px'), "Frame doesn't exist"
            assert result_frame2 == ('This is a sample page', '100px', '100px'), "Frame doesn't exist"

    class TestNestedFrames:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent iframe', 'Nested frame does not exist'
            assert child_text == 'Child iframe', 'Nested frame does not exist'
