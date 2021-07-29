from flask import jsonify,json


def help():
    string = """helep 
    /help 
        untuk nge bantu

    /tugas
        untuk nge liatin tugas
    
    /ubahtugas
        untuk mengganti tugas

    """

    return jsonify({"reply":string})

def tugas():
    jsonFile = open("data.json")
    data = json.load(jsonFile)

    print(data)

    return jsonify({"reply":"tugas\n\n"+data["tugas"]})

def ubahtugas(ubahan):
    jsonFile = open("data.json")
    data = json.load(jsonFile)
    print(ubahan)
    data["tugas"] = ubahan

    UbahJson = open("data.json","w")
    json.dump(data,UbahJson)
    UbahJson.close()

    return jsonify({"reply":f"tugas :\n{data['tugas']}"})



