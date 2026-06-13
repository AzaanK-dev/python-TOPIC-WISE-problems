# Create a function that returns a command executor.
# Every time the executor is called:
# Execute the command.
# Store it in history.
# History must remain available between calls without using global variables.


def history_track():
    history=[]
    def executer(cmd):
        nonlocal history
        history.append(cmd)
        print(cmd)
        return history
    return executer

h = history_track()
print(h("ls"))
print(h("cd"))
print(h("cls"))