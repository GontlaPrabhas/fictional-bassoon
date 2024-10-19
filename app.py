import getpass
from flask import Flask
import os
import time
from subprocess import check_output

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system username
    username = "Prabhas"

    # Get server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5.5 * 3600))

    # Get 'top' command output
    top_output = check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> gontla prabhas</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
@app.route('/htop')
def htop():
    # Get system username
    username = getpass.getuser()

    # Get server time in IST
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 5.5 * 3600))

    # Get 'top' command output
    top_output = check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> Your Full Name</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

