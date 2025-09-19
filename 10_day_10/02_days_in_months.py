def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        
        return True
      else:
        
        return False
    else:
      
      return True
  else:
    
    return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  """
  Takes year and month as input and in what year in which month how many days are there.
  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  # This block now ONLY handles updating the list
  if is_leap(year):
    month_days[1] = 29
    
  # ✅ Correctly un-indented!
  # This line now runs for ALL cases, after the check is done.
  return month_days[month - 1]
  
  


  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)