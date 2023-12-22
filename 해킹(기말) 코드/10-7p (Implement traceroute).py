# ICMP 패킷의 TTL 값을 변화 시키면서 목적지로 가는 경로에 라우터들의 IP 주소를
# 탐색하는 코드

a = IP()
# 목적지 IP 주소 설정
a.dst = "93.184.216.34"
b = ICMP()

# TTL 값을 1 부터 19 까지 변경하면서 반복을 한다.
for TTL in range(1,20):
    a.ttl = TTL
    # srl 함수를 사용하여 ICMP 패킷을 전송하고 응답을 기다린다.
    # a/b 는 IP 패킷 (a) 에 ICMP 패킷(b) 를 내포시킨 형태이다.
    # timeout=2 는 응답을 기다리는 최대 시간을 설정한다.
    h = srl(a/b, timeout=2, verbose=0)
    
    # 응답이 없는 경우 즉 타임아웃이 발생한 경우
    if h is None:
        print("Router : *** (hops = {})".format(TTL))
    # 응답이 있는 경우  즉 목적지에 도달한 경우
    else:
        print("Router: {} (hops = {})".format(h.src,TTL))
    