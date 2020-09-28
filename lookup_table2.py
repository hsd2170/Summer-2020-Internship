#!/usr/bin/env python3
import argparse
import os

#create dictionary
amino_acid_dict = {
	"A" : "alanine",
	"G" : "glycine",
	"I" : "isoleucine",
	"P" : "proline",
	"V" : "caline",
	"F" : "phenylalanine",
	"W" : "tryptophan",
	"Y" : "tyrosine",
	"D" : "asparatic acid",
	"E" : "glutamic acid",
	"R" : "argenine",
	"H" : "histidine",
	"K" : "lysine",
	"S" : "serine",
	"T" : "threonine",
	"C" : "cysteine",
	"M" : "methionine",
	"N" : "asparagine",
	"Q" : "glutamine"
	}
#print(amino_acid_dict)	

#using argparse to allow the user to input file name
parser = argparse.ArgumentParser(description = "promt the user for file entry")
parser.add_argument("fileone", help = "enter the first file you would like to use")
parser.add_argument("filetwo", help = "enter the second file you would like to use")
args = parser.parse_args()

with open(args.fileone, "r") as in_handle:
	amino_acid_genome = in_handle.read()
with open(args.filetwo, "r") as in_handle2:
	amino_acid_genome2 = in_handle2.read()

#check to make sure files aren't empty
filesize1 = os.path.getsize(args.fileone)
print("The first file you entered is empty")

filesize2 = os.path.getsize(args.filetwo)
print("The second file you entered is empty")


#create counter variables for amino acids
glutamine_counter =  0
asparagine_counter = 0
methionine_counter = 0
cysteine_counter = 0
threonine_counter = 0
serine_counter = 0
alanine_counter = 0
glycine_counter = 0
isoleucine_counter = 0
leucine_counter = 0
proline_counter = 0
valine_counter = 0
phenylalanine_counter = 0
tryptophan_counter = 0
tyrosine_counter = 0
asparatic_acid_counter = 0
glutamic_acid_counter = 0
argenine_counter = 0
histidine_counter = 0
lysine_counter = 0
arginine_counter = 0
     
#look through file and count number of times each amino acid appears
for item in amino_acid_genome:
	if "Q" == item:
		glutamine_counter +=1
	if "A" == item:
		alanine_counter+=1
	elif "G" == item:
		glycine_counter+=1
	elif "I" == item:
		isoleucine_counter+=1
	elif "L" == item:
		leucine_counter+=1
	elif "P" == item:
		proline_counter+=1
	elif "V" == item:
		valine_counter+=1
	elif "F" == item:
		phenylalanine_counter+=1
	elif "W" == item:
		tryptophan_counter+=1
	elif "Y" == item:
		tyrosine_counter+=1
	elif "D" == item:
		asparatic_acid_counter+=1
	elif "E" == item:
		glutamic_acid_counter+=1
	elif "R" == item:
		arginine_counter+=1
	elif "H" == item:
		histidine_counter+=1
	elif "K" == item:
		lysine_counter+=1
	elif "S" == item:
		serine_counter+=1
	elif "T" == item:
		threonine_counter+=1
	elif "C" == item:
		cysteine_counter+=1
	elif "M" == item:
		methionine_counter+=1
	elif "N" == item:
		asparagine_counter+=1
