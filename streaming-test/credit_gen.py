import time, datetime, os, sys, random

HOME_PATH = "."
filename = "credit_gen.log"
debug = False

# Check for arguments
for arg in sys.argv:
	if (arg == "--debug"):
		debug = True

	if (arg.isdigit()):
		filename = str.replace(filename, ".log", "_" + str(arg) + ".log")

# Kill file if it exists.
if(debug == False):
	theFile = open(HOME_PATH +  '/' + filename, 'w')

# Neverending Loop
loop = 1
count = 1000000

fraudData = ""
fraudExist = False
fraudMs = 0
fraudShow = 0

while loop :
	if (count == 9999999):
		count = 1000000

	count = count + 1
	
	# Append to file
	theFile = open(HOME_PATH +  '/' + filename, 'a')
	
	# Define Data
	randMs = random.randint(1, 100) + 100	
	currentTime = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S.') + str(randMs)
	currentMs = int(round(time.time() * 1000))

	transactionTypes = ["P", "P", "P", "P", "P", "P", "P", "P", "P", "R"]
	transactionType = transactionTypes[random.randint(0, len(transactionTypes) - 1)]

	LocationX = str(random.randint(33,38))
	LocationY = str(random.randint(124,132))

	cardNum1 = random.randint(1000, 9999)
	cardNum2 = random.randint(1000, 9999)
	cardNum3 = random.randint(1000, 9999)
	cardNum4 = random.randint(1000, 9999)
	cardNumber = str(cardNum1) + "-" + str(cardNum2) + "-" + str(cardNum3) + "-" + str(cardNum4)

	cardOwner = "USER_" + str(random.randint(100, 999))

	expireDate = str(random.randint(2018, 2020)) + "/" + str(random.randint(1, 12)) + "/" + str(random.randint(1, 28))

	amount = str(random.randint(10, 1000) * 100)

	merchant = "MERCHANT_" + str(random.randint(100, 999))
	
	line = currentTime + ",TR" + str(count) + "," + transactionType + "," + cardNumber + "," + cardOwner + "," + expireDate + "," + amount + "," + merchant + "," + LocationX + "," + LocationY + "\n"

	if(random.randint(1, 50) == 50 and transactionType == "P"):
		if(fraudExist == False):
			print("Fraud Preparing...")
			fraudExist = True
			fraudMs = int(round(time.time() * 1000))
			fraudShow = random.randint(30000,50000)
			amount = str(random.randint(1000, 10000) * 100)
			merchant = "MERCHANT_" + str(random.randint(100, 999))
			LocationX = str(random.randint(54,69))
			LocationY = str(random.randint(151,164))
			fraudData = transactionType + "," + cardNumber + "," + cardOwner + "," + expireDate + "," + amount + "," + merchant + "," + LocationX + "," + LocationY + "\n"

	if(fraudExist):
		if(currentMs - fraudMs > fraudShow):
			print("Fraud Detection!")
			fraudExist = False
			fraudMs = 0
			count = count + 1
			line = line + currentTime + ",TR" + str(count) + "," + fraudData

	if(debug):
		print(line),
	else:
		theFile.write(line)
	
	time.sleep(random.random() * 2)
	
	# This ensures proper line breaking for solid tailing 
	theFile.close()
