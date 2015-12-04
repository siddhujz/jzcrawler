import json
from pprint import pprint

file_list = []
file_list.append("./Output/CarverCollegeofMedicine.json")
file_list.append("./Output/CollegeofDentistry.json")
file_list.append("./Output/CollegeofEducation.json")
file_list.append("./Output/CollegeofEngineering.json")
file_list.append("./Output/CollegeofLaw.json")
file_list.append("./Output/CollegeofLiberalArtsandSciences.json")
file_list.append("./Output/CollegeofNursing.json")
file_list.append("./Output/CollegeofPharmacy.json")
file_list.append("./Output/CollegeofPublicHealth.json")
file_list.append("./Output/ContinuingEducation.json")
file_list.append("./Output/GraduateCollege.json")
file_list.append("./Output/TheUniversityofIowa.json")
file_list.append("./Output/TippieCollegeofBusiness.json")
file_list.append("./Output/UniversityCollege.json")

length_data = {}
for file in file_list:
    with open(file, 'r+') as json_data:
        data = json.load(json_data)
        length = (len(data)) 
        print (length)
        #length_data.update({file, length})
        length_data[file] = length

print ("length_data = ", length_data)
pprint(length_data)
