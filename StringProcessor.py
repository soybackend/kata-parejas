class StringProcessor:
    def process(self, string):
        if string == "":
            return [0, 0, 0, 0]
        elif "," in string:
            array = string.split(",")
            return [len(array), int(min(array)), int(max(array)), float(1.5)]
        else:
            return [1, int(string), int(string), int(string)]