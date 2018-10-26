from appJar import gui
import locale
import gettext

# leave it for now
_ = gettext.gettext
gettext.install('myapplication', './')

app = gui()

new_data = _("New Data")
edit_data = _("Edit Data")

#the title of the button will be received as a parameter
def press(btn):
	print(btn)
	print("Hello! added",btn)
	title = btn
	message = btn
	app.infoBox(title, message, parent=None)
	
def dealdata(btn):
#close data
    if btn == "Close":
       app.stop()
    elif btn == "Submit":
       main()
	
def pressone(btn):
	print(btn)
	print("Hello! added",btn)
	app.startLabelFrame("Login Details")
	# these only affect the labelFrame

	app.removeButton(new_data)
	app.removeButton(edit_data)
	app.removeButton("Three")

	app.setSticky("ew")
	app.setFont(20)

	app.addLabel("l1", "Name", 0, 0)
	app.addEntry("NA", 0, 1)
	app.addLabel("l2", "ID", 1, 0)
	app.addEntry("ID", 1, 1)
	app.addLabel("l3", "PW", 2, 0)
	app.addEntry("PW", 2, 1)
	# No Good for window text alignment, 2018.10.24
	#app.addLabelEntry("Us")
	#app.addLabelEntry("Id")
	#app.addLabelEntry("Pw")
	app.addButtons(["Submit", "Close"], dealdata, 3, 0, 3)
	app.stopLabelFrame()

def main():
	app.removeAllWidgets()
	# 3 buttons, each calling the same function
	app.addButton(new_data, pressone)
	app.addButton(edit_data, press)
	app.addButton("Three", press)
	app.go()

main()
