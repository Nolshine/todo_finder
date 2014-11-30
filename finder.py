import os

"""
This is a program that will find and list todos in a bunch of python files,
and tell me where each todo is.
Hopefully this is actually a useful tool huehue.
-Solshine
"""

# this code will eventually generate a list of files/locations to look for todos in.

def searchFolder(location):
		locations = []
		for root, dirs, files in os.walk(location):
			for file in files:
				if file.endswith(".py"):
						locations.append(os.path.join(root, file))
		return locations

# this code is what handles the one file and returns a list of todos it finds

def getTodoFromFile(input): #this one works
	with open(input, 'r') as f:
		todos = []
		newlinetodo = False
		for line in f.readlines():
			if newlinetodo:
				newlinetodo = False
				todos.append("#TODO:" + line)
				continue
			dat = line.lower()
			if ("#todo" in dat) or ("# todo" in dat) or ("todo:" in dat):
				if "todo\n" in dat:
					newlinetodo = True
					continue
				else:
					todos.append(line)
		if todos != []:
			return todos
		else:
			return None


# this code takes a list of file locations and runs getTodoFromFile on them

def generateDictFromFiles(locations):
	arranged_todos = {}
	for f in locations:
		dat = getTodoFromFile(f)
		if dat != None:
			arranged_todos[f] =  dat	# put the list of todos with the filename for a key..
										# might be better to use the filename as a key.
	return arranged_todos

if __name__ == "__main__": #TODO: test on this folder to see if it can get both files.
	for item in getTodoFromFile('C:\\Users\\USER\\Desktop\\pyjects\\todo_finder\\testfile.py'):
		print item
	raw_input()
	for location in searchFolder("C:\\Users\\USER\\Desktop\\pyjects\\todo_finder"):
		print location
	raw_input()
	#now for the real test
	todos = generateDictFromFiles(searchFolder("C:\\Users\\USER\\Desktop\\pyjects\\3dpe\\battle prototype"))
	for key in todos:
		print key + " :"
		for item in todos[key]:
			print "    " + item.split("#")[1]
		raw_input("press return to continue...\n")
	raw_input("DONE. press return to exit.")