##########################################################
from re import *
p="""Janice is 22 and Theon is 33
Gabriel is 44 and Goey is 21  """

ages=findall(r'\d{1,2}',p)
names=findall(r'[A-Z][a-z]*',p)
#print(ages)
#print(names)
f=open("regxinpython  --edurka/regx.txt","r")
x=f.read()
#print(x)
aadhar=findall(r'\d{6,11}',x)
#print()
#print("answer",aadhar)
######################################ebox question solved 
dictt={}
for i in range(len(names)):
   dictt[names[i]]=ages[i]
#print(dictt)
######################################formed dictionary
inform=findall("inform","we need to inform him with the latest information")
##################################return the list of search element 
print(inform)
if search("inform ","we need to inform to the person belongs to "):
    print("informed is conformed")
##################################search is used to search the element 
strr="we need to inform him with the latest information"
#s=[]
for i in finditer("inform",strr):
    #i=str(i)
   # s+=[findall(r'\d{1,2}',i)]
   # print(s)
    s=i.span()
    print(s)
###########################finditer is used to return the index 

st1="Sat,hat,mat,pat,Zat,Yat,kat,rat,jay"
var1=findall("[^h-z]at",st1)  #defining the range of character
#"[Shamp]at",#[h-z]at printing according to it 
#if we put ^ then it denotes negation
#print(var1)
############################replacing the particular string 
fo="hat,rat,mat,pat"
regex=compile("[r]at")
food=regex.sub("fat",fo)
#print(food)
##############################string is replaced
####################################################################
rand="where is \\drough"
#print(search(r'\\drough',rand))
#print(r'\\dough')
####################################raw string 
randstr='''
keep the blue flag 
flying high csk
'''
#print(randstr)          #whitespaces 
regex=compile(" ")
y=regex.sub("|",randstr)
o=y.strip().split("|")
#print(o)
#--------------------------------------------------------------------
#\b:backspace 
#\f:formfeed
#\r:carriage return
#\t:tab
#\v:vertical tab
#print("enter the number of elements")
rands="12345 123 1234 1234556"
#print(findall("\d{5,8}",rands))
#######################################basic of regular expression 
###########################application of  regex

#\w[a-z A-Z 0-9 _]
#\W[^a-z A-Z 0-9 _]---for any special character we can use this 

phn="412-555-1212"
if search("\w{3}\W\w{3}\W\w{4}",phn):
    print("number is verfied")

#\s[\f,\n,\r,\t,\v]
#\S[^/f\n\r\t\v]
if search(r"\w{2,20}\s{1,4}\w{2,20}","sandy \t\nramki"):
    print("name is valid")
#-[---------------------------------------------------------]
#to verify email
email="sk162@gmail.com re937@.com santhoram2002@gmail.com sheetkrishnan62@gmail.com sheet_grkrishnan@yahoo.com"
#print("email mathches",findall(r"[\w._%+-]{1,20}@[\w]{2,10}[.][a-z]{1,3}",email))
#web scraping 
import urllib.request as u
url =u.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html")
f=url.read()
file0=f.decode()
data=findall(r'[(][\d]{3}[)] [\d]{3}-[\d]{4}',file0)
name_data=findall(r'>[A-Z][a-z]{2,7} [A-Z][a-z]*<',file0)
""" print(len(name_data))
print(len(data))

z=dict(zip(name_data,data))
print(z) """
#web scraping done by me 
##################################################
txt="rakesh kumar reddy"
c=compile(" ")
#print(search("^T.*y$",txt))
#print(findall(r"\A\sA.*\bh",txt))
#print(findall(r'\d{4,8}',txt))
#print(findall(r'reddy\Z',txt))
#\b start of the string and end of the string 
#\B not(start of the string and end of the string)
#\Aonly starting string with spaces
#\w---- character or string and digits
# \W----not(character or string and digits) 
#\s---(\n\t\r\b)
#\S---not (\n\t\r\b)
#\d---only digits
#\D--not(digits)
#\Z---pecified character is end of the string 
""" [arn] 	Returns a match where one of the specified characters (a, r, or n) are present 	
[a-n] 	Returns a match for any lower case character, alphabetically between a and n 	
[^arn] 	Returns a match for any character EXCEPT a, r, and n 	
[0123] 	Returns a match where any of the specified digits (0, 1, 2, or 3) are present 	
[0-9] 	Returns a match for any digit between 0 and 9 	
[0-5][0-9] 	Returns a match for any two-digit numbers from 00 and 59 	
[a-zA-Z] 	Returns a match for any character alphabetically between a and z, lower case OR upper case 	
[+] 	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
 """
#^---equivalent \A 
#$----equivalent to \Z
#print(split('a',txt)) [' r', 'kesh kum', 'r reddy']
#print(split('a',txt,1))[' r', 'kesh kumar reddy']

#print(c.sub('|',txt))  
#print(sub(" ","yuvan",txt,2---INTERGER REPLACES FIRST TWO OCCURANCE ))
#txt = "The rain in Spain Spanish"
#x=[]

""" for i in finditer(r"\bS\w+",txt):
    print(i.string)
    print(i.span())
    print(i.group()) """

########################################################################
import camelcase
c=camelcase.CamelCase()
#print(c.hump(strr))


##avoiding the error by try except
try:
    for i in range(1):
        print(x)
#error like synatax and intentation not supporting 
except NameError:
    print("name error ")
finally:
    print("something else")

x=7
#if x<8:
    #raise IndentationError("machine will accept the number less than 8 ") 
#intentation error 
#syntax error 
#exception
#type error
#name error 
x="i {1}have {2} this {0:.10f} dolor" #indexing formating 
print(x.format(23,45,43))
x="i have a {key}is the no of {number} please take it {boy}"
print(x.format(key=24,number=222,boy="sandy"))

