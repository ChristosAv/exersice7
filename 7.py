import random

light1 = -1
light2 = -2
light3 = -3
while light1 != light2 and light2 != light3 and light1 != light3:
    light1 = random.randint(0, 100) #Στις επομενες 3 εντολες οριζω 3 μεταβλητες. Καθε μια απο αυτες αντιπροσωπευει και ενα φαναρι.
    light2 = random.randint(0, 100) # Οποτε τους αποδιδουμε τυχαια ενα Θετικο αριθμο εως το 100
    light3 = random.randint(0, 100)
    
print(light1, light2, light3)   #Εκτυπωση αποτελεσματων


while light1 > 0 and light2 > 0 and light3 > 0: #Παρολο που η εκφωνηση δεν δινει κριτιριο τερματισμου, επιλεγω σημειο τερματισμου τον μηδενισμο μιας μεταβλητης
    x = random.randint(5,10)    #Σε μια μεταβλητη εκχωτω μια τυχαια τιμη μεταξυ 5 και 10
    y = random.randint(0,5)     #Σε μια μεταβλητη εκχωτω μια τυχαια τιμη μεταξυ
    z = random.randint(0,5)     #ομοιως
    
    if light1 > light2 and light1 > light3 :     #Στους επομενους ελεγχους που ακολουθουν, εξεταζω τις maximum τιμες, και αναλογως προσθετω και αφαιρω 
        light1 -= x
        light2 += y
        light3 += z
        
        if light1 > x:          #Εξεταζω αν το φαναρι θα εχει μικροτερη ουρα απο την τιμη της RNG x 
            print("Traffic light 1 is Green and there are ", light1,"cars in queu. \n\
            Traffic lights 2 and 3 are Red and there are ",light2,",", light3," cars in queu, respectivelly.")
            print("Traffic light 1 has", light1 ,"cars.", x," cars left the queu. Also ", y, z,"cars added in \n\
            the queu for traffic light 2 and 3.")
        else:                   #Αν ναι, τοτε αγνοουμε την τιμη RNG και την καθοριζουμε σε 0. Ομοια εξεταζουμε και τις περιπτωσεις και για τα αλλα 2 φαναρια.
            light1 = 0
            print("Traffic light 1 has zero cars in queu. Also ", y, z,"cars added in the queu for traffic light 2 and 3.")
    
    elif light2 > light1 and light2 > light3: 
        light2 -= x
        light1 += y
        light3 += z
        if light2 > x:
            print("Traffic light 2 is Green and there are ", light2,"cars in queu. \n\
            Traffic lights 1 and 3 are Red and there are ",light1,",", light3," cars in queu, respectivelly.")
            print("Traffic light 2 has", light2 ,"cars.", x," cars left the queu. Also ", y, z,"cars added in \n\
            the queu for traffic light 1 and 3.")
        else:
            light2 = 0
            print("Traffic light 2 has zero cars in queu. Also ", y, z,"cars added in the queu for traffic light 2 and 3.")
    
    else:
        light3 -= x
        light1 += y
        light2 += z
        if light3 > x:
            print("Traffic light 3 is Green and there are ", light3,"cars in queu. \n\
            Traffic lights 1 and 2 are Red and there are ",light1,",", light2," cars in queu, respectivelly.")
            print("Traffic light 3 has", light3 ,"cars.", x," cars left the queu. Also ", y, z,"cars added in \n\
            the queu for traffic light 1 and 2.")
        else:
            light3 = 0
            print("Traffic light 3 has zero cars in queu. Also ", y, z,"cars added in the queu for traffic light 2 and 3.")
            
            
            