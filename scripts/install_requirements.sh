. motor/env/bin/activate
pip install -r motor/requirements.txt
deactivate

. tektronix/env/bin/activate
pip install -r tektronix/requirements.txt
deactivate

. adapter/env/bin/activate
pip install -r adapter/requirements.txt
deactivate

. web_app/env/bin/activate
pip install -r web_app/requirements.txt
deactivate
