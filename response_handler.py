import json, sys, re;
from dateutil import parser
from datetime import datetime

response = json.loads(' '.join(sys.argv[1:]))

class ResponseHandler:
  def __init__(self, api_response):
    self.response = api_response
    self.notifications = []
    self.assign_values()
    self.print_result()

  def assign_values(self):
    for notification in self.response:
      repo_info = notification['repository']
      repo_relation = notification['reason']
      repo_name = notification['repository']['full_name']
      notif_url = "https://api.github.com/" + repo_name
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
      self.notifications.append(notif_object)

  def pretty_print_notification(self, notification):
      repo_name = f'\033[1;32;40m{notification["repo_name"]}\u001b[0m'
      repo_relation = f'{notification["relation"]:<5}'
      notif_title = f'{notification["title"]}'
      notif_reason = self.format_notification_reason(notification["reason"])
      url = f'{notification["url"]}'
      date = notification["date"]
      now = datetime.now()

      print(f'{repo_name} - {repo_relation} - {abs(now - date)} hours ago')
      print(f'{notif_reason} \t {notif_title}')
      print(f'{url}')
      print('----------------------------------\n')

  def print_result(self):
    if self.notifications == []:
      print(f"\033[1;31;40m No new notifications in sight!")
    for notification in self.notifications:
      self.pretty_print_notification(notification)

  def format_notification_reason(self, reason):
    if reason == 'Pull Request':
      color = 33
    elif reason == 'Issue':
      color = 34
    elif reason == 'Mention':
      color = 35
    return f'\033[1;{color};40m{reason:>}\u001b[0m'

ResponseHandler(response)