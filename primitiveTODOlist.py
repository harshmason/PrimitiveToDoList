
import PySimpleGUI as sg

values = ('Enter a task','View your tasks','Remove a task',)
tasks = []

layout = [

    [sg.Button("Ok"), sg.Button("Cancel")],
    [sg.Text('Select from menu'), sg.InputOptionMenu(values, key='action')]
]



window = sg.Window("My Window", layout)


while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Cancel":
        break

    selected_action = values['action']

    if selected_action == 'Enter a task':
        newTask = sg.popup_get_text('Enter a new task:')
        if newTask:
            tasks.append(newTask)

    if event == "Enter a task":
        tasks.append(input('Enter a task'))

    elif selected_action == "View your tasks":
        sg.popup("Your Tasks:", "\n".join(tasks) if tasks else "No tasks added yet.")

    elif selected_action == "Remove a task":
        if tasks:
            task_to_remove = sg.popup_get_text("Enter the exact task to remove:")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                sg.popup("Task removed!")
            else:
                sg.popup("Task not found.")
        else:
            sg.popup("No tasks to remove.")

window.close()