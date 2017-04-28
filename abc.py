from flask import request
from flask import Flask
from flask import make_response
import json
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return make_response(json.dumps(request.data,indent=4))
    else:
        show_the_login_form()
if __name__ == '__main__':
    # port = int(os.getenv('PORT', 5000))
    # print("Starting app on port %d" % port)
    app.run()