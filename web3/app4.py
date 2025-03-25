#usage python app4.py

from flask import Flask, request, jsonify, render_template, redirect

import sqlite3

app = Flask(__name__)
DATABASE = 'contacts.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        conn.commit()

# index route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', 
                           (name, email, phone))
            conn.commit()
        
        return redirect('/')
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()
    
    return render_template('index.html', contacts=contacts)

# RESTful API start #
@app.route('/contacts', methods=['GET'])
def get_contacts():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts')
        contacts = cursor.fetchall()
    return jsonify([{ "id": c[0], "name": c[1], "email": c[2], "phone": c[3] } for c in contacts])

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        conn.commit()
        contact_id = cursor.lastrowid
    
    return jsonify({"id": contact_id, "name": name, "email": email, "phone": phone}), 201

@app.route('/contacts/<int:contact_id>', methods=['GET'])
def get_contact(contact_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        contact = cursor.fetchone()
    
    if contact:
        return jsonify({"id": contact[0], "name": contact[1], "email": contact[2], "phone": contact[3]})
    return jsonify({"message": "Contact not found"}), 404

@app.route('/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        conn.commit()
    return jsonify({"message": "Contact deleted"})

# RESTful API end #


if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0", port=8002, debug=True)

