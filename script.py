import regex as re

# load countries list into array from text file
c = open("countries.txt", "r")
countries = c.read().split("\n")

# load covid bill text
path = "./bills-116hr133sa-rcp-116-68.txt"
f = open(path, "r")
text=f.read()

# regex nastiness to try to clean the document up
text = text.encode("ascii", "ignore")
text = text.decode()
text = text.replace("U:\\2021OMNI\\Final\\DivA-M2.xml SEN. APPRO.", "")
text = text.replace("U:\\2021OMNI\\14OMNI\\DivO-FF.xml SEN.", "")
text = text.replace("U:\\2021OMNI\\Final\\H133JLHS68.xml", "")
text = text.replace("December 21, 2020 (12:59 p.m.)\x00", "")
text = text.replace("December 21, 2020 (10:27 a.m.)\x00", "")
text = text.replace("  ", " ")
text = re.sub('[a-z][0-9] [a-z]', '', text)
text = re.sub('[a-z][0-9][0-9] [a-z]', '', text)

cleaner_text = ""
regex = "(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"


for row in text.split("\n"):
    if row != "":
        if re.search("[0-9]", row[:1]):
            row = row.replace(row.split(" ")[0], "")
        cleaner_text += row.strip() + "\n"

splitted = re.split(regex, cleaner_text)

def write_countries_to_file():
	file_text = "<h1>References to dollar amounts given to outside-countries in COVID relief bill</h1>"
	for t in splitted:
		for c in countries:
			if (c + " ") in t and '$' in t:
				file_text += "<h4> " + c + "</h4>"
				file_text += t.replace("<br /><br />", "")
				file_text += "<br /><br />"
	f = open("./referenced-countries.html", "w")
	f.write(file_text)
	f.close()

def write_money_references_to_file():
	file_text = "<h1>References to dollar amounts in COVID relief bill</h1>"
	for t in splitted:
		if '$' in t:
			file_text += "<li>" + t + "</li>"
			file_text += t.replace("<br /><br />", "")
			file_text += "<br /><br />"
	f = open("./referenced-dollars.html", "w")
	f.write(file_text)
	f.close()

write_countries_to_file()
write_money_references_to_file()
print("Finished running parse and extraction")