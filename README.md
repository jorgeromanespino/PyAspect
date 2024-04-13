# PyAspect
PyAspect

# PyTestTutorial: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
Following steps included in the tutorial

Create virtual enviroment

    I've followed instruction given in https://stackoverflow.com/questions/54106071/how-can-i-set-up-a-virtual-environment-for-python-in-visual-studio-code  - comment 8

    Before launch VSC, activate virtual enviroment.


    Open any py file, like acli.py, and choose a python env with 3.7 or equal version
        It's important in order to get the plugin emerging message so you could set new env
        If it doesn't work, try to delete the virtual enviroment folder, and repeat all the steps

    python3 -m venv .venv  
    source .venv/bin/activate
    pip install --upgrade pip
    pip install antlr4-python3-runtime
    pip install sqlalchemy
    pip install pymysql
    pip install pytest

App instalation
    pip install -e .

Utils
    which {tool_name}

Execution:
    pytest
    or: 
    python -m pytest
    or:
    pytest -vvv # verbose

Good practices:
    http://doc.pytest.org/en/latest/goodpractices.html


# Antlr
https://tomassetti.me/antlr-mega-tutorial/
https://tomassetti.me/antlr-mega-tutorial/#python-setup


Setting up 
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_79.jdk/Contents/Home
export CLASSPATH=".:/usr/local/lib/antlr-4.6-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.6-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java org.antlr.v4.gui.TestRig'

pip install antlr4-python3-runtime==4.6
pip uninstall antlr4-python3-runtime
pip install --upgrade antlr4-python3-runtime

Generating antlr files
antlr4 -Dlanguage=Python3 -visitor -no-listener ./aspect/core/languages/aql/Aql.g4

# Database
Creation script for database
    CREATE DATABASE pyaspectdb;
    USE pyaspectdb;
    CREATE USER 'pyaspectuserdb'@'localhost' IDENTIFIED WITH mysql_native_password BY 'aspectuserpassword2020p';
    GRANT ALL ON pyaspectdb.* TO 'pyaspectuserdb'@'localhost';
