import tickethelper
from tickethelper import tickets
import json
import argparse
import zlib
import random
from datetime import datetime
import time


ticket_manager = tickets()

def main():
    dictionary = tickethelper.tickets.contents_load()

    parser = argparse.ArgumentParser(
        description = ""
    )

    parser.add_argument("-l", "--list", action = "store", help = "views a column of the tickets file")
    parser.add_argument("-a", "--add",  action = "store", help = "Add new ticket to backlog")
    parser.add_argument("-m", "--move",  action = "store", help = "Moves the ticket to specified stage")
    parser.add_argument("-rm", "--remove", action = "store", help = "removes the ticket specified from system after finding it.")
    args = parser.parse_args()


    if args.list:
        target_key = args.list.lower()
        dictionary = tickets.contents_load()
        if target_key in dictionary:
            contents = dictionary[target_key]
            for ticket_name, data in contents.items():
                try:
                    print(f"{ticket_name} |  | type: {data["type"]}")
                    print(f"{data["detail"]}")
                    print(f"Created date: {data["time_created"]} |  Last modified: {data["last_modified"]}")
                    print("_" * 90)
                except KeyError as e:
                    print(f"this ticket is missing a value in ticket : {e}")
                    #currently this KeyError is NOT verbose enough when multiple values 
                    #are missing, make keyError class or something to hold and print a
                    #list of items
        else:
            print("what has been typed is not a stage of the ticket system.\n-v will only return contents of backlog, in-progress, review, or closed steps.\nreturning user to console.")

    
    if args.add:
        ticket_name = args.add.lower()
        ticket_context = input("what type of ticket is this: 0). Bug or 1). Task ")
        ticket_manager.ticket_create(ticket_name, ticket_context)
        print(f"added {ticket_name} to the backlog!")
    
    if args.move:
        target_ticket = args.move
        destination = input("move ticket to what step(backlog, in-progress, review, or closed):")
        big_dict, step = ticket_manager.ticket_finder(target_ticket)
        ticket_manager.ticket_move(target_ticket, big_dict, step, destination)
        print(f"Successfully moved {target_ticket} to {step}")

    if args.remove:
        target_ticket = args.remove.lower()
        big_dict, step = ticket_manager.ticket_finder(target_ticket)
        ticket_manager.ticket_remove(target_ticket, big_dict, step)






if __name__ == "__main__":
    main()