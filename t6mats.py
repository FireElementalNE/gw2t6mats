import sys
import urllib
import json


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

try:
	scales_num = sys.argv[1]
	fang_num = sys.argv[2]
	claw_num = sys.argv[3]
	blood_num = sys.argv[4]
	dust_num = sys.argv[5]
	bone_num = sys.argv[6]
	venom_num = sys.argv[7]
	totem_num = sys.argv[8]
except IndexError:
	print 'Inputs are the number of the mat that you HAVE not that you have left.'
	print 'Usage: %s <scales> <fangs> <claws> <blood> <dust> <bone> <venom> <totem>' % (sys.argv[0])
	sys.exit(0)

scales_id = '24284'
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
		newPrice = scales_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Scales: %s' % (scales_left,priceFormat(newPrice))
	elif id1 == fang_id:
		newPrice = fang_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Fangs: %s' % (fang_left,priceFormat(newPrice))
	elif id1 == claw_id:
		newPrice = claw_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Claws: %s' % (claw_left,priceFormat(newPrice))
	elif id1 == blood_id:
		newPrice = scales_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Blood: %s' % (blood_left,priceFormat(newPrice))
	elif id1 == dust_id:
		newPrice = scales_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Dust: %s' % (dust_left,priceFormat(newPrice))
	elif id1 == bone_id:
		newPrice = scales_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Bones: %s' % (bone_left,priceFormat(newPrice))
	elif id1 == venom_id:
		newPrice = venom_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Venom Sacs: %s' % (venom_left,priceFormat(newPrice))
	elif id1 == totem_id:
		newPrice = totem_left * material['sells'][0]['unit_price']
		totalAmount += newPrice
		print '%d Totems: %s' % (totem_left,priceFormat(newPrice))
	
print '--------------------------------'
print 'Total: %s' % (priceFormat(totalAmount))
