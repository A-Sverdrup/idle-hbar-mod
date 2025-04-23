# idle-hbar-mod
Don't you hate it when you are writing a looooong one-liner in Python and only then you suddenly notice there is no horizontal scroll?

"Always has been"

I was using python since 2017 and Python 3.1.4.

8 years and 12 versions of python later, still no horizontal scrolling.

Despite the fact that (at least, in Python 3.12) you need JUST 7 LINES to make it work:

module idlelib.editor, located in Lib/idlelib/editor.py

Insert after line 136:
```
        self.hbar = hbar = Scrollbar(text_frame, orient='horizontal',name='hbar')
```
Insert after line 228 (227 in original):
```
        hbar['command'] = self.handle_xview
        hbar.grid(row=2, column=1, sticky=NSEW)
        text['xscrollcommand'] = hbar.set
```
Insert after line 553 (549 in original):
```
    def handle_xview(self, event, *args):
        self.text.xview(event, *args)
        return 'break'
```

Note: copy and paste WITH LEADING WHITESPACES


Or, alternatively, let a script do it for you
