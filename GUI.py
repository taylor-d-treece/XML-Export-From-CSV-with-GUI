import PySimpleGUI as sg


def xml_file_select():

    sg.theme("DarkTeal2")
    layout = [[sg.T("Choose Source File and Destination for exports below!")],
              [sg.Text("Source File: "), sg.Input(key="-IN2-", change_submits=True), sg.FileBrowse(key="-IN-")],
              [sg.Text("Destination: "), sg.Input(key="-IN3-", change_submits=True), sg.FolderBrowse(key="-IN4-")],
              [sg.Button("Submit")], [sg.Button("Exit")]]

    # Building Window
    window = sg.Window('XML Export', layout, size=(600, 160))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Submit":
            file_selected = (values["-IN-"])
            dest_selected = (values["-IN4-"])
            if file_selected != "":
                print('Source File: ' + file_selected)
                print('Destination: ' + dest_selected)
                break
            else:
                err_layout = [[sg.T("")], [sg.Text("User has not selected a file!")], [sg.Button("OK")]]
                err_window = sg.Window('No File Selected!', err_layout, size=(300, 140))
                event = err_window.read()
                print("User has not selected a file!")
                if event == "OK" or event == sg.WIN_CLOSED:
                    break
                err_window.close()
    window.close()
    return file_selected, dest_selected
