from flask import Flask, render_template, request
import recommender

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        result = request.form
        requirement = {"REQUIREMENT": {
            "DSA": int(result['DSA']),
            "OOPs": int(result['OOPs']),
            "Databases": int(result['Databases']),
            "Web_Development": int(result['Web_Development']),
            "CGPA": int(result['CGPA']),
            "Work_Experience": int(result['Work_Experience']),
            "Backlog": int(result['Backlog'])}}
        num_of_candidate = int(result['candidate'])
        result = recommender.topMatches(requirement, recommender.dataFrame, "REQUIREMENT", num_of_candidate)
        print(result)
        return render_template("index.html", result=result)

    return render_template("index.html", result=[("name","Score")])


if __name__ == '__main__':
    app.run(debug=True)
