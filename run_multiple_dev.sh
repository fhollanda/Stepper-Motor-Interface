. /tcc/motor/env/bin/activate
nohup python /tcc/motor/test/mock.py > /var/log/smi/motor.log 2>&1 &
deactivate

. /tcc/tektronix/comm/bin/activate
nohup python /tcc/tektronix/test/mock.py > /var/log/smi/tektronix.log 2>&1 &
deactivate

. /tcc/adapter/env/bin/activate
nohup python /tcc/adapter/bridge.py > /var/log/smi/adapter.log 2>&1 &
deactivate

. /tcc/web_app/env/bin/activate
nohup python /tcc/web_app/web_app.py > /var/log/smi/web_app.log 2>&1 &
deactivate