"""
This class can check if the ppl living in the house is at home,
or there is pple not living in this house, it will save the face of the guests
and record the detail about the person, like face information, height and weight(roughly)
The information stored will be removed the day after the guest left.

Left time and back Time recording the time when ppl coming in and leave the house


"""
import pandas as pd


class PeopleAtHome():
    def __init__(self):
        self.pplList = None
        self.atHome = []
        self.guest = []
        self.numPpl = 0
        self.leftTime = {}
        self.backTime = {}
        self.path = "./peopleInTheHouse"
        self.read_ppl()

    def read_ppl(self):
        try:
            df = pd.read_csv(self.path, header=0)
            self.pplList = df
            self.numPpl = len(df)
            print(df.head(10))
        except(FileExistsError):
            print("No Such File")


