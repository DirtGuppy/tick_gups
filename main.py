import json
import argparse
import zlib
import random
from datetime import datetime
import time



#take arguments from new_entry, should be 2 now, and assign it a name with crc32
#/zib
def tick_create(new_entry):
    #random ticket names to add
    with open("tickets.json", "r") as f:
        tickets = json.load(f)
    name =  name_make()
    context_value = new_entry[0]
    descript = input()
    tickets["backlog"][name] = {"type": context_value, "detail" : descript}
    save_contents(tickets)
    return

def name_make():
    random.seed(datetime.now().timestamp())
    c_seed =bytes(random.randint(0,0xFFFFFF))[2:]
    name = f"{zlib.crc32(c_seed):08x}"
    return name

def save_contents(tickets):
    with open("tickets.json", "w")as f:
        json.dump(tickets, f, indent=4)



def ticket_move(target_tick, big_dict, step, destination):
    moving_entry = big_dict[step].pop(target_tick)
    big_dict[destination][target_tick] = moving_entry
    save_contents(big_dict)
    return

    #if ticket is moving from review to complete, add a comfirmation line.  if y, push to complete.  if n, push to in-progress

def ticket_remove(target_tick, big_dict, step):
    big_dict[step].pop(target_tick)
    with open("tickets.json", "w") as f:
        json.dump(big_dict, f, indent =4)
    print("removed!  Try -v command!")
    return



def ticket_finder(target_tick):
    try:
        with open("tickets.json", "r") as f:
            big_dict = json.load(f)
        for step, tick_data in big_dict.items():
            for tick_id in tick_data:
                if tick_id == target_tick:
                    return tick_id, big_dict, step
    except:
        Exception("Could not find your ticket.  No action has been made")

def main():
    parser = argparse.ArgumentParser(
        description = ""
    )
    #first few will navigate to different 
    #repurpose -a --add not store a initial "name" argument.
    #repurpose -m --move to take two arguments, the "name" of the ticket, and the "detination"

    parser.add_argument("-v", "--view", action = "store", help = "views contents of dict")
    #old -a line parser.add_argument("-a", "--add", nargs = 3, action = "store", help = "Add new dictionary entry to dictionary")
    #parser.add_argument("-m", "--move", action = "store", help = "Moves the ticket to the next stage, moves entry with matching name")
    parser.add_argument("-a", "--add",  action = "store", help = "Add new dictionary entry to dictionary")
    parser.add_argument("-m", "--move", nargs = 2, action = "store", help = "Moves the ticket to the next stage, moves entry with matching name")
    parser.add_argument("-rm", "--remove", action = "store", help = "takes a ticket by name and removes it after confirming with user.")
    parser.add_argument("-t", "--testfind", action = "store", help = "debugging find method to see if it functions with other methods")
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
        tick_create(clean_list)
        print(f"added ticket!")
    
    if args.move:
        list_tar = args.move
        move_list=[]
        for word in list_tar:
            move_list.append(word.lower())
        target_tick = move_list[0]
        destination = move_list[1]
        target_tick, big_dict, step = ticket_finder(target_tick)
        ticket_move(target_tick, big_dict, step, destination)

    if args.remove:
        target_key = args.remove.lower()
        target_tick, big_dict, step = ticket_finder(target_key)
        ticket_remove(target_tick, big_dict, step)






if __name__ == "__main__":
    main()