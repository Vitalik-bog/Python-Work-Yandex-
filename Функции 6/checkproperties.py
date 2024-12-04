def same_by(characteristic, objects):
    even = [characteristic(i) for i in objects]
    if not(bool(even)) or even.count(even[0]) == len(even): return True
    return False
