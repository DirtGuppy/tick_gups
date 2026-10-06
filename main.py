import json
import argparse

def main():
    parser = argparse.ArgumentParser(
        description = ""
    )
    #first few will navigate to different 
    parser.add_argument("")
    parser.add_argument("-v", "--view", help = "views contents of dict")
    parser.add_argument("-a", "--add", action = "", help = "Add new dictionary entry to dictionary")
    args = parser.parse_args()

    #if I pass main.py -v "location", args.view will be equivalkent to "location"
    #if args.view:
        #target_key = args.view.lower()
        #if target_key in dictionary:
        #contents = dictionary[target_key]
            #for tick_id, (tick_type, details) in contents.items():
                #print(f"{tick_id} |  | {tick_type}:  \n{details}  \n_____________________________________________________________________________")