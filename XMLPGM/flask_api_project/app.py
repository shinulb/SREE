from flask import Flask, jsonify

app = Flask(__name__)

students_data = {
    "students": [
        {"name": "John Doe", "age": 20, "course": "Computer Science"},
        {"name": "Jane Smith", "age": 22, "course": "Mathematics"}
    ]
}

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students_data)

if __name__ == '__main__':
    app.run(debug=True)
