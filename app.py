from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")


app = Flask(__name__)


@app.route("/")
def index():
    return "hello, world!"

if __name__ == '__main__':
    logger.debug("Starting Flask Server")
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)

