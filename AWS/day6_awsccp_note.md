# AWS CCP 내용 정리 - Auto Scaling, Route 53, Elastic Beanstalk, Cloudformation

----------------------------------------

## Auto Scaling

 1. Create a Launch Configuration
 2. Assign the launch configuration to an auto scaling group
 
## Route 53 - register Domain

DNS 관리
트래픽 관리
가용성 모니터링
도메인 등록

### Route 53 exam tips

1. Amazon DNS의 이름은 Route 53
2. IAM 및 S3와 유사한 글로벌 제품
3. 이를 사용하여 전 세계의 트래픽을 유도하고 도메인 이름을 등록할 수 있음.

## Elastic Beanstalk

Elastic Beanstalk를 사용하면 애플리케이션을 실행하는 인프라에 대한 걱정 없이 AWS 클라우드에서 애플리케이션을 신속하게 구축하고 관리 및 배포할 수 있습니다.
애플리케이션을 업로드하기만 하면 Elastic Beanstalk는 용량 프로비저닝, 로드 밸런싱, 확장 및 애플리케이션 상태 모니터링에 대한 세부 정보를 처리합니다.
 
## Cloudformation

    1. AWS 리소스를 모델링하고 설정하여 리소스 관리 시간을 줄이고 애플리케이션에 더 많은 시간을 집중할 수 있도록 지원하는 서비스입니다.
    원하는 모든 AWS 리소스를 설명하는 템플릿을 생성합니다. 이는 EC2와 비슷하게 동작할 수 있습니다. RDS 인스턴스 등 AWS CloudFormation은 이러한 리소스의 프로비저닝 및 구성을 지원합니다.
    WordPress 사이트에서 수행한 것처럼 AWS 리소스를 개별적으로 생성 및 구성하여 무엇이 무엇에 종속되는지 파악할 필요가 없습니다. 

    2. Elastic Beanstalk와 CloudFormation은 모두 무료 서비스입니다. 하지만 이들이 프로비저닝하는 리소스 - EC2 인스턴스 또는 RDS 인스턴스... 등은 무료가 아닙니다. 따라서 서비스 자체는 무료이지만 프로비저닝하는 실제 리소스는 무료가 아닙니다.
    마지막으로, Elastic Beanstalk는 프로비저닝할 수 있는 것이 제한되어 있고 프로그래밍할 수 없는 반면 CloudFormation은 거의 모든 것을 프로그래밍하며 프로비저닝할 수 있습니다.
