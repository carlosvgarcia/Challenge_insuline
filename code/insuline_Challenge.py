
#1.-Manually or programmatically delete “ORIGIN”, “1”, “61”, “//”, and the spaces and return carriages.

#2.-Copy your results in the file preproinsulin_seq_clean.txt.

#3.-Verify that your file has 110 characters of lowercase letters, which represent the amino acids in the sequence of human preproinsulin.

#4.-Save amino acids 1-24 as lsinsulin_seq_clean.txt. Verify that your file has 24 characters.

#5.-Save amino acids 25-54 as binsulin_seq_clean.txt. Verify that your file has 30 characters.

#6.-Save amino acids 55-89 as cinsulin_seq_clean.txt. Verify that your file has 35 characters.

#7.-Save amino acids 90-110 as ainsulin_seq_clean.txt. Verify that your file has 21 characters.

print('''ORIGIN
    1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
   61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//''', file=open("insulin.txt", "a"))

list = ["1", "//", "61"," ","ORIGIN"]
with open("/content/insulin.txt","r+") as a, open("/content/cleaninsulin.txt","w") as b:
    for line in a:
        for word in list:
            line = line.replace(word,"")
        b.write(line)

x3 = open("/content/cleaninsulin.txt","r+").read()
x4 = x3[:24]
x5 = x3[25:54]
x6 = x3[55:89]
x7 = x3[90:110]

list_names = ["lsinsulin_seq_clean.txt","binsulin_seq_clean.txt","cinsulin_seq_clean.txt","ainsulin_seq_clean.txt"]
variable = [x4,x5,x6,x7]
for i in range(0,4):
  with open(list_names[i], 'w') as f:
    f.write(variable[i])
  with open(list_names[i], 'a') as f:
        f.write('\n'+f"the lenght is : {len(variable[i])} ")
