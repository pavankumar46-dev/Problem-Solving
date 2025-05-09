string = 'tree'
diction = {}
for i in string:
    if i not in diction:
        diction[i] = 1
    else:
        diction[i] = diction[i]+1
        
print(diction)

out = dict(sorted(diction.items(), key=lambda item: item[1], reverse=True))
samp = ''
for key,val in out.items():
    samp=samp+(key*val)
    
print(samp)
## Output eert
