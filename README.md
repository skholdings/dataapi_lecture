# Data API 실습

- HDP 샌드박스 설치 : 2.6.3

> https://downloads-hortonworks.akamaized.net/sandbox-hdp-2.6.3/HDP_2.6.3_virtualbox_16_11_2017.ova

<br>

- root 패스워드 변경 : hadoop(초기 패스워드) -> bigdata1234

<br>

- HDFS 계정으로 전환 : su - hdfs

<br>

- Data API 모듈 설치 : API Gateway, Streaming, Batch, Common, SSO, OAuth

> git clone https://github.com/skholdings/api-modules.git

<br>

- DB(MariaDB) 접속 : root / hadoop

<br>

- 데이터베이스 및 테이블 생성 : streaming, batch, sso

<br>

- API사용자 및 scope 추가

> 로그인 서버 (SSO, OAuth) 기동 : http://localhost:8091/admin

> ID / Password : skcc / skcc1234

> Scope : core:all

<br>

- Streaming 엔진 HDFS에 업로드

> hadoop fs -put -f streaming-core-1.0-hdp263.jar /user/spark/streaming/driver/

> hadoop fs -put -f phoenix-spark2-4.7.1-HBase1.1.jar /user/spark/streaming/lib/

> hadoop fs -put -f mariadb-java-client-2.0.2.jar /user/spark/streaming/lib/

<br>

- livy CR/LF 프로텍션 비활성화

> Ambari 로그인 : raj_ops / raj_ops

<br>

- API 모듈 기동

> API Gateway 기동

> Streaming API 모듈 기동

> Batch API 모듈 기동

> Common API 모듈 기동

<br>

- API 테스트

> 툴 다운로드 : https://install.advancedrestclient.com/#/install

> http://localhost:8765/api/v1/streaming

> 로그인 서버로부터 Access Token 획득

> Authorization 헤더에 Access Token 입력(Bearer xxxxx...) 후 API 호출

<br>

- Kafka 기동 및 데이터 생성

> python credit_gen.py

> tail -f credit_gen.log | /usr/hdp/current/kafka-broker/bin/kafka-console-producer.sh --topic credit --broker-list sandbox-hdp.hortonworks.com:6667
