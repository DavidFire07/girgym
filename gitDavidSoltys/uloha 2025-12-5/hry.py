import numpy as np
import pandas as pd

def error_log(row, message):
    with open("error_log.txt", "w") as f:
        f.write(f"Row {row}: {message}\n")

data_frame = pd.read_csv("hry.csv")

data_frame["hours_played"] = pd.to_numeric(data_frame["hours_played"], errors="coerce")
data_frame["price"] = pd.to_numeric(data_frame["price"], errors="coerce")
data_frame["rating"] = pd.to_numeric(data_frame["rating"], errors="coerce")

rows_to_remove = set()

for index, row in data_frame.iterrows():

    row_number = index + 2

    nazov = row["nazov"]
    zaner = row["zaner"]
    hours_played = row["hours_played"]
    price = row["price"]
    rating = row["rating"]

    if pd.isna(nazov) or pd.isna(zaner):
        error_log(row_number, "Error: nazov/zaner")
        rows_to_remove.add(index)

    if (pd.isna(hours_played) or hours_played < 0):
        error_log(row_number, "Error: hours_played")
        rows_to_remove.add(index)

    if (pd.isna(price) or price < 0):
        error_log(row_number, "Error: price")
        rows_to_remove.add(index)

    if (pd.isna(rating) or not (0 <= rating <= 100)):
        error_log(row_number, "Error: rating")
        rows_to_remove.add(index)

data_frame.drop(rows_to_remove, inplace=True)

avg_rating = data_frame["rating"].sum() / data_frame.shape[0]
top3_hours = data_frame.nlargest(3, "hours_played")
top3_rating = data_frame.nlargest(3, "rating")
top3_ratio_hours_price = data_frame.assign(ratio=data_frame["hours_played"] / data_frame["price"]).nlargest(3, "ratio")

total_hours = data_frame["hours_played"].to_numpy().sum()
data_frame["value_score"] = (data_frame["hours_played"] / (data_frame["price"] + 1)).round(2)

best_genres = data_frame["zaner"].mode()

conditions = [
    data_frame["price"] < 10,
    (10 <= data_frame["price"]) & (data_frame["price"] < 40),
    40 <= data_frame["price"]
]

choices = ["low", "medium", "high"]

data_frame["price_category"] = np.select(conditions, choices, default="unknown")

data_frame.to_csv("report.csv", index=False)

with open("vysledky.txt", "w", encoding="utf-8") as file:
    file.write(f"Average rating of all games is:\n{avg_rating}\n\n")

    file.write("Top 3 games based on played hours, rating, ration (played hours / price):\n\n")
    file.write(
        f"{top3_hours[["nazov", "hours_played"]]}\n\n" 
        f"{top3_rating[["nazov", "rating"]]}\n\n"
        f"{top3_ratio_hours_price[["nazov", "ratio"]]}\n\n")

    file.write(f"Total playing type:\n{total_hours}\n\n")

    file.write(f"Data frame with new column (value_score):\n\n{data_frame[["nazov", "value_score"]]}\n\n")

    file.write(f"The most popular genre/s:\n")
    for genre in best_genres:
        file.write(f"{genre}\n")
    file.write("\n")

    low_price = data_frame[data_frame["price_category"] == "low"]
    medium_price = data_frame[data_frame["price_category"] == "medium"]
    high_price = data_frame[data_frame["price_category"] == "high"]

    file.write(f"Games grouped by price:\n\n"
               f"{low_price[["nazov", "price_category"]]}\n\n"
               f"{medium_price[["nazov", "price_category"]]}\n\n"
               f"{high_price[["nazov", "price_category"]]}\n\n")