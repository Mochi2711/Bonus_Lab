# Save this as app.py

from flask import Flask, request, jsonify
import focus1  # Assuming your script is named focus1.py

app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return '''
        <form action="/run" method="post">
            <input type="submit" value="Run Script">
        </form>
    '''

# Define a route for the action of the form, for example '/run'
@app.route('/run', methods=['POST'])
def run_script():
    result = focus1.main()  # Call the main function from your script
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
