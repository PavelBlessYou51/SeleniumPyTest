from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and len(first_content) > 0, 'Incorrect title'
            assert second_title == 'Where does it come from?' and len(second_content) > 0, 'Incorrect title'
            assert third_title == 'Why do we use it?' and len(third_content) > 0, 'Incorrect title'

    class TestAutoCompletePage:

        def test_fill_multi_autocoplite(self, driver):
            autocomplite_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplite_page.open()
            colors = autocomplite_page.fill_input_multi()
            colors_result = autocomplite_page.check_color_in_multi()
            assert colors == colors_result, "Added colors are missing in the input"

        def test_remove_value_from_multi(self, driver):
            autocomplite_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplite_page.open()
            autocomplite_page.fill_input_multi()
            count_value_before, count_value_after = autocomplite_page.remove_value_from_multi()
            assert count_value_before != count_value_after, "Value was not deleted"

        def test_fill_single_autocomplite(self, driver):
            autocomplite_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplite_page.open()
            color = autocomplite_page.fill_input_single()
            color_result = autocomplite_page.check_color_in_single()
            assert color == color_result, "Added colors are missing in the input"

    class TestDatePickerPage:

        def test_date_picket_page(self, driver):
            date_picket_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picket_page.open()
            value_date_before, value_date_after = date_picket_page.select_date()
            assert value_date_before != value_date_after, "The date wasn't changed"

        def test_change_date_and_time(self, driver):
            date_picket_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picket_page.open()
            value_date_before, value_date_after = date_picket_page.select_date_and_time()
            assert value_date_before != value_date_after, "The date and time weren't changed"

    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            before, after = slider.change_slider_value()
            assert before != after, "The slider didn't move"

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            before, after = progress_bar.change_progress_bar_value()
            assert before != after, 'The progress bar has been changed'

    class TestTabsPage:

        def test_page(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open()
            what_button, what_content = tabs.check_tabs('what')
            origin_button, origin_content = tabs.check_tabs('origin')
            use_button, use_content = tabs.check_tabs('use')
            assert what_button == 'What' and what_content != 0, 'the tab "what" was not pressed or the text is missing'
            assert origin_button == 'Origin' and origin_content != 0, 'the tab "origin" was not pressed or the text is missing'
            assert use_button == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'

    class TestToolTips:
        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()
            button_text, field_text, contrary_text, section_text = tool_tips_page.check_tool_tips()
            assert button_text == 'You hovered over the Button', "Hover missing"
            assert field_text == 'You hovered over the Button', "Hover missing"
            assert contrary_text == 'You hovered over the text field', "Hover missing"
            assert section_text == 'You hovered over the text field', "Hover missing"
