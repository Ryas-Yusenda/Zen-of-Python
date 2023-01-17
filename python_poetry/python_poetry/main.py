import pandas as pd

if __name__ == "__main__":
    # create a dictionary of our data:
    data = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    # load data into a DataFrame object:
    df = pd.DataFrame(data)

    # print dataframe
    print(df)
