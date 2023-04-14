# React와 Next.js의 차이? / Next.js의 필요성

React와 Next.js의 차이


React는 Javascript 기반의 SPA 웹 프레임워크입니다. 컴포넌트를 활용하여 UI를 쉽고 효율적으로 만들 수 있습니다.

이 글에서 강조하고자 하는 내용은 리액트는 CSR(Client Side Rendering), 즉 화면을 그리는 렌더링이 클라이언트에게서 발생합니다. 서버에서 보내주는 HTML과 Javascript 파일을 서버가 아닌, 클라이언트의 브라우저에서 페이지를 만들어줍니다. 이러한 방식은 페이지 간 전환이 부드러워지는 장점이 있습니다. 하지만 HTML과 JS를 다운로드 받는동안 클라이언트는 렌더링이 불가능한, 즉 첫 페이지의 로딩속도가 느리다는 단점이 있습니다. 또한 CSR의 특성상 빈 HTML과 JS를 보낸 뒤 클라이언트의 브라우저에서 JS를 실행시켜 화면을 그리는데, 대부분의 검색 엔진은 HTML 파일만 크롤링합니다. 이것은 SEO(Search Engine Optimization)에 악영향을 끼쳐 구글과 같은 검색 사이트의 상위 노출에 불리해집니다. 이는 웹 비즈니스에 있어 매우 큰 단점으로 작용합니다.



이러한 단점들을 극복하기 위해 최근 들어 React Meta-Framework들이 나왔습니다.

대표적으로 Gatsby, Next.js, Remix 등이 있는데, 그중에서도 Next.js에 집중하고자 합니다.

그 이유는 2022년 10월 Next.js 13 version이 나오면서 많은 것들이 바뀌며 사용률, 만족도가 압도적으로 높아졌습니다.  웹 프레임워크의 특성상 해당 프레임워크 커뮤니티의 크기가 중요하기에, 아직 인지도가 적은 타 프레임워크들보다는 만족도가 높고 활발한 커뮤니티를 가진 Next.js가 가장 유용할 것이라 판단했습니다. 




npm trends


Next.js는 SSR(Server Side Rendering)으로 동작하는 리액트 프레임워크입니다. SSR은 서버 측에서 즉시 렌더링 가능하게끔 가공한 html파일을 만들어 브라우저에게 보내고, 브라우저는 이를 다운하여 즉각 화면에 렌더링할 수 있는 방식입니다. 또한 Next.js는 Code splitting이라는 기술을 통해 초기 로드 시 필요한 최소한의 코드만 다운로드하여 실행하므로, 앱의 초기 로딩 속도를 개선함과 동시에 React보다 가볍게 동작할 수 있습니다. SSR이기에 SEO 또한 훌륭합니다. 심지어 13버전부터 원하는 페이지에서 CSR이 가능하기 때문에 Next.js의 장점만 쓸 수 있어졌다고 할 수 있습니다.





Next.js의 필요성


앞서 React와 비교한 Next.js의 장점들을 설명했지만, 필요성을 강조할만한 내용들이 더 있습니다.

Next.js는 풀스택 프레임워크로 백엔드 개발도 가능합니다.

중요한 것은 프론트엔드, 백엔드 개발에서 필요한 잡다한 설정들에 드는 수고를 크게 줄여줍니다.

리액트에서의 라우팅, 바벨, 웹팩등의 설정부터, 백엔드의 미들웨어 설정, SEO, SSR 등 많은 것을 Next가 해결해줍니다.

대표적인 기능은 다음과 같습니다.

- Hot reloading : 저장되는 코드를 자동으로 새로고침

- Automatic routing : 따로 라우팅하지 않아도 pages 폴더에 있는 파일이 해당 파일 이름으로 라우팅됩니다.

- single file components : 해당 컴포넌트만 스코프를 가지는 css를 style jsx를 통해 만들 수 있음.

- server landing : 서버렌더링 한 페이지의 소스를 보면 내부에 소스가 있음

- code splitting : 내가 원하는 페이지에서 원하는 자바스크립트와 라이브러리 렌더링 가능

- typescirpt : 웹팩과 바벨을 수정할 필요없이 명령어만 쓰면 자동으로 tsconfig, next-end.d.ts 생성









활용

https://techblog.lotteon.com/next-js-%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-isomorphic-javascript-c77595b626c5

Next.js로 구현하는 Isomorphic JavaScript

구현에만 신경 쓸 수 있도록, Front-end와 Back-end 개발의 진입 장벽을 낮춰 준 프레임워크

techblog.lotteon.com


https://phrygia.github.io/react/2022-11-06-nextjs-13/

[react] Next.js 13

어느날 사수가 갑작스럽게 보내준 링크. (Next.js 13 신버전 발표회 요약 (웹개발자 비상!!)) 나는 프론트엔드 웹개발자로 React를 사용하고 있고 우리회사는 production에서 많이 사용되고 편리한 Next.js

phrygia.github.io
https://kyounghwan01.github.io/blog/React/next/basic/#next-js%E1%84%80%E1%85%A1-%E1%84%8C%E1%85%A6%E1%84%80%E1%85%A9%E1%86%BC%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB-%E1%84%8C%E1%85%AE%E1%84%8B%E1%85%AD-%E1%84%80%E1%85%B5%E1%84%82%E1%85%B3%E1%86%BC

next.js 기본 개념 알아보기

next.js 기본 개념 알아보기, react, seo, ssr

kyounghwan01.github.io






최근에 나온 13버전에서는 기존의 문법이 아예 바뀌었습니다.

기존 리액트 개발자들이 입문하기 쉬우며 서버 데이터 캐싱도 가능하고 이미지 최적화 등이 가능하여 속도에서 개선이 많이 됨. 단점으론 폴더기반 라우팅을 하다보니 예약 파일이 많아 프로젝트가 커지면 복잡해짐.

리액트의 미완성 기능들을 도입하다보니 귀찮은 점이 생김.

클라이언트 컴포넌트와 서버 컴포넌트를 구분해서 코드짜는점 귀찮음.

웹소켓이나 웹RTC는 서버 한대를 따로 만들어야 함.

1인 개발이나 프로토타입 개발 시에는 용이하나 프로젝트가 커지며 백엔드와 프론트엔드를 나누게 되면 풀스택 프레임워크의 의미가 퇴색될 수 있음.

