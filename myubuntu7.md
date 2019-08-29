## My Ubuntu

#### Ubuntu 7

```
메일 서버

이메일 송수신에 사용되는 프로토콜은 3가지
SMTP (Simple Mail Transfer Protocol) : 클라이언트가 메일을 보내거나 메일 서버끼리 메일을 주고 받을 때 사용
POP3(Post Offilce Protocol): 클라이언트가 메일을 보내거나, 메일 서버끼리 메일을 주고 받을 때 사용
imap(Internet Mail Access Protocol) : POP3와 용도가 같음

예를 들어서 sunny가 ryu에게 메일을 주고 받는 과정이라면
sunny의 pc에서 메일 클라이언트 프로그램(ex: outlook) 등을 실행해서 live.com에 접속 - 편지 쓰기 - ryuryuryu1@live.com에게 메일을 쓴다. (SMTP 프로토콜 이용)

메일 서버 1(live.com)은 sunny가 보낸 메일을 임시 장소에 잠시 보관하며, 메일 수신자의 메일 서버 ip 주소를 네임 서버에게 요청해서 알아옴

메일 서버1은 메일을 인터넷을 통해 메일 서버 2에게 전송 (SMTP 사용 )
메일 서버(수신자)는 메일 서버(발신자)로부터 받은 메일의 수신자 이름을 확인하고 서버가 관리하는 계정인지 확인한다. 있다면 메일 박스에 넣어둠

ryu는 자신의 pc에서 메일 클라이언트 프로그램을 실행해서 서버에 접속하여 메일을 pc2로 보냄 (POP3/ IMAP 프로토콜 사용)

샌드 메일 서버

메일 클라이언트(MUA) - SMTP - 샌드메일(MTA) - 메일 큐 - MDA - SMTP - 인터넷 - SMTP - 샌드메일 - MDA - 메일박스 - (메일클라이언트 2가 dovecot(MRA)에 먼저 메일을 달라고 요청함) - 메일박스가 dovecot에 메일이 있다면 줌 - POP3, IMAP 방식으로  보내줌

(MTA : Mail Transfer Agent, MUA : Mail User Agent, MDA : Mail Delivery Agent, MRA : Mail Retrieval Agent)

구현

네임 서버를 구현한 후에 메일 서버를 구현한다.

```
