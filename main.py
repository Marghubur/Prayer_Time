from flask import Flask, request, jsonify
import aladhan

app = Flask(__name__)

# Define the custom class
class Adhan:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def to_dict(self):
        return {"name": self.name, "time": self.time}

@app.route("/")
def home():
    location = aladhan.City("Asansol", "IND")
    client = aladhan.Client(location)

    adhans = client.get_today_times()

    adhan_list = []
    for adhan in adhans:
        adhan_list.append(Adhan(adhan.get_en_name(), adhan.readable_timing(show_date=False)))

    result = [adhan.to_dict() for adhan in adhan_list]

    # Return the JSON response
    return jsonify(result)

    # for adhan in adhans:
    #     return("{: <15} | {: <15}".format(adhan.get_en_name(), adhan.readable_timing(show_date=False)))
    # return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)


