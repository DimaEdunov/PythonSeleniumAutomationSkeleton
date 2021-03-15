from datetime import time


class ScrollActions(object):

    @staticmethod
    def scroll_to(element):
        element.location_once_scrolled_into_view
