@REM From repository root folder create new apps under project/apps
cd project/apps
python ../../manage.py startapp %1
cd ../..