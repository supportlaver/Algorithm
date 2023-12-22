// 이 함수는 주어진 IP 헤더를 사용하여 소스 IP 주소를 조작하고
// 원시 IP 패킷을 생성하여 목적지 주소로 전송하는 역할을 한다.
// 이러한 기능이 바로 패킷 스푸핑
void send_raw_ip_packet(struct ipheader* ip)
{
    struct sockaddr_in dest_info;
    int enable = 1;

    // 소켓 생성
    // IPPROTO_RAW 는 패킷에 사용되는 프로토콜을 직접 지정 한 것
    // 즉 이 패킷에는 내가 직접 IP 헤더를 추가할테니까
    // 그것을 그대로 사용해 라는 것
    int sock = socket(AF_INET , SOCK_RAW , IPPORTO_RAW);

    // IP_HDRINCL : 소켓 옵션으로 사용자가 직접 IP 헤더를 지정한다는 것
    // &enable : 소켓 옵션의 값으로 1 로 설정하면 IP 헤더를 포함한 패킷을 전송
    setsockopt(sock, IPPROTO_IP, IP_HDRINCL, &enable , sizeof(enable));

    // 목적지 정보 설정
    dest_info.sin_family = AF_INET;
    dset_info.sin_addr = ip->iph_estip;

    printf("Sending spoofed IP packet...\n");

    // sendto 로 소켓을 통해 패킷을 전송
    // ip : 전달된 IP 헤더를 포함한 패킷 데이터
    // ntohs : IP 헤더의 길이를 네트워크 바이트 순서로 변환하여 전체 패킷의 길이로 사용
    if (sendto(sock, ip, ntohs(ip->iph_len),0
        (struct sockaddr *)&dest_info , sizeof(dest_info))<0){
            perror("PACKET NOT SENT");
            return;
        }
    close(sock)
}