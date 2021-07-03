from flask import Flask, request, jsonify, render_template
import server.util as util

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")


@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")


@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify(
        {
            'locations': util.get_location_names()
        }
    )
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    # we will get the data from server/user using form request
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])
    Bedroom = int(request.form['Bedroom'])

    response = jsonify({
        'estimated_price': util.get_etimated_prices(location, total_sqft, bath, balcony, Bedroom)
    })
    return response


if __name__ == '__main__':
    print('Starting python flask server for Bangalore Home Price prediction..........')
    app.run()