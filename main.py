#--- Imports Moved To init.py & routes.py---#

from pythonic import create_app

app = create_app()

#--- Variables Moved To init.py ---#

#---  Routes Moved To routes.py  ---#

#------------- DATABASE MODELS MOVED TO models.py---------------#


if __name__ == "__main__":
    app.run(debug=True)


