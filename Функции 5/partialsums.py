def partialSums(*args):
    return [0] + [sum(args[:args.index(arg)+1]) for arg in args]