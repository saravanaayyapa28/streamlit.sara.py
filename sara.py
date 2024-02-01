from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(10), unique=True, nullable=False)
    available = db.Column(db.Boolean, default=True)

@app.route('/')
def home():
    rooms = Room.query.all()
    return render_template('index.html', rooms=rooms)

@app.route('/reserve/<int:room_id>')
def reserve(room_id):
    room = Room.query.get(room_id)
    if room and room.available:
        room.available = False
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/cancel/<int:room_id>')
def cancel(room_id):
    room = Room.query.get(room_id)
    if room and not room.available:
        room.available = True
        db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Reservation System</title>
</head>
<body>
    <h1>Hotel Reservation System</h1>

    <table border="1">
        <tr>
            <th>Room Number</th>
            <th>Status</th>
            <th>Action</th>
        </tr>
        {% for room in rooms %}
        <tr>
            <td>{{ room.room_number }}</td>
            <td>{% if room.available %}Available{% else %}Reserved{% endif %}</td>
            <td>
                {% if room.available %}
                    <a href="{{ url_for('reserve', room_id=room.id) }}">Reserve</a>
                {% else %}
                    <a href="{{ url_for('cancel', room_id=room.id) }}">Cancel</a>
                {% endif %}
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
