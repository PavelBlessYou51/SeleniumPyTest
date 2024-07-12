from pages.interections_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, 'The order didn"t chenge'
            assert grid_before != grid_after, 'The order didn"t chenge'

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0, "No elements were selected"
            assert len(item_grid) > 0, "No elements were selected"

    class TestResizablePage:
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            assert max_box == ('500px', '300px'), "Problem with max size"
            assert min_box == ('150px', '150px'), "Problem with min size"

    class TestDropablePage:
        def test_simple_dropable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == 'Dropped!', "Simple element has not been dropped"

        def test_accert_dropable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept != accept, 'The element one not has been dropped'

        def test_prevent_propogation_dropable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            not_greedy, not_greedy_inner, greedy, greedy_inner = droppable_page.drop_prevent_propogation()
            assert not_greedy == 'Dropped!', "The element text has not been changed"
            assert not_greedy_inner == 'Dropped!', "The element text has not been changed"
            assert greedy == 'Outer droppable', "The element text has been changed"
            assert greedy_inner == 'Dropped!', "The element text has not been changed"

        def test_revert_draggable_dropable(self, driver):
            droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable('will')
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable('not_will')
            assert will_after_move != will_after_revert, "Didn't revert"
            assert not_will_after_move == not_will_after_revert, "Revert"