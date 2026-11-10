from pathlib import Path
import os
import json
import argparse
import zlib
import random
from datetime import datetime
import time
from enum import Enum

document_path = "documents"
file_name = "tickets.json"
tickets_path = os.path.join(document_path, file_name)
initial = {"backlog": {},
        "in-progress": {},
        "review": {},
        "closed": {}}

class Status(Enum):
    BUG = 0
    TASK = 1


class tickets:

    def __init__(self, ticket_name = None, ticket_id = None, 
    step = None, ticket_type = None, detail = None, big_dict = None, 
    timestamp_created = None, timestamp_edited = None):
        self.ticket_name = ticket_name
        self.ticket_id = ticket_id
        self.step = step
        self.type = ticket_type
        self.detail = detail
        self.big_dict = big_dict
        self.timestamp_created = timestamp_created
        self.timestamp_edited = timestamp_edited

    def ticket_create(self, ticket_name, ticket_context):
        big_dict = tickets.contents_load()
        self.ticket_name = ticket_name
        self.ticket_type = ticket_context.strip().lower()
        self.ticket_id, self.timestamp_created = self.id_make()
        print(f"{self.ticket_id} {self.timestamp_created}")
        self.timestamp_edited = self.timestamp_created
        #assign context value AKA type of ticket
        descript = input("explain details of ticket below:")
        big_dict["backlog"][self.ticket_name] = {"id": self.ticket_id, 
        "type": self.ticket_type, "detail" : descript,
        "time_created" : self.timestamp_created, "Last_modified" : self.timestamp_edited
        }
        tickets.contents_save(big_dict)
        return


    def contents_load():
        try:
            with open("documents/tickets.json", "r") as f:
                big_dict = json.load(f)
        #revist except block, tried except NoFile found error, but code
        #does not work with that, fix this issue, current except block is not explicit
        #enough
        except FileNotFoundError:
            print("File could not be found.  Discovering why.")
            if not os.path.exists(document_path):
                print(f"Error: The directory {document_path} does not exist.  Make directory")
                os.mkdir("documents")
                with open(tickets_path, "w") as f:
                    json.dump(initial, f ,indent = 4)
                big_dict = initial
            else:
                print(f"Error: {file_name} does not exist, creating file")
                with open(tickets_path, "w")as f:
                    json.dump(initial, f, indent = 4)
                big_dict = initial
        return big_dict





    def contents_save(big_dict):
        try:   
            with open("documents/tickets.json", "w")as f:
                json.dump(big_dict, f, indent=4)
        except FileNotFoundError:
            print("no file found.  You should not be able to save without loading.  No change has been made.")
        return


    def id_make(self):
        try:
            now = datetime.now()
            timestamp_made = now.strftime("%Y-%m-%d %H:%m")
            random.seed(datetime.now().timestamp())
            c_seed =bytes(random.randint(0,0xFFFFFF))[2:]
            ticket_name = f"{zlib.crc32(c_seed):08x}"
        except ValueError as e:
            print(f"could not read the time found: {e}")
        return ticket_name, timestamp_made

    def ticket_finder(self, target_ticket):
        big_dict = tickets.contents_load()
        target_ticket = target_ticket
        try:
            for step, ticket_data in big_dict.items():
                for ticket_name in ticket_data:
                    if ticket_name == target_ticket:
                        self.ticket_name = target_ticket
                        return big_dict, step
        except KeyError:
            print(f"Error made, {target_ticket} is not a ticket within database.  perhaps a typo was made.")

    def ticket_remove(self, target_tick, big_dict, step):
        try:
            big_dict[step].pop(target_tick)
            tickets.contents_save(big_dict)
            print(f"removed {target_tick},  Try viewing changes with the -v command!")
            return
        except KeyError:
            print(f"Error finding correct ticket.  perhaps {target_ticket} is not a real ticket.")

    def ticket_move(self, target_ticket, big_dict, step, destination):
        try:
            moving_entry = big_dict[step].pop(self.ticket_name)
            now = datetime.now()
            moving_entry["last_modified"] = now.strftime("%Y-%m-%d %H:%M")
            print(moving_entry["last_modified"])
            big_dict[destination][self.ticket_name] = moving_entry
            print(f"Moving {self.ticket_name} to {destination}.  Try '-v {destination}' to view it now!")
            tickets.contents_save(big_dict)
            return
        except KeyError:
            print(f"Error finding target location: {destination} is not a valid place within dictionary.")