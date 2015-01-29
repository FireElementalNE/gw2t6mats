import sys
import urllib
import json

def checkBounds(passedArg):
	if int(passedArg) > 250 or int(passedArg) < 0:
		return False
	return True

def priceFormat(price):
	gold=0
	silver=0
	if price >= 10000:
		gold = price / 10000
		price = price % 10000
	if price >= 100:
		silver=price / 100
		price = price % 100
	copper=price
	return '%sG %sS %sC' % (gold,silver,copper)

def prettyPrint(material,matText,amount_left):
	newTotal = 0
	for lineItem in material['sells']:
		newPrice = None
		quantity = lineItem['quantity']
		if quantity >= amount_left:
			basePrice = lineItem['unit_price']
			newPrice = amount_left * lineItem['unit_price']
			newTotal += newPrice
			print '%d %s: %s @ %s each' % (amount_left,matText,priceFormat(newPrice),priceFormat(basePrice))
			break
		else:
			basePrice = lineItem['unit_price']
			amount_left = amount_left - quantity
			newPrice = quantity * lineItem['unit_price']
			newTotal += newPrice
			print '%d %s: %s @ %s each' % (quantity,matText,priceFormat(newPrice),priceFormat(basePrice))
	return newTotal

try:
	scales_num = sys.argv[1]
	fang_num = sys.argv[2]
	claw_num = sys.argv[3]
	blood_num = sys.argv[4]
	dust_num = sys.argv[5]
	bone_num = sys.argv[6]
	venom_num = sys.argv[7]
	totem_num = sys.argv[8]
	check1 = checkBounds(scales_num) and checkBounds(fang_num) and checkBounds(claw_num) and checkBounds(blood_num)
	check2 = checkBounds(dust_num) and checkBounds(bone_num) and checkBounds(venom_num) and checkBounds(totem_num)
	check3 = check1 and check2
	if not check3:
		print 'Invalid Bounds'
		sys.exit(0)
except IndexError:
	print 'Inputs are the number of the mat that you HAVE not that you have left.'
	print 'Usage: %s <scales> <fangs> <claws> <blood> <dust> <bone> <venom> <totem>' % (sys.argv[0])
	sys.exit(0)

scales_id = '24289'
fang_id = '24357'
claw_id = '24351'
blood_id = '24295'
dust_id = '24277'
bone_id = '24358'
venom_id = '24283'
totem_id = '24300'

scales_left = 250 - int(sys.argv[1])
fang_left = 250 - int(sys.argv[2])
claw_left = 250 - int(sys.argv[3])
blood_left = 250 - int(sys.argv[4])
dust_left = 250 - int(sys.argv[5])
bone_left = 250 - int(sys.argv[6])
venom_left = 250 - int(sys.argv[7])
totem_left = 250 - int(sys.argv[8])

url = 'http://api.guildwars2.com/v2/commerce/listings?ids=%s,%s,%s,%s,%s,%s,%s,%s' % (scales_id,fang_id,claw_id,blood_id,dust_id,bone_id,venom_id,totem_id)

content = json.loads(urllib.urlopen(url).read())

totalAmount = 0
for material in content:
	id1 = str(material['id'])
	if id1 == scales_id:
		totalAmount += prettyPrint(material,"Scale: ",scales_left)
	elif id1 == fang_id:
		totalAmount += prettyPrint(material,"Fangs: ",fang_left)
	elif id1 == claw_id:
		totalAmount += prettyPrint(material,"Claws: ",claw_left)
	elif id1 == blood_id:
		totalAmount += prettyPrint(material,"Blood: ",blood_left)
	elif id1 == dust_id:
		totalAmount += prettyPrint(material,"Dust: ",dust_left)
	elif id1 == bone_id:
		totalAmount += prettyPrint(material,"Bones: ",bone_left)
	elif id1 == venom_id:
		totalAmount += prettyPrint(material,"Venom Sacs: ",venom_left)
	elif id1 == totem_id:
		totalAmount += prettyPrint(material,"Totems: ",totem_left)
	
print '--------------------------------'
print 'Total: %s' % (priceFormat(totalAmount))
