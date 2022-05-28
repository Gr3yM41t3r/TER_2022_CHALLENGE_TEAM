import csv


header =['Annotations','Score','CR Author A','CR Author B','Review URL A','Review URL B','Text Fragments A','Text Fragments B','Entities A','Entities B','Keywords A','Keywords B','Citations A','Citations B','URI A','URI B']
data =[]
def final_cleaning1():

    with open('inputCSV/allClaims.csv') as inputData:
        counter = 0
        reader = csv.reader(inputData)
        claims = list(reader)
        with open('inputCSV/claims_prof.csv') as inputData2:
            reader2 = csv.reader(inputData2)
            calimsprof = list(reader2)
            with open("outputCSV/claims_benc.csv", "w") as outputData:
                writer = csv.writer(outputData)
                writer.writerow(header)
                for prof in calimsprof:
                    for row2 in claims:
                        if prof[5] == row2[12]:
                            counter += 1
                            data.clear()
                            data.append(prof[0])
                            data.append(prof[1])
                            data.append(prof[2])
                            data.append(prof[3])
                            data.append(prof[4])
                            data.append(prof[5])
                            data.append(prof[6])
                            data.append(prof[7])
                            data.append(prof[8])
                            data.append(row2[7])
                            data.append(prof[10])
                            data.append(row2[9])
                            data.append(prof[12])
                            data.append(prof[13])
                            data.append(prof[14])
                            data.append(prof[15])
                            writer.writerow(data)


def final_cleaning():
    with open('inputCSV/allClaims.csv') as inputData:
        counter = 0
        reader = csv.reader(inputData)
        claims = list(reader)
        print(len(claims))
        with open('inputCSV/claims_benc.csv') as inputData2:
            reader2 = csv.reader(inputData2)
            calimsprof = list(reader2)
            print(len(calimsprof))
            with open("outputCSV/claims_benc.csv", "w") as outputData:
                writer = csv.writer(outputData)
                writer.writerow(header)
                for prof in calimsprof:
                    print(counter)
                    for row2 in claims:
                        if prof[4] == row2[12]:
                            counter += 1
                            data.clear()
                            data.append(prof[0])
                            data.append(prof[1])
                            data.append(prof[2])
                            data.append(prof[3])
                            data.append(prof[4])
                            data.append(prof[5])
                            data.append(prof[6])
                            data.append(prof[7])
                            data.append(row2[7])
                            data.append(prof[9])
                            data.append(row2[9])
                            data.append(prof[11])
                            data.append(prof[12])
                            data.append(prof[13])
                            data.append(prof[14])
                            data.append(prof[15])
                            writer.writerow(data)

def wa3():
    header2 =['text','keywords']
    data =[]
    with open('inputCSV/mixture.csv') as inputData:
        counter = 0
        reader = csv.reader(inputData)
        claims = list(reader)
        with open("outputCSV/mixture.csv", "w") as outputData:
                writer = csv.writer(outputData)
                writer.writerow(header2)
                for prof in claims:
                    if prof[9] :
                        data.clear()
                        print(counter)
                        data.append(prof[1])
                        data.append(prof[9])
                        counter += 1
                        writer.writerow(data)
                       
            


