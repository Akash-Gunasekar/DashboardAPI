from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",  
        user="root",      
        password="root",   
        database="test_db"
    )

@app.route('/')
def display_techniques():
    return render_template('index.html')

@app.route('/display_steps')
def display_steps():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT steps FROM search WHERE techniques = 'regression'")
    steps = [step[0] for step in cursor.fetchall()]  
    cursor.close()
    conn.close()
    return render_template('steps.html', steps=steps)


@app.route('/display_source')
def display_source():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT source FROM search WHERE techniques = 'regression'")
    sources = [source[0] for source in cursor.fetchall()]  
    cursor.close()
    conn.close()
    return render_template('steps.html', sources=sources)

@app.route('/display_input')
def display_input():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Input FROM search")
    inputs = [input[0] for input in cursor.fetchall()] 
    cursor.close()
    conn.close()
    return render_template('steps.html', inputs=inputs)

if __name__ == '__main__':
    app.run(debug=True)
