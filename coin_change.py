import requests
url = 'https://api.exchangerate-api.com/v4/latest/USD'  # The coin rates API url.


class CoinChange:
    """
    This class uses a coin rates api and the data in the FileReader object and converts the amounts.
    """
    def __init__(self, file_data):
        """
        constructor of the CoinChange object.
        :param file_data: a FileReader object.
        """
        try:
            self.data = requests.get(url).json()
        except:
            print("Converter URL does not exist on Internet, please fix the api before trying again")
            exit()

        if 'rates' not in self.data:
            print("Something went wrong with the converter url, please fix the api before trying again")
            exit()
        self.currencies = self.data['rates']
        self.converted_list = []
        self.file_data = file_data  # FileReader object

    def convert(self):
        """
        This function performs the conversion of the amounts listed in the input file into a list of
        converted amount: self.converted_list. the amount are rounded to show up to 2 digits after the '.'.
        The rates given (from the api) corresponds to USD, therefore it changes the rates accordingly.
        :return: None
        """
        for amount in self.file_data.amount:
            if self.file_data.source_coin != 'USD':
                amount = amount / self.currencies[self.file_data.source_coin]
            amount = amount * self.currencies[self.file_data.dest_coin]
            self.converted_list.append(round(amount, 2))

    def print_converted(self):
        """
        This function prints all the converted amounts from self.converted_list.
        in the format of:
        X origin_coin = Y target_coin
        :return: None
        """
        for ind, converted_sum in enumerate(self.converted_list):
            print(f"{self.file_data.amount[ind]} {self.file_data.source_coin} = {self.converted_list[ind]} "
                  f"{self.file_data.dest_coin}")
