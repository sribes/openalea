#!/bin/sh

cd core/test
nosetests --exclude="(test_package.py|test_wralea.py|test_eval.py|test_session.py|test_packagemanager.py|test_persistence.py)"
cd ../../oalab/test
nosetests
cd ../../grapheditor/test
nosetests
cd ../../visualea/test
nosetests
cd ../../vpltk/test
nosetests
#cd ../../plantalab/test
#nosetests
cd -