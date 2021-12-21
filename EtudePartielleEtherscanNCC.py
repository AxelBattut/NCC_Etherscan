# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:39:52 2021

@author: SESSIONSOUFIANE
"""

""" Txhash,"Blockno","UnixTimestamp","DateTime","From","To","Quantity","Method" """

def moyennetransaction():
    import csv
    with open(r"C:\Users\axelb\Downloads\ncceth.csv") as file:
        reader = csv.reader(file)
        next(file)
        
        grosportefeuille = 0
        petitportefeuille = 0
        montantpetitportefeuille = 0
        montantgrosportefeuille = 0
        montantportefeuilletotal =0
        count = 0
        for row in reader:
            
            nbtokensswap = 7000 
            """ contante simplement si on veut faire le calcul sur un nombre reduit de cellules"""
            
            
            if count < nbtokensswap:
                
                
                nbtokens = float(row[6].replace(',', ''))
                nbtokensint = int(nbtokens)
                
                """print(nbtokens)"""
                """print(nbtokensint)"""
                
                count = count +1
                nombrevariable = 144693
                if nbtokensint > nombrevariable:
                    grosportefeuille = grosportefeuille +1
                    montantportefeuilletotal =montantportefeuilletotal+ nbtokensint
                    montantgrosportefeuille = montantgrosportefeuille +1
                
                else:
                    petitportefeuille = petitportefeuille +1
                    montantportefeuilletotal =montantportefeuilletotal + nbtokensint
                    montantpetitportefeuille = montantpetitportefeuille +1
            else:
                break
                
                
        print("On a donc ", petitportefeuille, " transactions qui ont eu lieu avec un montant swappé inférieur à ", nbtokensswap, " tokens NCC")
        print("Et nous avons ", grosportefeuille, " transactions qui ont eu lieu avec un montant swappé supérieur à ", nbtokensswap, " tokens NCC")
        print("La moyenne de NCC par transaction qui sont echangés est de ", montantportefeuilletotal/count, " NCC")
        
    
    
def similarites():
    
    import csv
    with open(r"C:\Users\axelb\Downloads\ncceth.csv") as file:
        reader = csv.reader(file)
        next(file)
        
        
        
        a = []
        for row in reader:
            a.append(row[4])
            
            
        seen = set()
        uniq = []
        for x in a:
            if x not in seen:
                uniq.append(x)
                seen.add(x)
            
        print("Nous pouvons donc constater qu'il y a ", len(seen) , " adresses uniques qui ont interagi avec le contrat NCC")
        
        
        
        
        
"""  HolderAddress,"Balance","PendingBalanceUpdate"     """
      
def repartitionholders():
    import csv
    supply =  657440000
    nbholders = 3649
    
    with open(r"C:\Users\axelb\Downloads\tokenholdersncc.csv") as file:
        reader = csv.reader(file)
        next(file)
        
        
        baleine = 0
        michou = 0
        nbtokensbaleine = 0
        nbtokensmichou = 0
        
        for row in reader:
            """print(row[1])"""
            nbtokens = float(row[1])
            nbtokensint = int(nbtokens)
            
            nombrencccomparatif = 450000 
            if nbtokensint > nombrencccomparatif:
                baleine = baleine +1
                nbtokensbaleine = nbtokensbaleine+ nbtokensint
                
            else :
                michou = michou +1 
                nbtokensmichou =nbtokensmichou + nbtokensint
            
        print("Il y a ", baleine, "(", baleine/nbholders*100 ,"%) adresses qui detiennent ", nbtokensbaleine/supply*100, "% de la supply de NCC" )
        print("Ce sont les adresses à plus gros portefeuille qui detiennent plus de ", nombrencccomparatif, " tokens NCC")
        print("Le reste des portefeuilles qui detiennent moins de ", nombrencccomparatif , " tokens NCC sont au nombre de ", michou , " et représentent ", nbtokensmichou/supply*100, "% de la supply")
                
        
        
        
        
repartitionholders()
""""moyennetransaction()   """ 
"""similarites()"""
    
            
            
        

