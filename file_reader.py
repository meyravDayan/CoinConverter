class FileReader:
    """
    Read a .txt file and extract the relevant converting data
    """
    def __init__(self, file_path):
        """
        constructor of FileReader.
        :param file_path: a path to the text file containing all the conversion data.
        """
        self.file_path = file_path
        self.amount = []  #list of floats
        self.source_coin = None
        self.dest_coin = None
        self.lines = None

    def read_file(self):
        """
        Read the text file in self.file_path into the list: self.lines, where each index contain a different row
        in the file.
        :return: None
        """
        try:
            with open(self.file_path) as fp:
                self.lines = fp.readlines()
        except:
            print("Couldn't read file entered")
            exit()

    def extract_data(self):
        """
        This function iterate over self.lines and extract its data to the corresponding class attributes.
        :return: None
        """
        if not isinstance(self.lines, list):
            print("Couldn't read file entered")
            exit()
        if len(self.lines) < 3:
            print("Data is missing in the file")
            exit()
        self.source_coin = self.lines[0].strip().upper()
        self.dest_coin = self.lines[1].strip().upper()
        for ind in range(2, len(self.lines)):
            line = self.lines[ind].strip("\n\t ")
            line = line.replace(",", "")
            if line == '' or not line.isnumeric():
                continue
            self.amount.append(float(line))
