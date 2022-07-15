
import pandas as pd

def main():
    ## open the file
    ## test change here
    print("tes")

    file_errors_location = './data/input/testfile.xlsx'
    df = pd.read_excel(file_errors_location)
    print(df)


if __name__ == '__main__':
    main()

