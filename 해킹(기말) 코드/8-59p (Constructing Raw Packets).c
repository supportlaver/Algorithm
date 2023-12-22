
// buffer : 패킷 데이터를 저장하는 문자열
// memset : buffer 를 0 으로 초기화 , 즉 버퍼를 모두 0 으로 채운다는 것
char buffer[PACKET_LEN];
memset(buffer , 0 , PACKET_LEN);

// IP 헤더와 UDP 헤더를 설정
// ip : 패킷의 시작 위치에서부터의 주소를 가리키는 구조체 포인터로, IP 헤더를 나타낸다.
// udp : 패킷의 시작 위치에서부터 IP 헤더 다음 위치에서부터의 주소를 가리키느ㅡㄴ 구조체
struct ipheader *ip = (struct ipheader*) buffer;
struct udpheader *udp = (struct udpheader*) (buffer + sizeof(struct ipheader));

// 데이터 부분 설정
// data : 패킷에서 실제 데이터가 시작하는 위치를 가리키는 포인터
// msg : 전송하고자 하는 메시지를 나타낸 것
// data_len : 메시지의 길이
// strncpy : 이 메시지를 data 에 복사하고, 이 함수는 지정된 길이만큼의 문자를 복사
char *data = buffer + sizeof(struct ipheader) + sizeof(struct udpheader);
char *msg = "Hello Server.\n";
int data_len = strlen(msg);
strncpy(data, msg,data_len);

// UDP 헤더 필드 설정
// dprot : 목적지 포트 설정
// sport : 소스 포트 설정
// ulen : UDP 헤더와 데이터를 포함한 전체 길이를 설정
// sum : 체크섬 필드를 0
udp->udp_dport = htons(DST_PORT);
udp->udp_sport = htons(9999);
udp->udp_ulen = htons(sizeof(struct udpheader) + data_len);
udp->udp_sum = 0;

// ver : IP 버전을 나타내는 것
// ihl : IP 헤더의 길이
// sourceip.s_addr : 소스 IP 주소를 설정 , 
// inet_addr 함수를 사용하여 문자열 형태의 IP 주소를 32-bit 이진수로 변환

// destip.s_addr : 목적지 IP 주소 설정
// protocol : 전송 계층 프로토콜을 나타내는 필드 (여기서는 UDP 를 의미하는 것을 설정)
// len : IP 헤더와 포함된 데이터의 전체 길이를 나타내는 필드
// chksum : IP 헤더의 체크섬 필드를 0
ip->iph_ver = 4;
ip->iph_ihl = 5;
ip->iph_sourceip.s_addr = inet_addr(SRC_IP);
ip->iph_destip.s_addr = inet_addr(DEST_IP);
ip->iph_protocol = IPPORTO_UDP;
ip->iph_len = htons(sizeof(struct ipheader) + sizeof(struct udpheader) + data_len);
ip->iph_chksum = 0;

// 이전에 생성했던 함수를 실행
send_raw_ip_packet(ip);