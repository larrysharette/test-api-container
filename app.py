from flask import Flask
# from docker import 
from flask import jsonify
from flask import request

import subprocess
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
  print('starting request')
  file = open("code_runner/main.js","w")

  file.write("""console.log('Hello from javascript!')""")

  file.close()

  print('wrote to file')

  response = None

  try:
    print('start run command')
    response = subprocess.run(["node","code_runner/main.js"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    response = {'returncode': str(response.returncode), 'stdout': str(response.stdout), 'stderr': str(response.stderr)}

    print('updating response')

    return jsonify(response)
  except Exception as err:
    response = err
    return jsonify(str(response))

  # os.remove("code_runner/main.js")

  
@app.route('/',methods=['POST'])
def test_post():
  body = request.get_json()
  if body != None:
    print('starting request')
    file = open("code_runner/" + body['filename'],"w")

    file.write(body['content'])

    file.close()

    print('wrote to file')

    response = None

    try:
      print('start run command')
      response = subprocess.run([body['language'],"code_runner/" + body['filename']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      response = {'returncode': str(response.returncode), 'stdout': str(response.stdout), 'stderr': str(response.stderr)}

      print('updating response')

      return jsonify(response)
    except Exception as err:
      response = err
      return jsonify(str(response))

  return jsonify('Nothing was posted')