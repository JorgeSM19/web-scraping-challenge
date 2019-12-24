from flask import Flask, render_template
import pymongo

#Crear conexión con mongo
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

#Nos conectamos con nuestra Base de Datos
db = client.mars_DB

app = Flask (__name__)

@app.route("/")
def home():
        #print(db.list_database_names_())
        mars = list(db.mars.find())
        print(mars)
        return render_template("index.html", mars = mars)

if __name__ == "__main__":
        app.run(debug = True)