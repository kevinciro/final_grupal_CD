from login_reg import app
from login_reg.controllers import users_controller
from login_reg.controllers import fligths_controller
from login_reg.controllers import bills_controller
from login_reg.controllers import seats_controller

if __name__ == '__main__':
    app.run()
    debug = True
