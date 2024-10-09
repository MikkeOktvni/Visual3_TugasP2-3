import PySimpleGUI as sg
sg.theme("DarkPink1")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010478")],
                           [sg.Text("Nama   : Mikke Oktaviani")],
                           [sg.Text("Kelas   : 5P Reguler Pagi Banjarmasin")],
                           [sg.Text("Matkul  :  Pemrograman Visual 3")]
                           ], 
                   size=(400,200))
window()
window.close()