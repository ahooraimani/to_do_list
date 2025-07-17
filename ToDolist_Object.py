import csv

class Task():
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    def __str__(self):
        return (f"{self.name}, {self.priority}")

class TodoList():
    def __init__(self):
        self.tasks = []
    def addList(self, task):
        self.tasks.append(task)
    def removeList(self, taskName):
        for task in self.tasks:
            if task.name == taskName:
                self.tasks.remove(task)
                break
    def showList(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for task in self.tasks:
                print("-", task)
    def load_from_csv(self, filename):
        self.tasks.clear()
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task = Task(row['task name'], row['priority'])
                self.tasks.append(task)

todo = TodoList()
while True:
    print("1- Add task")
    print("2- Remove task")
    print("3- Show tasks")
    print("4- Save to CSV")
    print("5- Load from CSV")
    print("6- Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter task name: ")
        priority = input("Enter priority (high, medium, low): ")
        task = Task(name, priority)
        todo.addList(task)

    elif choice == '2':
        name = input("Enter task name to remove: ")
        todo.removeList(name)

    elif choice == '3':
        todo.showList()

    elif choice == '4':
        outfileAddress = input("Please enter your address to save on your system (e.g. C:\\Users\\ahoora\\Desktop): ")
        filename = input("Add your file name (without .csv): ")

        try:
            full_path = outfileAddress + "\\" + filename + ".csv"
            with open(full_path, mode='w', newline='', encoding="utf-8") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(['task name', 'priority'])
                for task in todo.tasks:
                    writer.writerow([task.name, task.priority])
            print("✅ File saved successfully at:", full_path)
        except FileNotFoundError:
            print("❌ The address wasn't found on your system.")

    elif choice == '5':
        filename = input("Enter file_address with filename to load (e.g. C:\\Users\\ahoora\\Desktop\\yourfile.csv): ")
        todo.load_from_csv(filename)

    elif choice == '6':
        print("bye bye buddy!")
        break

    else:
        print("Invalid option, try again.")