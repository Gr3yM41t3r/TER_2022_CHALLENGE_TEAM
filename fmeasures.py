import csv


def precision(classe):
    with open("outputCSV/pretraiteCSV.csv") as input:
        reader = csv.reader(input)
        results = list(reader)
        right_answers = 0
        vraiposifit = 0;
        vraitotal = 0;

        for result in results:

            if result[9] == result[8] == classe:
                vraiposifit += 1
            if result[9] == classe:
                vraitotal += 1
        # print((vraiposifit / vraitotal) * 100)
        if vraitotal == 0:
            return 0
        return (vraiposifit / vraitotal) * 100


def recall(classe):
    with open("outputCSV/pretraiteCSV.csv") as input:
        reader = csv.reader(input)
        results = list(reader)
        right_answers = 0
        vraiposifit = 0
        vraitotal = 0
        for result in results:
            if result[9] == result[8] == classe:
                vraiposifit += 1
            if result[8] == classe:
                vraitotal += 1
        # print((vraiposifit / vraitotal) * 100)
        return (vraiposifit / vraitotal) * 100


def fMeasure(classe):
    prs = precision(classe)
    rcl = recall(classe)
    if (prs + rcl) == 0:
        return 0
    return 2 * ((prs * rcl) / (prs + rcl))
