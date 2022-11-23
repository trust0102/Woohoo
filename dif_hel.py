def sender(send_pp,rcv_sk,p):
	return send_pp ** rcv_sk % p 

def receiver(rcv_pp,send_sk,p):
	return rcv_pp** send_sk % p
	
	
def main():
	p = int(input("Enter the prime number: "))
	g = int(input("Enter the generator: "))
	
	send_sk = int(input("Enter Alice Secret Key: "))
	rcv_sk = int(input("Enter Bob secret Key: "))
	
	send_pp = g ** send_sk % p
	rcv_pp = g ** rcv_sk % p
	
	print("Bob Common Key :", sender(send_pp,rcv_sk,p))
	print("Alice Common Key : ", receiver(rcv_pp,send_sk,p))
	
main()
