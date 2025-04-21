from flask import Flask, render_template

app = Flask('_name_')


app_name = "My Application Name is: Agang and Friend"

@app.route("/")
def home():
    return "Hello, Flask!"


#route
@app.route('/step')
def about():
    return "Ini step"


@app.route("/demit")
def demit():
    return render_template('about.html')



#4 App Route dengan HTML with bostrapp
@app.route("/demit_bootstrap")
def demit_bootstrap():
    return render_template('aboutwith.html')

#5 App Route Dinamis
@app.route("/nama/<string:nama_mahasiswa>")
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)

#6 App Route ID
@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

#7 App Route Variabel Global
@app.route('/variabel-global')
def variabel_global():
    return f"Welcome {app_name}"

#8 App Route Dictionary Variabel
@app.route('/data')
def data():
    user = {"name": "Fazle", "age": 18, "city": "Makassar"}
    return render_template('data.html', user=user)




if '_name_' == "_main_":
    app.run(debug=True)