# Korg Monotribe wave -> firmware binary decoding application
# by th0mas aka gravitronic

# http://gravitronic.blogspot.com
# hit me up on twitter http://twitter.com/gravitronic

from struct import pack

def encode(short, long, skip, little, output):
   f = open("bits", "r")
   finished = ""
   i = 0
   f.seek(0)
   str=""

   print "%s: short %s, long %s, skip %d, little %d" % (output, short, long, skip, little)

   for i in range(skip):
      print "skipping a line"
      f.readline();

   for b in f.readlines():
       if b[0] == "0":
          if little == True:
             str = short + str
          else:
             str = str + short
       elif b[0] == "1":
          if little == True:
             str = long + str
          else:
             str = str + long

       i+=1
       if i == 8:
          finished += pack("B", int(str, 2))
          i = 0
          str = ""

   f = open(output, "w")
   f.write(finished)
   f.close()

#j = 0
#for i in range(8):
#   encode("0", "1", i, True, str(j)+".bin")
#   j+=1
#   encode("1", "0", i, True, str(j)+".bin")
#   j+=1
#   encode("0", "1", i, False, str(j)+".bin")
#   j+=1
#   encode("1", "0", i, False, str(j)+".bin")

# this works:
# 1.bin: short 1, long 0, skip 0, little 1

print "Monotribe firmware decoder by th0mas aka gravitronic"
print "http://twitter.com/gravitronic"
print "use at your own risk!"

encode("1", "0", 0, True, "firmware.bin")

