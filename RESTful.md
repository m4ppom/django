# RESTful

``` 
URI Uniform Resource Identifier 통합자원 식별자 인터넷에 있는 자원을 나타내는 주소
URL
```

``` 
GET https://localhost:8000/articles/1
HTTP VERB HOSTNAME		   Resource id
URI는 자원만을 표현한다.
HTTP VERB(method)로 자원을 조작
```

| HTTP method | URI         | Description       |
| ----------- | ----------- | ----------------- |
| GET         | /articles   | article목록       |
| GET         | /articles/1 | id=1 article 상세 |
| POST        | /articles   | article 생성      |
| PATCH       | /articles/1 | id=1 article수정  |
| DELETE      | /articles/1 | id=1 article삭제  |

