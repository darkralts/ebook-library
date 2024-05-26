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
