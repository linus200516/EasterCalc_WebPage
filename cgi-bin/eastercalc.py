#!/usr/bin/python3
import cgi

print('Content-Type: text/html; charset=utf-8')
print('')


form = cgi.FieldStorage()
yearStr = form.getvalue('theYear')
calculation = form.getvalue('calculation')

def Easter2(y): 
  a = y % 19   
  b = y // 100   
  c = y % 100   
  d = b // 4   
  e = b % 4   
  g = (8 * b + 13) // 25   
  h = (19 * a + b - d - g + 15) % 30   
  j = c // 4 
  k = c % 4 
  m = (a + 11 * h) // 319 
  r = (2 * e + 2 * j - k - h + m + 32) % 7 
  n = (h - m + r + 90) // 25 
  p = (h - m + r + n + 19) % 32 
  return(f"{p}/{n}/{y}") 


def Easter1(y): 
  months = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

  a = y % 19   
  b = y // 100   
  c = y % 100   
  d = b // 4   
  e = b % 4   
  g = (8 * b + 13) // 25   
  h = (19 * a + b - d - g + 15) % 30   
  j = c // 4 
  k = c % 4 
  m = (a + 11 * h) // 319 
  r = (2 * e + 2 * j - k - h + m + 32) % 7 
  n = (h - m + r + 90) // 25 
  p = (h - m + r + n + 19) % 32 
  
  if p in [1,21,31]:
    sup = 'st'
  elif p in [2,22]:
    sup = 'nd'
  elif p in [3,23]:
    sup = 'rd'
  else:
    sup = 'th'
    
  
  mword = months[n]
  return(f"{p}<sup>{sup}</sup> {mword} {y}") 
  
   

def Easter3(y): 
  months = {
        1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"
    }

  a = y % 19   
  b = y // 100   
  c = y % 100   
  d = b // 4   
  e = b % 4   
  g = (8 * b + 13) // 25   
  h = (19 * a + b - d - g + 15) % 30   
  j = c // 4 
  k = c % 4 
  m = (a + 11 * h) // 319 
  r = (2 * e + 2 * j - k - h + m + 32) % 7 
  n = (h - m + r + 90) // 25 
  p = (h - m + r + n + 19) % 32 
  
  
  
  if p in [1,21,31]:
    sup = 'st'
  elif p in [2,22]:
    sup = 'nd'
  elif p in [3,23]:
    sup = 'rd'
  else:
    sup = 'th'
    
  #print(f"{p}/{n}/{y}")
  mword = months[n]
  #print(f"{p} {mword} {y}") 
  return(f"{p}/{n}/{y} and in verbose {p}<sup>{sup}</sup> {mword} {y} ")

try:
  if yearStr and yearStr.isdigit():
    year = int(yearStr)
    if calculation == "Numerical date":
        message = Easter2(year)
    elif calculation == "Verbose":
        message = Easter1(year)
    else:
        message = Easter3(year)
  else:
    message = "please enter a valid year"
except (TypeError, ValueError):
    message = "Please enter a valid number."

#print(f"<p>{message}</p>")



print('<!DOCTYPE html>')
print('<html>')
print("<head")
print('<title> Easter Sunday calculation </title>')
print('<link rel="stylesheet" href="../coursework part 2/secondpage.css">')
print("</head>")
print('<body>')
print()
print('<h2>')
print(f"<p>{message}</p>")
print('</h2>')
print('</body>')
print('</html>')
