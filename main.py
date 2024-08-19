from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Kumar@2002'
app.config['MYSQL_DB'] = 'entertainment_db'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM bookings''')
    results = cur.fetchall()
    cur.close()
    return render_template('events.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
