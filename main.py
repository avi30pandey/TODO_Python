import sys


# '''print(sys.argv)
# print("Name of the file: ",sys.argv[0])'''

todo = []        #? data structure for storing tasks as a list of dictionary

# todo = [{
#     id, taskname, marks,
# }, {
#     id, taskname, marks,
# }, {
#     id, taskname, marks,
# }, ...]

#? For each Particular Task
# {
    # id: 1
#     task_name: taskName,
#     task_start_time:,
#     task_end_time:,
#     mark_as_done:,
# }

# python main.py <option> <value>
# python main.py add/remove/update/delete "Take Tea at night"
#? To add particular task in a list of dictionary
def addTask(id):
    taskName=input("Enter your specific task:-")
    Task=dict() #?creating a dictionary for storing task in the structure/list
    Task["id"]=id 
    Task["name"]=taskName
    Task["mark_as_done"]=False
    #print(Task)
    todo.append(Task)


def removeTask():    #? 
    if not len(todo):    #?  case where user chooses to remove task before entering the task
        print("No Tasks to display!")
        return

    printTask()
    removableId=int(input("Press task number which you want to remove :- "))

    
    # ids = [task['id'] for task in todo]
    ids = []                    #?to store all the id of tasks
    for task in todo:
        ids.append(task['id'])

    # ids = [1, 3]
    print('ids :- ', ids)    
    print(removableId)
    if removableId not in ids: #?to check whether the user supplied id's is valid or not(damage control)
        print("No tasks to remove!")
        return
    
    for task in todo:
        print(task['id'])
        if task["id"] == removableId:
            todo.remove(task)
    
    print("Deleted Successfully")


def printTask():
    #? Below Condition ran when there is no tasks to display currently
    if not len(todo): 
        print("No Tasks to display!")
        return

    print("\nTasks :-")
    for task in todo:
        # if task["mark_as_done"] == True:
        #     status = "Completed"
        # else:
        #     status = 'Not Completed'
        status = "Completed" if task["mark_as_done"] else "Not Completed"
        printable = f'{task["id"]}: {task["name"]}, status = {status}.'
        print(printable)

    print()



# print(chosen_option)

id = 1
while True:
    chosen_option = int(input("Enter the below options to perform: \n Press 1 to add task \n Press 2 to remove task \n Press 3 to update task \n Press 4 to clear all task  \n Press 5 to view task \n Press 0 to add quit \n"))
    if chosen_option==1:
        print("Adding...")
        addTask(id)
        id += 1
    elif chosen_option==2:
        removeTask()
    elif chosen_option==3:
        print("update...")
    elif chosen_option==4:
        print("delete...")
    elif chosen_option==5:
        printTask()
    elif chosen_option==0:
        print("Exiting...")
        quit()
    else:
        print("Invalid choice")










