print " lets get started! "
spy_name= raw_input("provide your name here :")
# check wether spy has input something or not
if len(spy_name) > 0 :
     #code block if condition is true.
     #concatination  of salutation and name.
     spy_age =0
     spy_rating=0.0
     spy_is_online= False
     spy_slautation = raw_input("what should we call you ?")
     spy_age = raw_input("enter your age.?")
     print ( spy_age )
     spy_name = spy_slautation + " " + spy_name
     print 'welcome' + spy_name + "glad to have you back with us "
     print "Alright" +spy_name + "i would like to know little bit more before you proceed further"
else:
     print "invalid name. Try again"
