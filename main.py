from everything import *

def main():
    data = read_file('BTCPrice.csv')
    data_clean = cleaning(data)
    data_analysis = analysis(data_clean)
    #data_api = api(data_analysis)


if __name__ == "__main__":
    main()
