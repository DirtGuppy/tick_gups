import json
import argparse



def tick_create(new_entry):
    with open("tickets.json", "r") as f:
        tickets = json.load(f)
    title = new_entry[0]
    context_value = new_entry[1]
    descript = new_entry[2]
    tickets["backlog"][title] = {"type": context_value, "detail" : descript}
    save_contents(tickets)
    return

def save_contents(tickets):
    with open("tickets.json", "w")as f:
        json.dump(tickets, f, indent=4)


def ticket_move(target_tick):
    with open("tickets.json", "r") as f:
        big_dict = json.load(f)
    for step, tick_data in big_dict.items():
        for tick_id in tick_data:
            print(tick_id)
            if tick_id == target_tick:
                print("attempting movement please hold")
                if step == "backlog":
                    moving_entry = big_dict["backlog"].pop(tick_id)
                    big_dict["in-progress"][target_tick] = moving_entry
                    save_contents(big_dict)
                    return
                if step == "in-progress":
                    moving_entry = big_dict["in-progress"].pop(tick_id)
                    big_dict["review"][target_tick] = moving_entry
                    save_contents(big_dict)
                    return
                if step == "review":
                    moving_entry = big_dict["review"].pop(tick_id)
                    big_dict["closed"][target_tick] = moving_entry
                    save_contents(big_dict)
                    return

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
        print(f"added ticket!")
    
    if args.move:
        target_key = args.move.lower()
        ticket_move(target_key)











if __name__ == "__main__":
    main()