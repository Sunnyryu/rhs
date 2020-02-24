## Django Rest framework

#### Automation 

```

Django REST Swagger 

자동으로 API 목록과 각 API의 Request Body, Query Parameter를 문서화해주며,
바로 Postman과 같이 API를 테스트해 볼 수 있는, 많은 프로젝트에서 사용하는 검증된 문서화 도구

단점 
response schema를 제공하지 않음
Field-level documentation이 어려움
Response의 Object를 판별하기 어려움

API BLueprint
유연하고 깔끔한 마크다운 기반 Web API language. HTTP Testing Framework 인 Dredd를 사용하여 Auto Testing 이 가능
직접 문서 유지보수를 해야함 ..

RAML
YAML 문법과 유사한 RAML 언어를 사용, Atom 기반으로 Workbench를 제공합니다. 
직접 문서 유지보수

drf-yasg
 DRF용 문서 자동화 라이브러리 

 nested serializer와 schema 대응
 response schema 및 field-level description 가능
 swagger-spec-validator 혹은 flex로 schema validation 가능
 Versioning 가능
 Swagger-UI / Redoc 활용 가능

pip install -U drf-yasg
settings.py에 installed_apps에 drf_yasg 추가 

https://github.com/axnsan12/drf-yasg#id6 참조 



```
