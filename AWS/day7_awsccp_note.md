# AWS CCP 내용 정리 - Exam Tips

----------------------------------------

##  Exam Tips: Which AWS Services are Global:
	1. IAM
	2. Route 53
	3. CloudFront
	4. SNS, is available in all regions
	5. SES, is not available in all regions

	Some services give global views but are regional
	1. S3 buckets

* What AWS Services Can Be Deployed On Premise
	1. SnowCone -  Disk that amazon send out to you, you load the data and then send it to amazon
	2. Snowball Edge - Similar to Snowball plus CPU. Computer with storage, allows to deploy lambda functions on premise. Boeing uses this.
	3. Storage Gateway - Caching your files inside your data centre and replicate files to S3
	4. CodeDeploy - To deploy applications on premise
	5. Opsworks - Opsworks uses chef to do automated deployments.
	6. IoT Greengrass - AWS service, connect on premise devices to AWS cloud.
	7. Systems Manager
	
* CloudWatch 101
	1. CloudWatch is to monitor performance
	2. Monitors
		2.1 EC2 Instances
		2.2 Autoscaling Groups
		2.3 Elastic Load Balancers
		2.4 Route53 Health Checks
	3. Storage and Content Delivery
		3.1 EBS Volumes
		3.2 Storage Gateways
		3.3 CloudFront
	4. Monitors host level metrics such as CPU, Network, Status check and Disk

* CloudWatch 101 - Exam Tips:
	1. CloudWatch is used for monitoring performance.
	2. CloudWatch can monitor most of AWS as well as your applications that run on AWS
	3. CloudWatch with EC2 will monitor events every 5 mins by default.
	4. You can have 1 min interval by turning on detailed monitoring
	5. You can create CloudWatch alarms which trigger on detailed monitoring.
	6. CloudWatch is all about performance.

* AWS Systems Manager - Exam Tips
	1. Systems Manager is used to manage fleets of EC2 instances and virtual machines
	2. A piece of software installed on each VM
	3. Can be both inside AWS and on premise
	4. Run command is used to install, patch and uninstall software.
	5. Integrates with CloudWatch to give you a dashboard of your entire estate.