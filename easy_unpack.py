def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return elements[0], elements[2], elements[-2]


el = easy_unpack((range(10)))
print(type(el), el)
