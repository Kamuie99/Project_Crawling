## 프로젝트 배경

- 친구들끼리 같이 먹을 음식을 주문하기로 했다.
    - 갑자기 궁금해졌다.
    - 사람들이 깐풍기를 더 선호할까? 탕수육을 더 선호할까?

- 구글에 검색해보고 어떤 메뉴가 더 많이 검색되는 지로 판별해보고자 한다.

- **사람이 검색하는 것처럼 파이썬이 자동으로 검색 후 결과를 수집**하는 방법
    - 이러한 기술을 **크롤링(Crawling)**이라고 한다.
    - 이번 프로젝트에서 사용할 기술이다.

- 웹 크롤링 프로세스
    - 웹 페이지 다운로드
    - 페이지 파싱
    - 링크 추출 및 다른 페이지 탐색
    - 데이터 추출 및 저장

- 구글 웹사이트 활용하여 검색 후 해당 데이터를 수집하여 그래프로 시각화 해보기

[Google](https://www.google.com/)

## 공통 요구 사항

- 구글 검색 엔진을 활용하여 검색 결과에 따른 트렌드 분석 애플리케이션을 구현합니다.
    - 검색 결과 페이지의 ‘검색결과 개수’를 활용

- 다른 파일 템플릿 경로로 이동할 수 있는 링크들을 출력합니다.

- 검색하고자 하는 키워드를 추가 및 삭제할 수 있도록 구성합니다.

- 생성하기 및 삭제하기 버튼을 통해, Keyword 테이블에 데이터를 저장 및 삭제 하도록 구성

- Keyword 테이블에 저장된 키워드들을 활용하여 크롬검색 결과페이지 크롤링을 수행

- 저장시 이미 저장되어 있는 키워드라면, 새로 생성하지 않고 검색결과 개수를 변경

- 전체기간 검색결과를 이용하여 막대그래프를 출력

- 검색결과 페이지중 “지난1년” 을 기준으로 필터링하여 크롤링을 수행 후 그래프 출력

## 프로젝트 소감

1. 검색 엔진에서 자동으로 추가된 키워드 값을 기반으로 검색결과를 가져오는 과정이 신기했습니다. 그 중 평소 프론트엔드 개발 공부에 매진 중인 제게 **html의 class와 id 속성**을 이용하여 google이라는 웹 사이트의 결과 값을 **django가 가져올 수 있다**는 것이 인상깊었습니다.
   
2. 검색을 하고 그 검색 결과를 가져오는 과정에서 생각보다 **로딩 시간이 길었는데** 그 로딩 시간을 줄이는 방법은 없을까 고민하게 되었습니다.
   
3. 만일 로딩 시간을 줄일 수 없다면 해당 페이지 내에서 검색을 수행하고 있고, 결과를 기다리고 있다는 **사실을 알려줄 필요가 있지 않을까** 생각해 보았습니다. 성격이 급한 사람은 새로고침이나 앱을 나가는 방법을 택할 것 같아 정상적인 구동상황에서도 불편할 것 같아 **사용자 경험 관점**에서 **좋지 못한 서비스**가 된 것 같아서 아쉬웠습니다.

4. 추후 검색 결과의 많고 적음을 활용하여 인기를 구별하는 방법 외에도 **또 다른 방법**으로 이와 같은 크롤링을 활용하여 신뢰도 높은 정보를 제공한다면 **더 좋은 사용자 경험**을 선사해 줄 수 있는 프로그램 개발이 될 것 같습니다. **단순히 검색 결과가 많다고** 인기가 있다고 생각하지는 않기 때문입니다.

5. 가끔 오류나 문제가 발생했을 때 덜컥 겁을 먹는 경향이 있는데, 이 때 **코드를 진중하게** 다시 읽어보는 것만으로도 **대부분의 문제를 해결**할 수 있다는 것을 다시 한 번 깨닫게 되었습니다. chat-gpt를 이용할 때도 이용하는 방법에 따라 **성능에 큰 차이**가 나는 것 역시 확인할 수 있었습니다.

6. 저번 프로젝트와는 다르게 이번 프로젝트 중에는 **팀원과 조화롭게 협업이 이루어지지 못한 것** 같습니다. 그 이유로는 **둘다 모르는 부분**이 나왔을 때의 대처법과 **시간을 좀 더 효율적으로 활용**하지 못한 점이 아쉬운 것 같습니다. 컴퓨터 두대로 필요할 때마다 **파일을 주고받는 방법**은 확실히 합리적이지 못한 것 같아서, 다음주에 진행 될 **branch, merge** 특강을 통해 **협업 능력을 강화**해야 할 필요성을 느꼈습니다.
