import json
import datetime as dt
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir.parent/"hello-portfolio/plan.json"

# today = "Wednesday"
today = dt.date.today().strftime("%A")



def main():
    with open(file_path, newline='') as plan:
        plan_dict = json.load(plan)

        try:
            if plan_dict[today]:
                print(f"Today is {today} The topic will be {plan_dict[today]['Topic']}. You are expected to spend {plan_dict[today]['Hours']} on this topic.")
        except KeyError:
            print("There is no planned study session today.")

                
    


if __name__ == "__main__":
    main()
