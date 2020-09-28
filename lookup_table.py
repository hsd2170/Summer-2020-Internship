#!/usr/bin/env python3

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
	"T" : "thereonine",
	"C" : "cysteine",
	"M" : "methionine",
	"N" : "asparagine",
	"Q" : "glutamine"
	}
#print(amino_acid_dict)	


#open file with amino acid sequence to read it , set handle
with open ("masp1_latrodectus_hesperus.faa", "r") as in_handle:

#interpret handle and set interpretation to variable
        amino_acid_genome = in_handle.read()

#prompt user for amino acid they are looking for
value = input("What amino acid are you looking for? ")

#check if legal value entered
#allow uppercase and lowercase
#permit for both key and value inputs
if(len(value) > 2):
	value = list(amino_acid_dict.keys())[list(amino_acid_dict.values()).index(value)]
#print(value)

#create counter variables for amino acids
glutamine_counter =  0
asparagine_counter = 0
methionine_counter = 0
cysteine_counter = 0
thereonine_counter = 0
serine_counter = 0
alanine_counter = 0
glycine_counter = 0
isoleucine_counter = 0
proline_counter = 0
caline_counter = 0
phenylalanine_counter = 0
tryptophan_counter = 0
tyrosine_counter = 0
asparatic_acid_counter = 0
glutamic_acid_counter = 0
argenine_counter = 0
histidine_counter = 0
lysine_counter = 0

counter = 0

#look through file and count number of times each amino acid appears
for item in amino_acid_genome:
	if value == item:
		counter +=1

#alternative way to print
#print("The number of glutamine in this file is " + str(counter))

print("The number of " + amino_acid_dict[value] + " in this file is " +  str(counter))
