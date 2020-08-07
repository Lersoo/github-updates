import json, sys, re;
from dateutil import parser
from datetime import datetime

class ResponseHandler:
  COLORS = {
  "black": 30,
  "red": 31,
  "green": 32,
  "yellow": 33,
  "blue": 34,
  "magenta": 35,
  "cyan": 36,
  "white": 37,
  "bright_black": 90,
  "bright_red": 91,
  "bright_green": 92,
  "bright_yellow": 93,
  "bright_blue": 94,
  "bright_magenta": 95,
  "bright_cyan": 96,
  "bright_white": 97,
  'none': 0
  }

  FORMATS  = ['normal', 'bold', 'light', 'italic', 'underline', 'slow_blink', 'rapid_blink']

  def __init__(self, api_response, max_nb = 10, show_security_updates = True):
    self.response = api_response
    self.max_nb = max_nb
    self.show_security_updates = show_security_updates
    self.notifications = []
    self.now = datetime.now().replace(second=0, microsecond=0, minute=0)
    self.assign_values()
    self.print_result()

  def assign_values(self):
    for notification in self.response:
      repo_relation = notification['reason']
      repo_name = notification['repository']['full_name']
      notif_url  = self.extract_url(notification)
      notif_details = notification['subject']
      notif_reason = ' '.join(re.findall('[A-Z][^A-Z]*', notif_details["type"]))
      notif_date = parser.isoparse(notification["updated_at"]).replace(tzinfo=None)

      notif_object = {
        "repo_name": repo_name,
        "relation": repo_relation,
        "title": notif_details["title"],
        "reason": notif_reason,
        "url": notif_url,
        "date": notif_date
      }
      if not self.show_security_updates:
        self.notifications.append(notif_object) if notif_object["relation"] != "security_alert" else None;
      else:
        self.notifications.append(notif_object)

  def extract_url(self, notification):
    notification_detail = notification['subject']['url'].split('repos', 1)[1]
    return 'https://github.com' + notification_detail.replace('pulls', 'pull')

  def pretty_print_notification(self, notification):
      repo_name = self.color_text(f'{notification["repo_name"]}', text_color = 'bright_blue')
      repo_relation = self.format_repo_relation(notification["relation"])
      notif_title = f'{notification["title"]}'
      notif_reason = self.format_notification_reason(notification["reason"])
      url = f'{notification["url"]}'
      date = notification["date"]
      time_difference = self.round_date(self.now - date)
      separator = self.color_text('||', text_color = 'blue')

      first_line = f'{separator} {repo_name} {separator} {notif_reason} - {repo_relation} ({time_difference})'
      print(self.color_text(first_line, bg_color = 'red'))
      print(f'{notif_title}')
      print(f'{url}')
      print('-----------------------------------------------\n')

  def print_result(self):
    if self.notifications == []:
      print(f"\033[1;31;40mNo new notifications in sight!")
    else:
      sorted_notifications = sorted(self.notifications, key = lambda i: i['date'])[:self.max_nb]
      for notification in sorted_notifications:
        self.pretty_print_notification(notification)

  def format_repo_relation(self, repo_relation):
    if repo_relation == 'security_alert':
      return self.color_text('Security Alert', text_color = 'red', text_format = 'bold')
    elif repo_relation == 'comment':
      return self.color_text('Comment', text_color = 'bright_blue')
    elif repo_relation == 'author':
      return self.color_text('Author', text_color = 'cyan', text_format = 'bold')
    elif repo_relation == 'mention':
      return self.color_text('Mention', text_color = 'green')
    elif repo_relation == 'state_change':
      return self.color_text('State Changed', text_color = 'yellow')
    elif repo_relation == 'subscribed':
      return self.color_text('Subscribed', text_color = 'magenta')
    else:
      return repo_relation

  def format_notification_reason(self, reason):
    if reason == 'Pull Request':
      return self.color_text(f' {reason} ', text_color = 'yellow')
    elif reason == 'Issue':
      return self.color_text(f' {reason} ', text_color = 'blue')
    elif reason == 'Mention':
      return self.color_text(f' {reason} ', text_color = 'magenta')
    elif reason == 'Repository Vulnerability Alert':
      return self.color_text(f' {reason} ', text_color = 'red')
    else:
      return self.color_text(f' {reason} ')


  def color_text(self, string, text_color = 'white', bg_color = 'none', text_format = 'normal'):
    text_color = self.COLORS[text_color]
    bg_color = self.COLORS[bg_color] + 10
    text_format = self.FORMATS.index(text_format)
    return f'\033[{text_format};{text_color};{bg_color}m{string:>}\u001b[0m'

  def round_date(self, date):
    total_hours = round(date.total_seconds() / 3600)
    if total_hours > 24:
      days = 'days' if int(total_hours / 24) > 1 else 'day'
      return f'{int(total_hours / 24)} {days}, {total_hours % 24} hours ago'
    else:
      return f'{total_hours} hours ago'
