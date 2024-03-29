# AWS CCP 도메인

</br>

# 도메인 1: 클라우드 개념

</br>

#### 1.1 AWS 클라우드 및 그 가치 제안 정의

</br>

 다음을 포함하여 AWS 클라우드의 이점을 정의합니다.
o 보안
o 안정성
o 고가용성
o 탄력성
o 민첩성
o 사용한 만큼 지불하는 요금제
o 확장성
o 글로벌 도달 범위
o 규모의 경제

</br>

 AWS 클라우드를 통해 사용자가 비즈니스 가치에 집중할 수 있는 방법 설명
o 인프라 관리와 달리 기술 리소스를 수익 창출 활동으로 전환

</br>

#### 1.2 AWS 클라우드의 경제성 식별

</br>

 총 소유 비용 제안의 일부가 되는 품목 정의
o 운영 비용(OpEx)의 역할 이해
o 설비투자비용(CapEx)의 역할 이해
o 온프레미스 운영과 관련된 인건비 이해
o 클라우드로 전환할 때 소프트웨어 라이선스 비용이 미치는 영향 이해

</br>

 클라우드로 전환하여 운영 비용을 절감할 수 있는 부문 식별
o 적정 규모의 인프라
o 자동화의 이점
o 규정 준수 범위 축소(예: 보고)
o 관리형 서비스(예: RDS, ECS, EKS, DynamoDB)

</br>

#### 1.3 다양한 클라우드 아키텍처 설계 원칙 설명

</br>

 설계 원칙 설명
o 장애 대비 설계
o 구성 요소와 모놀리스 아키텍처 분리
o 클라우드와 온프레미스에서 탄력성 구현
o 병렬 사고

# 도메인 2: 보안 및 규정 준수

#### 2.1 AWS 공동 책임 모델 정의
 공동 책임 모델의 요소 인식
 AWS 에 대한 고객의 책임 설명
o 사용한 서비스(예: RDS, Lambda, EC2)에 따라 고객의 책임이 어떻게 달라질 수
있는지 설명
 AWS 책임 설명

</br>

#### 2.2 AWS 클라우드 보안 및 규정 준수 개념 정의
 AWS 규정 준수 정보를 찾을 수 있는 위치 식별
o 사용 가능한 공식 규정 준수 제어(예: HIPPA, SOC) 목록 위치
o AWS 서비스마다 규정 준수 요구 사항이 다르다는 점을 인식
 고객이 AWS 에서 규정 준수를 달성하는 방법을 개략적으로 설명
o AWS 에서 서로 다른 암호화 옵션 식별(예: 전송 중 데이터, 저장 데이터)
 특정 서비스에 대해 AWS 에서 암호화를 활성화하는 사용자 설명
 감사 및 보고에 도움이 되는 서비스가 있음을 인식
o 감사 및 모니터링을 위한 로그가 존재함을 인식(로그를 이해할 필요는 없음)
o Amazon CloudWatch, AWS Config 및 AWS CloudTrail 정의
 최소 권한 액세스의 개념 설명

</br>

#### 2.3 AWS 액세스 관리 기능 식별
 사용자 및 ID 관리의 목적 이해
o 액세스 키 및 암호 정책(교체, 복잡성)
o MFA(Multi-Factor Authentication)
o AWS IAM(Identity and Access Management)
• 그룹/사용자
• 역할
• 정책, 사용자 지정 정책 대비 관리형 정책
o 루트 계정을 사용해야 하는 태스크
루트 계정 보호

</br>

#### 2.4 보안 지원을 위한 리소스 식별
 서로 다른 네트워크 보안 기능이 있음을 인식
o 기본 AWS 서비스(예: 보안 그룹, 네트워크 ACL, AWS WAF)
o AWS Marketplace 의 서드 파티 보안 제품
 문서(예: 모범 사례, 백서, 공식 문서)가 있다는 점과 문서를 찾을 수 있는 위치를 인식
o AWS 지식 센터, 보안 센터, 보안 포럼 및 보안 블로그
o 파트너 시스템 통합 사업자
 보안 검사가 AWS Trusted Advisor 의 구성 요소임을 파악

</br>

# 도메인 3: 기술

</br>

#### 3.1 AWS 클라우드에서 배포 및 운영 방법 정의

</br>

 AWS 클라우드에서 다양한 프로비저닝 및 운영 방식을 개략적으로 식별
o 프로그래밍 방식 액세스, API, SDK, AWS Management Console, CLI, Infrastructure as Code(IaC)
 다양한 유형의 클라우드 배포 모델 식별
