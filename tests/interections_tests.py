from pages.interections_page import SortablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'The order didn"t chenge'
            assert grid_before != grid_after, 'The order didn"t chenge'
