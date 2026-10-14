import json
import datetime as dt
from pathlib import Path

script_dir = Path(__file__).resolve().parent
file_path = script_dir.parent/"hello-portfolio/plan.json"




def main():
    with open(file_path, newline='') as plan:
        json_reader = json.load(plan)
        print(json_reader)
    


if __name__ == "__main__":
    main()
