import sys
from g4f.client import Client

coll = 0

try:
	for i in sys.argv:
		if coll != 0:
			argv = sys.argv[coll]
		coll += 1
	coll = 0
	client = Client()
	response = client.chat.completions.create(
		model="gpt-3.5-turbo",
		messages=[{"role": "user", "content": argv }]
	)
	print(response.choices[0].message.content)
except:
	print("Введите prompt")