try:
	with open("FileA_output.txt","w") as out_handle:
		out_handle.write("The number of glutamine in this file is " + str(glutamine_counter))
		out_handle.write("\nThe number of alanine in this file is " + str(alanine_counter))
		out_handle.write("\nThe number of glycine in this file is " + str(glycine_counter))
		out_handle.write("\nThe number of isoleucine in this file is " + str(isoleucine_counter))
		out_handle.write("\nThe number of leucine in this file is " + str(leucine_counter))
		out_handle.write("\nThe number of proline in this file is " + str(proline_counter))
		out_handle.write("\nThe number of valine in this file is " + str(valine_counter))
		out_handle.write("\nThe number of phenylalanine in this file is " + str(phenylalanine_counter))
		out_handle.write("\nThe number of tryptophan in this file is " + str(tryptophan_counter))
		out_handle.write("\nThe number of tyrosine in this file is " + str(tyrosine_counter))
		out_handle.write("\nThe number of asparatic acid in this file is " + str(asparatic_acid_counter))
		out_handle.write("\nThe number of glutamic acid in this file is " + str(glutamic_acid_counter))
		out_handle.write("\nThe number of arginine in this file is " + str(arginine_counter))
		out_handle.write("\nThe number of histidine in this file is " + str(histidine_counter))
		out_handle.write("\nThe number of lysine in this file is " + str(lysine_counter))
		out_handle.write("\nThe number of serine in this file is " + str(serine_counter))
		out_handle.write("\nThe number of threonine in this file is " + str(threonine_counter))
		out_handle.write("\nThe number of cysteine in this file is " + str(cysteine_counter))
		out_handle.write("\nThe number of methionine in this file is " + str(methionine_counter))
		out_handle.write("\nThe number of asparagine in this file is " + str(asparagine_counter))

except IOError as err:
#this is the exception error that will help skip over syntax errors
	print("IOError")

#open file with amino acid sequence to read it , set handle
#with open ("masph_nephila_clavipes.faa", "r") as in_handle2:

#interpret handle and set interpretation to variable
#        amino_acid_genome2 = in_handle2.read()

glutamine_counter2 =  0
asparagine_counter2 = 0
methionine_counter2 = 0
cysteine_counter2 = 0
threonine_counter2 = 0
serine_counter2 = 0
alanine_counter2 = 0
glycine_counter2 = 0
isoleucine_counter2 = 0
leucine_counter2 = 0
proline_counter2 = 0
valine_counter2 = 0
phenylalanine_counter2 = 0
tryptophan_counter2 = 0
tyrosine_counter2 = 0
asparatic_acid_counter2 = 0
glutamic_acid_counter2 = 0
argenine_counter2 = 0
histidine_counter2 = 0
lysine_counter2 = 0
arginine_counter2 = 0

for item in amino_acid_genome2:
        if "Q" == item:
                glutamine_counter2 +=1
        if "A" == item:
                alanine_counter2+=1
        elif "G" == item:
                glycine_counter2+=1
        elif "I" == item:
                isoleucine_counter2+=1
        elif "L" == item:
                leucine_counter2+=1
        elif "P" == item:
                proline_counter2+=1
        elif "V" == item:
                valine_counter2+=1
        elif "F" == item:
                phenylalanine_counter2+=1
        elif "W" == item:
                tryptophan_counter2+=1
        elif "Y" == item:
                tyrosine_counter2+=1
        elif "D" == item:
                asparatic_acid_counter2+=1
        elif "E" == item:
                glutamic_acid_counter2+=1
        elif "R" == item:
                arginine_counter2+=1
        elif "H" == item:
                histidine_counter2+=1
        elif "K" == item:
                lysine_counter2+=1
        elif "S" == item:
                serine_counter2+=1
        elif "T" == item:
                threonine_counter2+=1
        elif "C" == item:
                cysteine_counter2+=1
        elif "M" == item:
                methionine_counter2+=1
        elif "N" == item:
                asparagine_counter2+=1
