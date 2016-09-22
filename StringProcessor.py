class StringProcessor:
    def process(self, string):
        if string == "":
            return [0, 0]
        else:
            array = string.split(",")
            return [len(array)]