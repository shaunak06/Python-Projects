# -*- coding: utf-8 -*-
import poplib
from email import parser
import getpass
import re



def getEmailData(password):
    pop_conn = poplib.POP3_SSL('pop.gmail.com')
    pop_conn.user('shaunak06')
    pop_conn.pass_(password)
    #get messages from server
    utel=set()
    #print pop_conn.list()
    print "Total Messages", len(pop_conn.list()[1])
    for i in range(1, len(pop_conn.list()[1])+1):
        msg= pop_conn.retr(i)
        #print msg
        
        msgparts = parser.Parser().parsestr("\n".join(msg[1]))
        #print "Attributes: ", msgparts.keys()
        #print "Subject: {} on {} ".format(msgparts['subject'], msgparts['date'])
        

        for part in msgparts.walk():
            #print "Part context type: ", part.get_content_type()
            if part.get_content_type().startswith("text"):
                body=part.get_payload(decode=True)
                #print "text/plain body = >{}<".format(body)
                result = getPhoneNumbers(body)
                for elem in result:
                    utel.add(elem)
    print utel
        
        
def getPhoneNumbers(body):
    phonepat = '\(?(\d{3})\)?[ -]*(\d{3})[ -]*(\d{4})'
    prog= re.compile(phonepat)
    result=prog.findall(body)
    return result
    
    
        
        
        
utel=set()
                
    #Homework search through the email body's to search for phone numbers   
    
    
##    
if __name__ == "__main__":
    pwd= open("C:\Users\Shaunak\Documents\Python Snakes\pass.txt","r").read()
    password = "".join([chr(ord(c)-2) for c in pwd])

getEmailData(password)
    

    
    
#   
#    #to encrypt
#pwd=""
#epwd="ugetgv"
#for letter in epwd:
#    print "letter = {}, ord = {}, new ord {}, new char={}".format(letter, ord(letter), ord(letter)-2, chr(ord(letter)-2))
#    pwd=pwd+chr(ord(letter)-2)
#print pwd
#[chr(ord(c)-2) for c in "ugetgv"] #List generator
#(chr(ord(c)-2) for c in "ugetgv") #Generator expression creates an object

#Homework make a pasword encrypter that is circular and can go backwards too

#join([chr(ord(d[i])^ord(k[i])) for i in range(len(d))])

#set it to a variable and then switch the variable with the d(data) to get the password back

# get k (key) from user
# repeat it to match length of d = rk
rk = k*(len(d)/len(k))+k[:(len(d)%len(k))] 
# key length = password length
# look at and understand  different parts of this expression
# may be just print different parts first with different values of d & k
# use rk for encode & decode
 
# encode – use once and save e to file (write file using program
e = "".join([chr(ord(d[i])^ord(rk[i])) for i in range(len(d))])
#Save e to file
 
# decode
# read e from file
# get k (key) from user – repeat it to length of e = rk
p = "".join([chr(ord(e[i])^ord(rk[i])) for i in range(len(e))])
# Use p as password


#x=raw_input("Insert Password: ")
#code=
