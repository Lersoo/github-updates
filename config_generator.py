import os, json, requests;
from time import sleep;

class ConfigGenerator:
  def __init__(self):
    if not os.path.exists("config.json"):
      os.system('touch config.json')
      os.system('echo "{}" >> config.json')

    jsonFile = open("config.json", "r")
    self.current_config = json.load(jsonFile)
    jsonFile.close()
    self.current_config = json.load(open('./config.json'))
    self.set_config()
    self.check_config()

  def set_config(self):
    config = {
      "github_username": self.ask_username(self.current_config.get('github_username')),
      "github_bearer_token": self.ask_api_key(self.current_config.get('github_bearer_token')),
      "max_nb_notifications": self.ask_max_nb(self.current_config.get('max_nb_notifications')),
    }
    jsonFile = open("config.json", "w+")
    jsonFile.write(json.dumps(config))

  def ask_username(self, current_value):
    os.system('clear')
    print('Enter your github username:')
    print(f'Current: {current_value}, press Enter to skip')
    return self.return_value(input(), current_value)

  def ask_api_key(self, current_value):
    os.system('clear')
    print('Enter your API key: (you can get an API key at \033[1;31mhttps://github.com/settings/tokens\u001b[0m)')
    print(f'Current: {current_value}, press Enter to skip')
    return self.return_value(input(), current_value)

  def ask_max_nb(self, current_value):
    os.system('clear')
    print('How many notifications do you want to see maximum?')
    print(f'Current: {current_value}, press Enter to skip')
    return self.return_value(input(), current_value)


  def ask_security_updates(self, current_value):
    print('Do you want to see security updates? Y/N')
    answer = input().upper()
    while answer != 'Y' and answer != 'N':
      answer = input().upper()
    return self.return_value(answer, current_value)


  def return_value(self, value, current_value):
    if value == '':
      return current_value
    else:
      return value