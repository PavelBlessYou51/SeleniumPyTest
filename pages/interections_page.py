import random

from selenium.webdriver import ActionChains

from locators.interactions_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list(self):
        ActionChains(self.driver).scroll_by_amount(delta_x=0, delta_y=300).perform()
        elem = self.element_is_visible(self.locators.TAB_LIST)
        elem.click()
        order_defore = self.get_sortable_items(self.locators.LIST_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEM)
        return order_defore, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_defore = self.get_sortable_items(self.locators.GRID_ITEM)
        item_list = random.sample(self.elements_are_visible(self.locators.GRID_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEM)
        return order_defore, order_after
