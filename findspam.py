import re


class FindSpam:
  rules = [
   {'regex': "\\b(baba(ji)?|vashikaran|here is|porn)\\b", 'all': True,
    'sites': [], 'reason': "Bad keyword detected"},
   {'regex': "\\+\\d{10}|\\+?\\d{2}[\\s\\-]?\\d{8,11}", 'all': True, 
    'sites': ["patents.stackexchange.com"], 'reason': "Phone number detected"},
   {'regex': "\\b(asshole|crap|fag|fuck|idiot|shit|whore)s?\\b", 'all': True,
    'sites': [], 'reason': "Offensive title detected"},
   {'regex': "^[A-Z0-9\\.\\-\\?\\s'\"]*$", 'all': True, 'sites': [], 'reason': "All-caps title"}
  ]

  @staticmethod
  def testpost(title, site):
    result = [];
    for rule in FindSpam.rules:
      if rule['all'] != (site in rule['sites']):
        if re.compile(rule['regex']).search(title):
          result.append(rule['reason'])
    return result

  @staticmethod
  def testtitle(title):
    regexes=["\\b(baba(ji)?|vashikaran|fashion|here is|porn)\\b","\\+\\d{10}","\\+?\\d{2}\\s?\\d{8}","\\b(asshole|crap|fag|fuck|idiot|shit|whore)s?\\b"]
    result = []
    p = [not not re.compile(s).search(title) for s in regexes]
    if 'vashikaran' in title or 'baba' in title or True in p:
      result.append('Possible spam')
      # magic if matches word
    return result
