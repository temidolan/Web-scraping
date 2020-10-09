from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrapemarsDB"
mongo = PyMongo(app)



@app.route("/")
def home():
    usgs_dict = mongo.db.usgs_dict.find_one()
    return render_template("index.html", usgs_json=usgs_dict)


@app.route("/scrape")
def scraped():
    usgs_dict = mongo.db.usgs_dict
    usgs_dict_data = scrape_mars.scrape()
    usgs_dict.update({}, usgs_dict_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
