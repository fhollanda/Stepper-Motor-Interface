. motor/env/bin/activate
nohup python motor/test/mock.py > /var/log/smi/motor.log 2>&1 &
deactivate

. tektronix/env/bin/activate
nohup python tektronix/test/mock.py > /var/log/smi/tektronix.log 2>&1 &
deactivate

. adapter/env/bin/activate
nohup python adapter/bridge.py > /var/log/smi/adapter.log 2>&1 &
deactivate

. web_app/env/bin/activate
nohup python web_app/web_app.py > /var/log/smi/web_app.log 2>&1 &
deactivate
