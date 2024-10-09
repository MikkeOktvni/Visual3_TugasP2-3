import PySimpleGUI as sg
sg.theme("DarkPink1")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                    layout=[[sg.Text("SELAMAT DATANG DI KELAS",
				                font=("Arial",25,"italic","bold","underline"))],
			               [sg.Text("NPM    : 2210010478")],
                           [sg.Text("Nama   : Mikke Oktaviani")],
                           [sg.Text("Kelas   : 5P Reguler Pagi Banjarmasin")],
                           ], 
                    size=(510,200),
		            font=("Times", 18))
window()
window.close()