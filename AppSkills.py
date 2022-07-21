
import sqlite3 
db= sqlite3.connect("app.db")
cr=db.cursor()
cr.execute("create table if not exists skills (name text, progress integer, user_id integer)")
user_id=1

def commit_close():
 
    db.commit()
    db.close()
print("Connection To Database Is Closed")
input_message ="""
"s"=> Show All Skills 
"a"=> Add New Skills 
"d"=> Delete A Skill 
"u"=> Update Skill progress
"q"=> Quit The App 
Choose Option : 
"""

def commit_and_close():

    # Save (Commit) Changes
    db.commit()

    # Close Database
    db.close()
    print("Connection To Database Is Closed")


user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():

   cr.execute("select * from skills ")
   res = cr.fetchall()
   print(res)

   commit_and_close()

def add_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write Skill Progress ").strip()

    cr.execute(f"insert into skills(name, progress, user_id) values('{sk}', '{prog}', '{user_id}')")

    commit_and_close()

def delete_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{user_id}'")

    commit_and_close()

def update_skill():

    cr.execute(f" update skills set name ='java' where user_id=1" )

    commit_and_close()

# Check If Command Is Exists
if user_input in commands_list:

    # print(f"Command Found {user_input}")

    if user_input == "s":

        show_skills()

    elif user_input == "a":

        add_skill()

    elif user_input == "d":

        delete_skill()

    elif user_input == "u":

        update_skill()

    else:

      print("App Is Closed.")

else:

    print(f"Sorry This Command \"{user_input}\" Is Not Found")