import getopt
import sys


def main(argv):
    keywordthreshold = ''
    numberofclaims = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "k:n:o:")
    except getopt.GetoptError:
        print('test.py -i <inputfile>a -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-k":
            keywordthreshold = arg
        elif opt == "-n":
            numberofclaims = arg
        elif opt == "-o":
            outputfile = arg
        else:
            print('test.py -i <inputfile>b -o <outputfile>')
            sys.exit()

    print("generating a file with these settings :\n keyword similarity threshold :{}\n" +
          " total number of claims : {}\n" +
          " to file : {}".format(keywordthreshold, numberofclaims, outputfile))


if __name__ == "__main__":
    main(sys.argv[1:])
