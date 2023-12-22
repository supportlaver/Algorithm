int main()
{
    // 패킷 챕처에 사용되는 PCAP 핸들
    pacp_t *hadnle;
    // PCAP 에서 발생하는 오류 세미지를 저장할 버퍼
    char errbuf[PCAP_ERRBUF_SIZE];
    // 필터 프로그램을 저장할 구조체
    struct bpf_program fp;
    // 패킷을 필터링하기 위한 BPF 필터 표현식
    char filter_exp[] = "udp or icmp";
    // 현재 네트워크의 IP 주소를 저장할 변수
    bpf_u_int32 net;

    // 패킷 핸들 생성
    // enp0s3 가 캡처할 네트워크 인터페이스의 이름
    // 8192 는 캡처할 최대 바이트 수
    // 1 은 프로미스큐어스 모드 설정
    // 1000 은 타임아웃 설정
    // errbuf 는 오류 메시지를 저장할 버퍼
    handle = pcap_open_live("enp0s3", 8192, 1, 1000, errbuf);

    // 필터 표현식을 컴파일하여 필터 프로그램을 생성한다.
    // handl 은 위에서 만든 PCAP 핸들러
    // fp 는 필터 프로그램을 저장할 구조체
    // filter_exp 는 필터 표현식
    // 0 은 최적화 옵션으로 일반적으로 설정한다고 생각
    // net 은 현재 네트워크의 IP 주소
    pcap_complie(handle, &fp, filter_exp, 0, net);

    // setfilter 로 캡처한 패킷을 필터링하기 위해 필터 프로그램을 설정 (pcap 핸들에)
    // pcap_perror 은 오류 메시지를 출력
    // 오류가 발생한 경우 프로그램을 종료
    if (pcap_setfilter(handle, &fp) != 0)
    {
        pacap_perror(handle, "Error:");
        exit(EXIT_FAILURE);
    }

    // 캡처한 패킷을 루프로 처리
    // -1 은 무한 루프로 설정
    // get_packet 은 각 패킷을 처리할 사용자 정의 함수
    pcap_loop(handle, -1, get_packet, NULL);

    pcap_close(handle);
    return 0;
}