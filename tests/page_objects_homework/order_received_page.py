from tests.helpers.support_functions import *

order_received_header = '//*[@id="post-8"]/header/h1'

def order_received_header_visible(driver_instance):
    elem = wait_for_visibility_of_element_by_xpath(driver_instance, order_received_header, time_to_wait=1)
    return elem.is_displayed()
