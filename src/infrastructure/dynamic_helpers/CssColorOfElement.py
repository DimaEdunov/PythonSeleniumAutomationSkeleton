import ast

class CssColorOfElement(object):
    colors_list = []

    def __init__(self, driver, element):
        self.driver = driver
        self.element = element

    def extract_color_of_element(self):
        rgba = self.element.value_of_css_property("color")

        r, g, b, a = ast.literal_eval(rgba.strip("rgba"))
        hex_value = '#%02x%02x%02x%02x' % (r, g, b, a)

        CssColorOfElement.colors_list.append(hex_value)

    def check_color_change(self):

        if CssColorOfElement.colors_list[0] == CssColorOfElement.colors_list[1]:
            print("Color of element has not changed between clicks")
            assert False

        else:
            print("Element color changed from '%s' to '%s' " %(CssColorOfElement.colors_list[0], CssColorOfElement.colors_list[1]))