try:
	with open("FileB_output.txt","w") as out_handle2:
		out_handle2.write("The number of glutamine in this file is " + str(glutamine_counter2))
		out_handle2.write("\nThe number of alanine in this file is " + str(alanine_counter2))
		out_handle2.write("\nThe number of glycine in this file is " + str(glycine_counter2))
		out_handle2.write("\nThe number of isoleucine in this file is " + str(isoleucine_counter2))
		out_handle2.write("\nThe number of leucine in this file is " + str(leucine_counter2))
		out_handle2.write("\nThe number of proline in this file is " + str(proline_counter2))
		out_handle2.write("\nThe number of valine in this file is " + str(valine_counter2))
		out_handle2.write("\nThe number of phenylalanine in this file is " + str(phenylalanine_counter2))
		out_handle2.write("\nThe number of tryptophan in this file is " + str(tryptophan_counter2))
		out_handle2.write("\nThe number of tyrosine in this file is " + str(tyrosine_counter2))
		out_handle2.write("\nThe number of asparatic acid in this file is " + str(asparatic_acid_counter2))
		out_handle2.write("\nThe number of glutamic acid in this file is " + str(glutamic_acid_counter2))
		out_handle2.write("\nThe number of arginine in this file is " + str(arginine_counter2))
		out_handle2.write("\nThe number of histidine in this file is " + str(histidine_counter2))
		out_handle2.write("\nThe number of lysine in this file is " + str(lysine_counter2))
		out_handle2.write("\nThe number of serine in this file is " + str(serine_counter2))
		out_handle2.write("\nThe number of threonine in this file is " + str(threonine_counter2))
		out_handle2.write("\nThe number of cysteine in this file is " + str(cysteine_counter2))
		out_handle2.write("\nThe number of methionine in this file is " + str(methionine_counter2))
		out_handle2.write("\nThe number of asparagine in this file is " + str(asparagine_counter2))

except IOError as err:
#this is the exception error that will help skip over syntax errors
        print("IOError")


#comparing two files
try:
	with open("fileA_fileB_comparison.txt","w") as out_handle3:
		out_handle3.write("The number of glutamine in File A is " + str(glutamine_counter) + " and in File B is " +  str(glutamine_counter2))
		out_handle3.write("\nThe number of alanine in File A is "+ str(alanine_counter) + " and in File B is " + str(alanine_counter2))
		out_handle3.write("\nThe number of glycine in File A is " + str(glycine_counter) + " and in File B is " + str(glycine_counter2))
		out_handle3.write("\nThe number of isoleucine in File A is " + str(isoleucine_counter) + " and in File B is " + str(isoleucine_counter2))
		out_handle3.write("\nThe number of leucine in File A is " + str(leucine_counter) + " in File B is " + str(leucine_counter2))
		out_handle3.write("\nThe number of proline in File A is " + str(proline_counter) + " and in File B is " + str(proline_counter2))
		out_handle3.write("\nThe number of valine in File A is " + str(valine_counter) + " and in File B is "+ str(valine_counter2))
		out_handle3.write("\nThe number of phenylalanine in File A is " + str(phenylalanine_counter) + " and in File B is " + str(phenylalanine_counter2))
		out_handle3.write("\nThe number of tryptophan in File A is " + str(tryptophan_counter) + " and in File B is " + str(tryptophan_counter2))
		out_handle3.write("\nThe number of tyrosine in File A is " + str(tyrosine_counter) + " and in File B is " + str(tyrosine_counter2))
		out_handle3.write("\nThe number of asparatic acid in File A is " + str(asparatic_acid_counter) + " and in File B is " + str(asparatic_acid_counter2))
		out_handle3.write("\nThe number of glutamic acid in File A is " + str(glutamic_acid_counter) + " and in File B is " + str(glutamic_acid_counter2))
		out_handle3.write("\nThe number of arginine in File A is " + str(arginine_counter) + " and in File B is " + str(arginine_counter2))
		out_handle3.write("\nThe number of histidine in File A is " + str(histidine_counter) + " and in File B is " + str(histidine_counter2))
		out_handle3.write("\nThe number of lysine in File A is " + str(lysine_counter) + " and in File B is " + str(lysine_counter2))
		out_handle3.write("\nThe number of serine in File A is " + str(serine_counter) + " and in File B is " + str(serine_counter2))
		out_handle3.write("\nThe number of threonine in File A is " + str(threonine_counter) + " and the in File B is " + str(threonine_counter2))
		out_handle3.write("\nThe number of cysteine in File A is " + str(cysteine_counter) + " and the in File B is " + str(cysteine_counter2))
		out_handle3.write("\nThe number of methionine in File A is " + str(methionine_counter) + " and in File B is " + str(methionine_counter2))
		out_handle3.write("\nThe number of asparagine in File A is " + str(asparagine_counter) + " and in File B is " + str(asparagine_counter2))

except IOError as err:
	print("IOError")
