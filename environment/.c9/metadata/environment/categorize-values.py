{"filter":false,"title":"categorize-values.py","tooltip":"/categorize-values.py","undoManager":{"mark":30,"position":30,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["\"\"\"","Your module description","\"\"\"",""],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":73},"action":"insert","lines":["myMixedTypeList = [45, 290578, 1.02, True, \"My dog is on the bed.\", \"45\"]"],"id":2}],[{"start":{"row":0,"column":73},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":62},"action":"insert","lines":["for item in myMixedTypeList:","    print(\"{} is of the data type {}\".format(item,type(item)))"],"id":4}],[{"start":{"row":2,"column":62},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]},{"start":{"row":3,"column":4},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":1},"action":"insert","lines":["#"],"id":7}],[{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["s"],"id":8},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["a"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["d"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["a"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["s"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["d"]}],[{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["d"],"id":9},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["s"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":["a"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"remove","lines":["d"]},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"remove","lines":["a"]},{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"remove","lines":["s"]}],[{"start":{"row":4,"column":1},"end":{"row":4,"column":2},"action":"insert","lines":["C"],"id":10},{"start":{"row":4,"column":2},"end":{"row":4,"column":3},"action":"insert","lines":["o"]},{"start":{"row":4,"column":3},"end":{"row":4,"column":4},"action":"insert","lines":["m"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["p"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["o"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["s"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["i"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["e"],"id":11}],[{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":[" "],"id":12}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["d"],"id":13},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["a"]},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["t"]},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["a"]}],[{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":[" "],"id":14},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["t"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["y"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["p"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":20},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":11},"action":"insert","lines":["import csv","import copy"],"id":16}],[{"start":{"row":6,"column":11},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":17},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":17,"column":1},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}"],"id":18}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":19}],[{"start":{"row":19,"column":0},"end":{"row":20,"column":38},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))"],"id":20}],[{"start":{"row":20,"column":38},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":21},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":24},"action":"insert","lines":["myInventoryList = []"],"id":22}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":23},{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":21,"column":4},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":22,"column":20},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":26}],[{"start":{"row":23,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":24,"column":0},"end":{"row":44,"column":42},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')"],"id":28}],[{"start":{"row":44,"column":42},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":29},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":4},"end":{"row":46,"column":0},"action":"insert","lines":["",""]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":49,"column":22},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")"],"id":30}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":[" "],"id":31},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":[" "]}]]},"ace":{"folds":[],"scrolltop":360,"scrollleft":4,"selection":{"start":{"row":31,"column":8},"end":{"row":31,"column":8},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1674647477444,"hash":"f9e9fcb315dac5dd00f4c1f2b176ced94c4d9020"}