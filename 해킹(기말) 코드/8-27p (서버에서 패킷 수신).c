#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/ip.h>
void main()
{
    // 서버의 소켓 주소 정보를 저장하는 구조체
    struct sockaddr_in server;
    // 클라이언트의 소켓 주소 정보를 저장하는 구조체
    struct sockaddr_in client;
    // 클라이언트 주소 구조체의 크기를 나타내는 변수
    int clientlen;
    // 수신된 데이터를 저장하는 버퍼
    char buf[1500];

    // 소켓을 생성
    int sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);

    // 서버 주소 설정
    server.sin_family = AF_INET; // IPv4 주소 체계 사용
    // 모든 네트워크 인터페이스로부터의 패킷을 수락하도록 설정
    server.sin_addr.s_addr = htonl(INADDR_ANY);
    // 서버의 포트 번호를 9090 으로 설정
    server.sin_port = htons(9090);

    // 소켓에 주소 정보를 할당하고 바인딩하는데, 바인딩에 실패하면 오류 메시지를 출력
    if (bind(sock, (struct sockaddr *)&server, sizeof(server)) < 0)
        error("ERROR on binding");

    // 무한 루프를 돌면서 클라이언트로부터 데이터를 수신하고 출력
    while (1)
    {
        // 버퍼를 초기화
        bzero(buf, 1550);
        // 클라이언트로부터 데이터를 수신
        // 1500 - 1 : 세번째 매개변수는 수신할 데이터의 최대 크기를 나타낸다.
        // 이 크기보다 더 큰 데이터가 수신되면 잘라내거나 버리게 되는데,
        // 1500-1 은 전형적인 MTU 크기에서 1바이트를 뺀 값을 사용하는 것이다.
        // 이더넷에서는 최대 패킷 크기가 일반적으로 1500 바이트인데 여기서
        // -1 을 뺀 이유는 문자열에서 null 종결 문자를 고려하기 위해서이다.
        recvfrom(sock, buf, 1500 - 1, 0, (struct sockaddr *)&client, &clientlen);
        printf("%s\n", buf);
    }
    close(sock);
}