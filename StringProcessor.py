class StringProcessor:
    def avg(self, numbers):
        return sum(numbers) / len(numbers)

    def process(self, string):
        if string == "":
            return [0, 0, 0, 0]
        elif "," in string:
            array = string.split(",")
            return [len(array), int(min(array)), int(max(array)), self.avg(map(float, array))]
        else:
            return [1, int(string), int(string), int(string)]