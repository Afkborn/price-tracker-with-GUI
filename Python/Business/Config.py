import configparser


class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file)

    def get_config(self, section, option):
        return self.config.get(section, option)
    


    def set_config(self, section, option, value):
        if not self.config.has_section(section) and section != 'DEFAULT':
            self.config.add_section(section)
        self.config.set(section, option, value)


    def save_config(self):
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)

# config = configparser.ConfigParser()
# config['DEFAULT'] = {'headless':True}

# with open('config.ini','w') as configfile:
#     config.write(configfile)

# myConfig = Config("config.ini")
# print(myConfig.get_config('DEFAULT', 'headless'))
# myConfig.set_config('DEFAULT', 'headless', 'True')

