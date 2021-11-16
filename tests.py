
class Tester:
    """
    Receive a FileReader object and a CoinChange objects and perform some tests to evaluate the input data, using
    'run_tests' function.
    """
    def __init__(self, data, converter):
        """
        constructor of Tester object.
        :param data: FileReader object.
        :param converter: CoinChange object.
        """
        self.data = data  # FileReader object
        self.converter = converter  # CoinChange object

    def test_origin(self):
        """
        validates the origin coin existence.
        :return: if invalid coin, prints an error message and exits the program.
        """
        if self.data.source_coin not in self.converter.currencies:
            print("Source coin doesn't exist")
            exit()

    def test_target(self):
        """
        validates the target coin existence.
        :return: if invalid coin, prints an error message and exits the program.
        """
        if self.data.dest_coin not in self.converter.currencies:
            print("Target coin doesn't exist")
            exit()

    def test_amounts(self):
        """
        Test whether any valid amount to convert were given.
        :return: if no valid amount were given, prints an error message and exits the program.
        """
        if not self.data.amount:
            print("No amount was given to convert")
            exit()

    def run_tests(self):
        """
        Run all tests in Tester.
        :return: None
        """
        self.test_origin()
        self.test_target()
        self.test_amounts()
