from flask import Flask,request,json,jsonify
import function

app = Flask(__name__)

def hasil(msg):
    return jsonify({"reply":msg})

@app.route('/',methods=['POST'])
def wa():
    message = request.form['message']
    ArrMsg = message.split()
    print(ArrMsg)

    if (ArrMsg[0] == "/p"):
        return jsonify({"reply":"apa"})
    elif (ArrMsg[0] == "/help"):
        return function.help()
    elif (ArrMsg[0] == "/tugas"):
        return function.tugas()
    elif (ArrMsg[0] == "/ubahtugas"):
        ArrMsg.pop(0)
        ArrMsg = " ".join(ArrMsg)
        try:
            return function.ubahtugas(ArrMsg)
        except :
            return hasil("blok mau ubah ap")
    elif (ArrMsg[0] == "/ngomong"):
        ArrMsg.pop(0)
        ArrMsg = "".join(ArrMsg)
        return hasil(ArrMsg)
    else:
        return "blok"


app.run(
    host="192.168.1.7",
    port=6900
)