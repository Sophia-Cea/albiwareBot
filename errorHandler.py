class Errors:
    errors = []

    def __init__(self, category, errorMsg): #, testScreenObject) -> None:
        self.category = category
        self.errorMsg = errorMsg
        Errors.errors.append(self)
        # if testScreenObject.textPosition <= 70:
        #     testScreenObject.addError(errorMsg)

    def toString(self):
        return "Category: " + self.category + "  Error Msg: " + self.errorMsg

    def logErrors():
        with open("errorLog.txt", 'a') as f:
            for error in Errors.errors:
                f.write(error.toString() + "\n")
            f.write("\n")
