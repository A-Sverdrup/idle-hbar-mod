from sys import version_info
try:
    assert version_info[0]==3 and version_info[1]==12
    import idlelib.editor
    file=idlelib.editor.__file__
    first=second=third=fourth=''
    line=0
    with open(file)as f,open(file+'.bak','w')as f2:f2.write(f.read())#Preserve the original just in case
    with open(file)as f:#Read and split
        while l:=f.readline():
            line+=1
            if line<=136:first+=l
            elif line<=227:second+=l
            elif line<=549:third+=l
            else:fourth+=l
    with open(file,'w')as f:#Apply mod
        f.write(first)
        f.write("        self.hbar = hbar = Scrollbar(text_frame, orient='horizontal',name='hbar')\n")
        f.write(second)
        f.write('''        hbar['command'] = self.handle_xview
        hbar.grid(row=2, column=1, sticky=NSEW)
        text['xscrollcommand'] = hbar.set
''')
        f.write(third)
        f.write('''    def handle_xview(self, event, *args):
        self.text.xview(event, *args)
        return 'break'
''')
        f.write(fourth)
    print('Done!')
except AssertionError:
    print('You are not using Python 3.12')
