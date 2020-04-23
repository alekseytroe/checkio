def best_stock(data):
    return sorted(data, key=data.__getitem__, reverse=True)[0]


print(best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 100.2}))
