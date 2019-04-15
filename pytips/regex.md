## Datetime extraction
```py
str_time = 'asdf asdf 2019-04-15 03:37 PM ET asdfasdfas'
date_pattern = r"2019-[0-1][1-9]-[0-3][0-9]\s\d+:\d+\s([aApP][Mm])\sET"
if bool(re.search(date_pattern, str_time)):
    dt = datetime.strptime(
                re.search(date_pattern, str_time)[0], 
                '%Y-%m-%d %I:%M %p ET'
         )
 ```
