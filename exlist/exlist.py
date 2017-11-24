class ExList(list):
    def __init__(self, *args):
        list.__init__(self, *args)

    def map(self, f):
        return ExList([f(x) for x in self])

    def filter(self, f):
        return ExList([x for x in self if f(x)])

    def fold(self, ini, f):
        if len(self) == 0:
            return ini
        else:
            return ExList(self[1:]).fold(f(ini,self[0]),f)
