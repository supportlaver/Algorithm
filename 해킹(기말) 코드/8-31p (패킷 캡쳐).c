#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/ip.h>
int main()
{
    int PACKET_LEN = 512;
    char buffer[PACKET_LEN] struct sockaddr saddr;
    struct packet_mreq mr;

    // htons(ETH_P_ALL) : 이 소켓은 모든 이더넷 프레임을 수신하도록 설정
    int sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));

    // PACKET_MR_PROMISC : 프로미스큐어스 모드로 설정
    mr.mr_type = PACKET_MR_PROMISC;
    // setsockopt : 해당 함수로 프로미스큐어스 모드를 활성화
    // SOL_PACKET 은 소켓 옵션의 레벨
    // PACKET_ADD_MEMBERHIP 은 프로미스큐어스 모드를 활성화 하기 위해서는
    // 멤버십을 추가해야 한다.
    // 결론적으로 프로미스큐어스 모드로 설정해서 모든 패킷을 수락하도록 하는 것
    setsockopt(sock, SOL_PACKET, PACKET_ADD_MEMBERSHIP, &mr, sizeof(mr));

    // 무한 루프를 통해 raw 소켓에서 패킷을 수신
    while (1)
    {
        // recvfrom 함수로 소켓에서 데이터를 수신
        int data_size = revfrom(sock, buffer, PACKET_LEN, 0, &saddr, (socklen_t *)sizeof(saddr));
        if (data_size)
            print("Got one packet\n");
    }
    close(sock);
    return 0
}