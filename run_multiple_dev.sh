. /Stepper-Motor-Interface/motor/env/bin/activate
nohup python /Stepper-Motor-Interface/motor/test/mock.py > /var/log/smi/motor.log 2>&1 &
deactivate

. /Stepper-Motor-Interface/tektronix/env/bin/activate
nohup python /Stepper-Motor-Interface/tektronix/test/mock.py > /var/log/smi/tektronix.log 2>&1 &
deactivate

. /Stepper-Motor-Interface/adapter/env/bin/activate
nohup python /Stepper-Motor-Interface/adapter/bridge.py > /var/log/smi/adapter.log 2>&1 &
deactivate

. /Stepper-Motor-Interface/web_app/env/bin/activate
nohup python /Stepper-Motor-Interface/web_app/web_app.py > /var/log/smi/web_app.log 2>&1 &
deactivate
