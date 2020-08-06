import webbrowser
from flask import Flask
import os
import cb as cb1

app = Flask(__name__)

@app.route('/')
def new():
    cb1.on_start()
    


if(__name__ == '__main__'):
    port = int(os.environ.get('PORT', 5000))
    app.jinja_env.cache = {}
    h="http://localhost:"+str(port)
    webbrowser.open_new(h)
    app.run(debug=True, host='0.0.0.0', port=port)

