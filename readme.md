![image](https://github.com/darkralts/ebook-library/assets/16366107/a195b405-8f03-421a-9f96-b595748483f3)

hello there. so you use this by putting in .bashrc something like: 
```bash
alias library='python /home/ichigo/.scripts/books.py'
```
or bind a key to open a terminal with the library
```bash
bindsym $mod+Shift+l exec i3-sensible-terminal -e "bash -ic 'library'"
```

requirements: 
- `epy`
- `python-blessed`

thank you for checking it out!!!! ^~^
