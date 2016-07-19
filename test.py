import smbus
import time
bus = smbus.SMBus(1)
bus.write_byte_data(0x68, 0x6B, 0)
listex = []
listey = []
while True:
	x = bus.read_byte_data(0x68, 0x3B)
	y = bus.read_byte_data(0x68, 0x3D)
	c = bus.read_byte_data(0x68, 0x3F)
	if x > 127:
		x -= 256
	if y > 127:
		y -= 256
	if len(listex) <= 4:
		listex.append(x)
		listey.append(y)
	else:
		xx = (listex[0]+listex[1]+listex[2]+listex[3])/4
		yy = (listey[0]+listey[1]+listey[2]+listey[3])/4
		listex.append(x)
		listey.append(y)
		del listex[0]
		del listey[0]
		x = xx
		y = yy
	print("x:", x, "y:", y, "z:", c)
	time.sleep(0.1)