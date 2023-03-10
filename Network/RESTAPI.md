# API란 무엇일까요?

개발을 하며 여러 API를 사용하지만, 마음으로는 알겠으나 설명하라면 정확하게 설명할 수 없었기에

API의 개념에 대해 짧게 정리를 해볼까 합니다.  
<br/>

API란 Application Programming Interface의 약자로,

프로그래밍 언어의 기능을 제어하고 어플리케이션에서 상호작용할 수 있도록 만든 인터페이스입니다.

즉, "클라이언트와 리소스 사이의 게이트웨이"와 같은 느낌입니다.

이때 클라이언트는 웹에서 정보에 접근하려는 사용자이고,

리소스는 이미지, 텍스트를 포함한 모든 유형의 데이터를 의미합니다.

API를 통해서 클라이언트에게 리소스를 공유하고 보안, 인증 등을 유지한 채 웹 서비스를 제공할 수 있습니다.  
<br/>

정보를 찾던 도중 찰떡인 비유가 있었습니다. 일련의 개발 과정을 레스토랑으로 비유한 것인데,

테이블(프론트엔드)에서 주문을 하면 식당(백엔드)에서 주문받은 것을 요리하여 제공할 것입니다.

이 때 테이블에서 식당까지 연결해주는 사람이 바로 웨이터(API)인 것입니다.

손님은 주방에서 벌어지는 일을 모두 알진 않지만,

주문한 것(request)에 대해 재료가 없다-는 등의 응답(response)는 들어야합니다.  
<br/>


채용 공고에서 흔히 볼 수 있는 "백엔드 API 시스템(혹은 서버) 개발을 한다"는 말의 의미는

해당 서비스에 필요한 백엔드 기능을 API 형태, 즉 URI를 통한 HTTP 프로토콜로 통신할 수 있는

인터페이스 형태로써 개발을 진행한다는 의미입니다.   
<br/>


이러한 웹개발을 진행하다 보면 RESTful API(REST API)라 불리는 것을 많이 봐왔을 것입니다.

(REST 아키텍처를 이루는 웹서비스를 RESTful API라 하기에, 사실상 같은 의미로 보아도 될 것 같습니다.)  
<br/>


### 그렇다면 REST API란 무엇일까요?

REST는 Representational State Transfer의 약자로,

번역하여 이해하자면 이름으로써(Representational) 상태를(State) 주고받는 것(Transfer)이라 생각하면 편합니다.

Client와 Server 사이의 통신 방식 중 하나로, URI(Uniform Resource Identifier, URL의 상위 개념)로 POST, GET, PUT, DELETE 및 HTTP 헤더와 같은 HTTP Method를 통해 요청을 보내고, JSON을 통해 표현되어 데이터를 주고 받게 됩니다.  
<br/>

### 이때 REST API의 작동 순서는

1. 클라이언트가 API 문서에 따라 서버에 요청을 전송하면,

2. 서버가 클라이언트를 인증하고 권한이 있는지를 확인하고

3. 서버가 요청을 수신하고 내부적으로 처리한 뒤

4. 서버가 클라이언트에 요청이 성공했는지의 응답과, 클라이언트가 요청한 정보 응답을 반환합니다.  
<br/>


### 여기서 요청이 성공했는지의 서버 응답의 종류로

- 1XX : 전송 프로토콜 수준의 정보 교환

- 2XX : 클라이언트 요청이 성공적으로 수행됨

- 3XX : 클라이언트는 요청을 완료하기 위해 추가적인 행동을 취해야 함

- 4XX : 클라이언트의 잘못된 요청

- 5XX : 서버쪽 오류로 인한 상태코드

가 있습니다.  
<br/>


### REST 아키텍처 스타일에는 몇가지 원칙이 있습니다.


1. Stateless 프로토콜

Client Server 모델을 따르는 REST 아키텍처는 Stateless합니다.

즉, 무상태함을 유지하며 필요에 따라 클라이언트와 서버가 상호작용을 하게 됩니다.   
<br/>


2. 캐시 가능성

REST 웹서비스는 서버 응답 시간 개선을 위해 클라이언트에게 응답을 저장하는 프로세스인 캐싱을 지원합니다.

즉, 서비스의 요청 결과가 Caching되어 효율적으로 서비스를 사용하고 재사용할 수 있습니다.  

<br/>

3. 계층화

REST한 웹서비스는 시스템을 계층화하기 쉽습니다.

API 서버에 보안, 로드밸런싱, 암호화등을 계층에 추가하여 유연한 구성이 가능합니다.  

<br/>

4. Code on demand

프로그램 코드를 서버에서 다운받아 클라이언트에서 실행할 수 있습니다.

이를 통해 클라이언트를 차후에 확장하거나 사용자를 지정할 수 있습니다.  

<br/>

### 또한 REST API에는 아래와 같은 설계 규칙이 있습니다.

1. /는 계층 관계를 나타내는데 사용합니다.

2. URL 마지막 문자로 /를 포함하지 않습니다.

3. -은 URL 가독성을 높이는데 사용합니다.

4. _은 URL에 사용하지 않습니다.

5. URL 경로에는 소문자가 적합합니다.

6. 파일확장자는 URL에 포함하지 않습니다.

7. URL에 사용되는 영어를 복수형으로 작성합니다.   
<br/>


이렇게 설계된 RESTful API에서 요청을 보낼땐 인증(authentication)이 필요합니다.  
<br/>

### RESTful API의 인증 방법은 아래 네가지가 있습니다.



1. HTTP 인증 - 요청 헤더에 사용자 이름과 암호를 넣고 base64로 인코딩하여 전송하는 기본 인증

2. HTTP 인증2- 서버가 생성한 암호화된 문자열 토큰을 요청 헤더에 넣어 전송하는 전달자 인증

3. Oauth - 암호를 요청한 다음 추카 토큰을 요청하는 방식으로 암호와 토큰을 결합한 인증

4. API Key - 서버가 고유하게 생성된 값을 최초 클라이언트에 할당하여 인증  

<br/>

### 이같은 REST API는 AWS의 Amazon API Gateway를 사용하면 API 생성, 유지 관리, 모니터링을 쉽게 할 수 있습니다.


API Gateway를 등록하면 서비스의 엔드포인트 대신 API Gateway로 요청을 전달하여 엔드포인트 서버에서 필요한 인증, 사용량 제어, 요청/응답 변조등의 기능을 플러그인 형태로 사용하여 비용을 절감할 수 있습니다.

매달 100만건의 호출이 무료이고, 이를 초과하는 경우 비용이 청구됩니다.

AWS API Gateway의 경우 AWS Lambda와 연동하여 Serverless 서비스를 구축하는데 주로 사용됩니다!  
<br/>
