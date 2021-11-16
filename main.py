import tests
import coin_change
import file_reader


def main_pipeline():
    """
    The function asks you to enter a text file and prints converted amounts of money corresponding to the data in
    the file. The file is in the shape of:
    line 1: origin coin
    line 2: coin to convert to
    line 3-end: amount to convert. each amount in a separate line.
    :return: None
    """
    file_path = input("please enter a txt file path: ")
    data = file_reader.FileReader(file_path)
    data.read_file()
    data.extract_data()
    converter = coin_change.CoinChange(data)
    tester = tests.Tester(data, converter)
    tester.run_tests()
    converter.convert()
    converter.print_converted()


if __name__ == '__main__':
    main_pipeline()
