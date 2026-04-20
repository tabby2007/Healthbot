import pandas as pd

# Load your data into a dataframe
df = pd.read_csv("health_data.csv")
# print(df)

print("Healthbot: Hello there, I am your Health assistance bot. Ask me about your symptoms.")

while True:
    # 1. Get the user input ans store the same into a variable
    user_text = input("\n You:").lower()

    # 2. Check if the user wants to exit
    if user_text == "quit":
        print("Healthbot: Goodbye! It was nice being of service to you. Stay healthy")
        break

    # Create a variable that will store the details structured in the csv file
    found_answer = False

    # Come up with a loop that loops through the entire dataframe created before
    for index, row in df.iterrows():
        # Clean up the keywords from the csv row
        keywords_list = str(row["Keywords"]).split(",")

        # Below we check every keyword in that given row(keywords)
        
        for word in keywords_list:
            clean_word = word.strip().lower()

            # if the keyword is inside the user's sentence
            if clean_word in user_text:
                print("Healthbot:", row["Response"])
                found_answer = True
                break # stop looking at other keywords

        if found_answer:
            break # Stop looking at other answers since we already found a match

     # 4. If we went through the entire/whole CSV file and never found any match of the keywords,
    #  We need to display a message to the user

    if not found_answer:
        print("Healthbot: Sorry, I don't know that one. Try asking for something else")