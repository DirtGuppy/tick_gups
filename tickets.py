class Status(Enum):
    BUG = 0
    TASK = 1


class tickets
    def __init__(self, tick_id, tick_title, tag, detail)
    #tick_id is crc32 hexadecimal giving to a ticket upon creation
    #tick_title is user created title to ticket
    #tag is the type of ticket it is (ex: Feature, Bug, etc.) as an enum
    #detail is the ticket description of the issue or need of user.
    #add two more values: Tick_made and tick_modified.  These track when a tick was
    #created and modified so you can display new stuff at the top, old stuff tucked 
    #away
    self.tick_title = tick_title
    self.tick_id = tick_id
    self.tag = tag
    self.detail = detail
    self.tick_made = tick_made
    self.tick_edit = tick_edit

    def tick_create(self):
        #open ticket here
        tick_id =  id_make()
        tick_title = #retrieve user input for title
        #retrieve user input for descript descript = input()
        #submit ticket into dictionary:
        tickets["backlog"][tick_id] = {"title": tick_title, "type": context_value, 
        "detail" : descript    #add two more values, a created with the current time
        #translated to now, and a "modified last", which will be the same for creation
        #purposes
        }
        #save here: save_contents(tickets)
        return

    def id_make()