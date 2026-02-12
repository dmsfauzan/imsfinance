from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        otr = float(request.form["otr"])
        dp_persen = float(request.form["dp"])
        tenor = int(request.form["tenor"])

        # DP & pokok
        dp = otr * dp_persen / 100
        pokok = otr - dp

        # menentukan bunga sesuai flowchart
        if tenor <= 12:
            bunga_persen = 12
        elif tenor <= 24:
            bunga_persen = 14
        else:
            bunga_persen = 16.5

        # hitung bunga
        bunga = pokok * bunga_persen / 100

        # total hutang
        total = pokok + bunga

        # angsuran per bulan
        angsuran = total / tenor

        result = {
            "dp": dp,
            "pokok": pokok,
            "bunga_persen": bunga_persen,
            "bunga": bunga,
            "angsuran": angsuran
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
