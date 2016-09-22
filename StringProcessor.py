class StringProcessor:
    def avg(self, numbers):
        return sum(numbers) / len(numbers)

    def process(self, string):
        if string == "":
            return [0, 0, 0, 0]
        else:
            array = string.split(",")
            return [len(array), int(min(array)), int(max(array)), self.avg(map(float, array))]