# Guppy Ticket System

by GupDirt.

## What is the project for?

Mac needs a system to help fix his disorganization and help structure his workflow.  What better way to do this than to create a ticket system, allowing a quick look at all the tasks that are needed to be started, continued, reviewed, as well as a quick look at what is completed.

## System in Summary

The ticket system will feature a couple of dictionaries for each stage of progress a feature/system is in.  Currently, the idea is to feature 4 stages for entries:  Not started, In-progress, review, and complete.  Entries can be pushed around between entries, but will only ever proceed to the next step, with the exception being the review step, which will allow one to push the item back into In-Progress.


Each dictionary will carry a couple of values for each entry:  Project, Type, detail, and a time table (review this this seems like ass tbh).  The title will feature simply the project name with the type (Feature, Fix, etc.) in parenthesis.  The detail is a short sentence to describe the task (i.e. "program crashes on ___", "program needs x", "Project: initialize X project").  Finally, a time table (currently idea is a list that adds entries when a ticket is added, started, reviewed, and completed).  Each time an entry is moved forward, a time will be added, with the exception of the "reivew", as it might possibly go back to "In-progress" if the change fails review.


The project will work entirely in command line, and not a constant "while" loop with interaction.  commands will be with flags something like "python3 main.py -command --F".  for example, "python3 main.py -view --b" will allow the user to view(-view) the entire list of items within In-progress(--b).  "python3 main.py -Push --A --1 will push the 1st (--1) item in In-progress(--b) to the review step (--c).

## Milestones

1. Start date: October 3rd, try to have basic dictionaries open for entry.  Be able to make entries to the "not started" dictionary.
2. October 6th: Have entries be able to be shifted around different dictionaries with command.
3. October 24th: Have project up and running.  Begin using for personal organization.

