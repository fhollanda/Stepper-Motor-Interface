#@app.endpoint('example.endpoint')
#def example():
#    return "example"

abort = "http://localhost:5001/adapter/api/abort"
captures = "http://localhost:5001/adapter/api/captures"
capture = "http://localhost:5001/adapter/api/capture/{0}/{1}"
copyright = "http://localhost:5001/adapter/api/copyright"
movement = "http://localhost:5001/adapter/api/move"
set_scope_config = "http://localhost:5001/adapter/api/scope/config"
delete_capture = "http://localhost:5001/adapter/api/capture/{0}"
motor_move = "http://localhost:5000/motor/api/move"