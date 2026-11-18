import pandas as pd
game_data = pd.read_csv("video_games_raw.csv")

while True:
    entry = input("What row would you like to inspect? (or x to quit): ").strip()

    if entry.lower() == "x":
        break

    try:
        inspect_row = int(entry)
    except ValueError:
        print("Please enter an integer or x to quit.")
        continue

    if not 1 <= inspect_row <= len(game_data):
        print("Please enter an integer between 1 and " + str(len(game_data)))
        continue

    print(game_data.iloc[inspect_row - 1])

    comp = False
    while comp == False:

        new_status = input("Please enter the new status for this game: ")
    
        if new_status == "Backlog":
            game_data.at[inspect_row-1, 'Status'] = new_status 
            comp = True
        elif new_status == "Playing":
            game_data.at[inspect_row-1, 'Status'] = new_status
            comp = True
        elif new_status == "Completed":
            game_data.at[inspect_row-1, 'Status'] = new_status
            comp = True
        elif new_status == "Dropped":
            game_data.at[inspect_row-1, 'Status'] = new_status
            comp = True
        else:
            print("Please enter either Backlog, Playing, Completed, or Dropped.")

game_data["Recommended"] = "No"

game_data.loc[
    (game_data["Rating"] >= 8) & (game_data["Price"] <= 40.00),
    "Recommended"
] = "Yes"

recommended_games = game_data.query("Recommended == 'Yes'")
print(recommended_games[["Title", "Platform", "Price", "Rating"]])

game_data.to_csv("video_games_cleaned.csv", index=False)
     
    

