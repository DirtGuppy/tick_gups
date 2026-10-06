import json
import argparse
import json


def tick_create(new_entry):
    title = new_entry[0]
    context_value = new_entry[1]
    descript = new_entry[2]
    new_data = {
        "title":{"type": context_value, "detail" : descript}}
    with open("tickets.json","w") as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)
    return


def ticket_move():
    #move a ticket up the chain to the next step

    #if ticket is moving from review to complete, add a comfirmation line.  if y, push to complete.  if n, push to in-progress
    return

def main():
    parser = argparse.ArgumentParser(
        description = ""
    )
    #first few will navigate to different 
    parser.add_argument("-v", "--view", action = "store", help = "views contents of dict")
    parser.add_argument("-a", "--add", nargs = 3, action = "store", help = "Add new dictionary entry to dictionary")
    parser.add_argument("-m", "--move", action = "store", help = "Moves the ticket to the next stage, moves entry with matching name")
    args = parser.parse_args()

    with open("tickets.json", "r")as f:
        dictionary = json.load(f)

    #if I pass main.py -v "location", args.view will be equivalent to "location"
    if args.view:
        target_key = args.view.lower()
        if target_key in dictionary:
            contents = dictionary[target_key]
            #print(contents)
            for tick_id, data in contents.items():
                tick_type = contents[tick_id]
                #details = contents[data]
                print(f"{tick_id} |  | type: {data["type"]} \n{data["detail"]}  \n_____________________________________________________________________________")
    
    if args.add:
        list_val = args.add
        clean_list = []
        for word in list_val:
            clean_list.append(word.lower())
        ticket_name = list_val[0]
        print(clean_list)
        tick_create(clean_list)
        print(f"added ticket!")
    
    #if args.move:
        #target_key = args.move()
        #if target_key in dictionary:











if __name__ == "__main__":
    main()