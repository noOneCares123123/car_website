from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "cars.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    conn = get_db()
    cars = conn.execute("SELECT * FROM cars").fetchall()
    conn.close()
    return render_template("index.html", cars=cars)


@app.route("/car/<int:id>")
def car(id):
    conn = get_db()
    car = conn.execute(
        "SELECT * FROM cars WHERE id=?",
        (id,)
    ).fetchone()
    conn.close()
    return render_template("car.html", car=car)


@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":

        conn = get_db()

        conn.execute("""
        INSERT INTO cars
        (name,brand,year,horsepower,engine,topspeed,image,description)

        VALUES (?,?,?,?,?,?,?,?)
        """,(

        request.form["name"],
        request.form["brand"],
        request.form["year"],
        request.form["horsepower"],
        request.form["engine"],
        request.form["topspeed"],
        request.form["image"],
        request.form["description"]

        ))

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_car.html")


if __name__ == "__main__":
    app.run(debug=True)