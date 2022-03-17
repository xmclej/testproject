echo off
cls
echo.

if "%1" == "" (goto BLANK) else (goto RUN)

:BLANK
echo Project name required as first input. Use "project" then rename with prefix of solution
echo App name required as second input. This gets placed into subfolders of "project/apps"
goto DONE

:RUN
echo running code
pipenv install django==3.2.7
django-admin startproject %1
cd %1
mkdir apps
cd apps
python manage.py startapp %2
cd ../..
goto DONE

:DONE
echo done!