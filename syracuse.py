# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
def syracuse_steps(n)   :
    s = 0
    while n != 1 :
        if n  % 2 == 0 :
            n = n  // 2 
        else: 
            n = 3 * n + 1
        s = s + 1
    return s
    
def main()  : 
    for i in range (1, 100):
        s = syracuse_steps(i)
        print (i,s)
        

main()

