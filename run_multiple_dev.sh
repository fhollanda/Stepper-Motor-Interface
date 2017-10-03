nohup ./motor/test/mock.py > /var/log/smi/motor.log 2>&1 &
nohup ./tektronix/test/mock.py > /var/log/smi/tektronix.log 2>&1 &
nohup ./adapter/bridge.py > /var/log/smi/adapter.log 2>&1 &
nohup ./web_app/web_app.py > /var/log/smi/web_app.log 2>&1 &