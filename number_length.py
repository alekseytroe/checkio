def number_length(a: int) -> int:
    """ You have a positive integer. Try to find out how many digits it has?
    Input: A positive Int
    Output: An Int. """

    return len(str(a))


print(number_length(10),
      number_length(0),
      number_length(4),
      number_length(44))
