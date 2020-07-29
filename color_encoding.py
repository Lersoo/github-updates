COLORS = {
  "black": 30,
  "red": 31,
  "green": 32,
  "yellow": 33,
  "blue": 34,
  "magenta": 35,
  "cyan": 36,
  "white": 37
}

def color_text(color_string, string):
  if color_string == 'black':
    color = COLORS['black']
  elif color_string == 'red':
    color = COLORS['red']
  elif color_string == 'green':
    color = COLORS['green']
  elif color_string == 'yellow':
    color = COLORS['yellow']
  elif color_string == 'blue':
    color = COLORS['blue']
  elif color_string == 'magenta':
    color = COLORS['magenta']
  elif color_string == 'cyan':
    color = COLORS['cyan']
  else:
    color = COLORS['white']
  return f'\033[0;{color};40m{string}\u001b[0m'


print(color_text('blablablalb', "Bonjour c'est Thomas"))