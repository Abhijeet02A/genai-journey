def add_task(fileName, task):
    with open(fileName, 'a') as file:
        file.write(task + '\n')
        print(f"Task '{task}' added to {fileName}.")

def view_tasks(fileName):
    try:
        with open(fileName, "r") as fileReader:
            # for line in fileReader:
            #     if not line:
            #         print("Nothing To Do!!!")
            #         return
            #     print(f"Task  `{line.strip()}`")
            lines = fileReader.readlines()
            if not lines:
                print(f"Empty File, Enjoy your day!")
                return
            for lineNum, line in lines.index, lines:
                print(f"`{lineNum}` Task is `{line}`")
    except FileNotFoundError:
        print(f"No tasks found. The to-do list is empty or does not exist yet.`{fileName}`")
    except Exception as e:
        print(f"Exception raised `{e}`")

def clear_tasks(fileName):
    with open(fileName, "w") as fileWriter:
        print("cleared successfully.")

add_task("welcome.txt", "Wakeup")
add_task("welcome.txt", "read")
add_task("welcome.txt", "sleep")
add_task("welcome.txt", "thats fine")

view_tasks("welcome.txt")

clear_tasks("welcome.txt")

view_tasks("welcome.txt")
view_tasks("skdf.txt")
