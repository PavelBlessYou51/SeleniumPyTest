from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


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

