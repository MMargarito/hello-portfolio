import json
import datetime as dt
from pathlib import Path

file_path = f"{Path(__file__).resolve().parent}/plan.json"

#Getting todays date with datetime.
today = dt.date.today().strftime("%A")



def main():
    with open(file_path, newline='') as plan:
        plan_dict = json.load(plan)

        try:
            today == plan_dict[today]
        except KeyError:
            print("There is no planned study session today.")

        else:
            print(f"Today is {today} The topic will be {plan_dict[today]['Topic']}. You are expected to spend {plan_dict[today]['Hours']} hours on this topic.")



if __name__ == "__main__":
    main()
