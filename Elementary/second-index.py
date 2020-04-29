def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    symbol_index = text.find(symbol, text.find(symbol)+1)
    return symbol_index if symbol_index != -1 else None


print( second_index("sims", "s")) # 3, "First"
print( second_index("find the river", "e"))  # 12, "Second"
print( second_index("hi", " ")) # is None, "Third"
print( second_index("hi mayor", " ")) # None, "Fourth"
print( second_index("hi mr Mayor", " ")) # 5, "Fifth"