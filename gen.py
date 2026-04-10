import os  
def wf(p, t):  
    os.makedirs(os.path.dirname(p), exist_ok=True)  
    with open(p, 'w', encoding='utf-8') as f: f.write(t)  
    print('Written: ' + str(len(t)) + ' chars - ' + p)  
print('gen.py ready')  