o 클라우드/클라우드 네이티브 사용
o 하이브리드
o 온프레미스
 연결 옵션 식별
o VPN
o AWS Direct Connect
o 퍼블릭 인터넷

</br>

#### 3.2 AWS 글로벌 인프라 정의

</br>

 리전, 가용 영역 및 엣지 로케이션의 관계 설명
 여러 가용 영역을 사용하여 고가용성을 달성하는 방법 설명
o 고가용성은 여러 가용 영역을 사용하여 달성된다는 점을 상기
o 가용 영역이 단일 장애 지점을 공유하지 않는다는 점을 인식
 여러 AWS 리전의 사용을 고려해야 할 시기 설명
o 재해 복구/비즈니스 연속성
o 최종 사용자를 위한 짧은 지연 시간
o 데이터 주권
 엣지 로케이션의 이점을 개략적으로 설명
o Amazon CloudFront
o AWS Global Accelerator

# 3.3 핵심 AWS 서비스 식별

</br>

 AWS 의 서비스 범주 설명(컴퓨팅, 스토리지, 네트워크, 데이터베이스)
 AWS 컴퓨팅 서비스 식별
o 서로 다른 컴퓨팅 제품군이 있음을 인식
o 컴퓨팅을 제공하는 다양한 서비스 인식(예: Amazon ECS(Amazon Elastic Container
Service) 대비 AWS Lambda, Amazon EC2 등)
o 탄력성은 Auto Scaling을 통해 실현됨을 인식
o 로드 밸런서의 목적 식별
 다른 AWS 스토리지 서비스 식별
o Amazon S3 설명
o Amazon EBS(Amazon Elastic Block Store) 설명
o Amazon S3 Glacier 설명
o AWS Snowball 설명
o Amazon EFS(Amazon Elastic File System) 설명
o AWS Storage Gateway 설명
 AWS 네트워킹 서비스 식별
o VPC 식별
o 보안 그룹 식별
o Amazon Route 53 의 목적 식별
o VPN, AWS Direct Connect 식별
 다른 AWS 데이터베이스 서비스 식별
o AWS 관리형 데이터베이스 대비 Amazon EC2 에 데이터베이스 설치
o Amazon RDS 식별
o Amazon DynamoDB 식별
o Amazon Redshift 식별

</br>

# 3.4 기술 지원을 위한 리소스 식별

</br>

 문서(모범 사례, 백서, AWS 지식 센터, 포럼, 블로그)가 있음을 인식
 AWS 지원의 다양한 수준과 범위 식별
o AWS 침해
o AWS 지원 사례
o Premium Support
o 기술 지원 관리자
 독립 소프트웨어 공급업체 및 시스템 통합 사업자를 포함한 파트너 네트워크(마켓플레이스,
서드 파티)가 있음을 인식
 전문 서비스, 솔루션 아키텍트, 교육 및 자격증, Amazon 파트너 네트워크를 비롯한 AWS
기술 지원 및 지식의 출처 식별
 AWS Trusted Advisor 사용의 이점 식별

# 도메인 4: 결제 및 요금제

</br>

#### 4.1 AWS 의 다양한 요금제(예: 온디맨드 인스턴스, 예약 인스턴스 및 스팟 인스턴스 요금제) 비교 및
대조
 온디맨드 인스턴스 요금제에 가장 적합한 시나리오 식별
 예약 인스턴스 요금제에 가장 적합한 시나리오 식별
o 예약 인스턴스 유연성 설명
o AWS 조직의 예약 인스턴스 동작 설명
 스팟 인스턴스 요금제에 가장 적합한 시나리오 식별

</br>

#### 4.2 AWS 결제 및 요금제와 관련된 다양한 계정 구조 인식
 통합 결제가 AWS Organizations 의 기능임을 인식
 여러 계정을 통해 부서 전체에 비용을 할당하는 방법 식별

</br>

#### 4.3 결제 지원에 사용할 수 있는 리소스 식별
 결제 지원 및 정보를 얻는 방법 식별
o 비용 탐색기, AWS 비용 및 사용 보고서, Amazon QuickSight, 서드 파티 파트너 및
AWS Marketplace 도구
o 결제 지원 케이스 열기
o AWS Enterprise Support 플랜 고객을 위한 컨시어지의 역할
 AWS 서비스에 대한 요금 정보를 찾을 수 있는 위치 식별
o AWS 월 사용량 계산기
o AWS 서비스 제품 페이지
o AWS 요금 API
 경보/경고가 존재함을 인식
 비용 할당에 태그가 사용되는 방식 식별