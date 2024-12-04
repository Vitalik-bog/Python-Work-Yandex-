arr = []
def shuffle_array(arr):
    even = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd = [arr[i] for i in range(len(arr)) if i % 2 != 0]; odd.reverse()
    out = []
    for i in arr:
        if i in even:
            out += [str(i)]
        else:
            out += [str(odd[0])]
            del odd[0]
    arr.clear()
    arr += out
