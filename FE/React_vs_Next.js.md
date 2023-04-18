# React와 Next.js의 차이

</br>

React는 Javascript 기반의 SPA 웹 프레임워크입니다. 컴포넌트를 활용하여 UI를 쉽고 효율적으로 만들 수 있습니다.

이 글에서 강조하고자 하는 내용은 리액트는 CSR(Client Side Rendering), 즉 화면을 그리는 렌더링이 클라이언트에게서 발생합니다. 서버에서 보내주는 HTML과 Javascript 파일을 서버가 아닌, 클라이언트의 브라우저에서 페이지를 만들어줍니다. 이러한 방식은 페이지 간 전환이 부드러워지는 장점이 있습니다. 하지만 HTML과 JS를 다운로드 받는동안 클라이언트는 렌더링이 불가능한, 즉 첫 페이지의 로딩속도가 느리다는 단점이 있습니다. 또한 CSR의 특성상 빈 HTML과 JS를 보낸 뒤 클라이언트의 브라우저에서 JS를 실행시켜 화면을 그리는데, 대부분의 검색 엔진은 HTML 파일만 크롤링합니다. Meta 태그 또한 크롤링 봇이 가져가지 못하기에, meta 태그를 이용하는 마케팅 툴또한 사용할 수 없습니다. 이러한 점들은 SEO(Search Engine Optimization)에 악영향을 끼쳐 구글과 같은 검색 사이트의 상위 노출에 불리해집니다. 이는 웹 비즈니스에 있어 매우 큰 단점으로 작용합니다.

</br>

이러한 단점들을 극복하기 위해 최근 들어 React Meta-Framework들이 나왔습니다.

대표적으로 Gatsby, Next.js, Remix 등이 있는데, 그중에서도 Next.js에 집중하고자 합니다.

그 이유는 2022년 10월 Next.js 13 version이 나오면서 많은 것들이 바뀌며 사용률, 만족도가 압도적으로 높아졌습니다.  웹 프레임워크의 특성상 해당 프레임워크 커뮤니티의 크기가 중요하기에, 아직 인지도가 적은 타 프레임워크들보다는 만족도가 높고 활발한 커뮤니티를 가진 Next.js가 가장 유용할 것이라 판단했습니다. 

<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcnfkkI%2FbtsaffnLaE3%2F9w9hIsc69aGORILwluBIYK%2Fimg.png">

</br>

Next.js는 SSR(Server Side Rendering)으로 동작하는 리액트 프레임워크입니다. SSR은 서버 측에서 즉시 렌더링 가능하게끔 가공한 html파일을 만들어 브라우저에게 보내고, 브라우저는 이를 다운하여 즉각 화면에 렌더링할 수 있는 방식입니다. 또한 Next.js는 Code splitting이라는 기술을 통해 초기 로드 시 필요한 최소한의 코드만 다운로드하여 실행하므로, 앱의 초기 로딩 속도를 개선함과 동시에 React보다 가볍게 동작할 수 있습니다. SSR이기에 SEO 또한 훌륭합니다. 심지어 13버전부터 원하는 페이지에서 CSR이 가능하기 때문에 Next.js의 장점만 쓸 수 있어졌다고 할 수 있습니다.

</br>


# Next.js의 필요성

</br>

앞서 React와 비교한 Next.js의 장점들을 설명했지만, 필요성을 강조할만한 내용들이 더 있습니다.

Next.js는 풀스택 프레임워크로, 백엔드 개발도 가능합니다.

중요한 것은 프론트엔드, 백엔드 개발에서 필요한 잡다한 설정들에 드는 수고를 크게 줄여줍니다.

리액트에서의 라우팅, 바벨, 웹팩등의 설정부터, 백엔드의 미들웨어 설정, SEO, SSR 등 많은 것을 Next가 해결해줍니다.

</br>


대표적인 기능은 다음과 같습니다.

</br>


- Hot reloading : 저장되는 코드를 자동으로 새로고침

- Automatic routing : 따로 라우팅하지 않아도 pages 폴더에 있는 파일이 해당 파일 이름으로 라우팅됩니다.

- single file components : 해당 컴포넌트만 스코프를 가지는 css를 style jsx를 통해 만들 수 있음.

- server landing : 서버렌더링 한 페이지의 소스를 보면 내부에 소스가 있음

- code splitting : 내가 원하는 페이지에서 원하는 자바스크립트와 라이브러리 렌더링 가능

- typescirpt : 웹팩과 바벨을 수정할 필요없이 명령어만 쓰면 자동으로 타입스크립트 컴파일러가 Next.js의 타입을 가져오게 하는 next-end.d.ts 및 트랜스파일을 위한 tsconfig 생성


</br>

# Next.js 13 버전 변경점

</br>

최근에 나온 13버전에서는 기존의 문법이 바뀐점이 많습니다. 하나하나 살펴보겠습니다.

구체적인 변경점은 공식문서 https://beta.nextjs.org/docs를 참고하세요.

</br>


### 1. app directory 추가

Next.js에서는 react-router-dom 없이 Automatic routing이 가능하도록 하는 파일시스템 기반 라우팅을 위한 pages 디렉토리가 있었습니다. 13버전에서 라우팅 방식을 향상시킨 app 폴더가 추가로 생겼습니다. 현재는 pages와 app 모두 사용가능한 베타 버전입니다.




app 디렉토리를 통해 Layout, React server component, streaming, data fetching 기능을 쉽고 효율적으로 사용할 수 있습니다. 추가된 각각의 기능에 대해 알아보겠습니다.


</br>

- Layout

Layout은 리소스가 큰 중복되는 컴포넌트의 리렌더링을 피해 웹 성능을 향상시킬 수 있습니다. 

또한 각 라우팅 위치에 컴포넌트, 스타일, 테스트 관련 코드를 넣을 수 있게 됐습니다.


</br>

- React server components

server components를 사용하면 초기 페이지 로드 속도가 빨라지고 클라이언트 측 Javascript 번들의 크기가 줄어들 수 있다고 합니다. 또한 런타임이 async하게 로딩되며, 별도의 설정없이 server component를 통한 성능 최적화가 가능합니다.

Client component를 원한다면 'use client' 명령어를 통해 선택적인 컴포넌트 사용도 가능합니다.


</br>

- Streaming

서버 단에서 컴포넌트를 점진적으로 렌더링하여 클라이언트에게 전달할 수 있습니다.

기존에 서버 사이드 렌더링을 할 때 데이터가 fetch될 때까지 기다려야 했던 문제를, 고정적인 레이아웃을 먼저 렌더링하고 이후 다른 부분을 data fetch가 끝나면 별도로 렌더링을 하여 클라이언트에 전달하는 방식으로 해결하였습니다.


</br>

- Data fetching

이전 버전에서는 Data fetching 시 getStaticProps와 getServerSideProps 함수를 별도로 export하였지만, 13버전에서는 리액트 use 훅을 사용해 fetch 함수를 실행하여 쉽고 직관적으로 사용할 수 있습니다.


</br>

### 2. Turbopack


</br>

기존 Webpack을 대체하는 Rust 기반의 새로운 번들러입니다. Server Components, Typescript, jsx, css를 모두 지원하며 Webpack보다 700배, Vite보다 10배 빠르다고 합니다. 

그 외에도 adaptable bundling을 통해 빠르고 유연하며, 다양한 장점을 제공한다고 합니다.


</br>


### 3. next/image

</br>


Image 컴포넌트를 통해 이미지 파일을 넣으면, 이미지 로드가 느릴 때 발생하던 Layout shift(레이아웃이 밀려나는)현상없이 이미지를 자동으로 최적화해줍니다. 또한 alt 속성이 추가되어 웹 접근성이 향상되었습니다.


</br>

### 4. next/font


</br>

마찬가지로 Layout shift가 방지되며, 구글 폰트가 내장되어 브라우저에서 별도로 요청을 하지 않고 사용할 수 있게 되었습니다. 아래와 같이 사용할 수 있습니다.
```javascript
Import {Inter} from '@next/font/google';
const font = Inter();
<html className={font.className}>
```
</br>

### 5. next/link


</br>

이전엔 'Link' 태그를 사용하려면 'a' 태그를 필요로 했지만, 이제 'a 태그 없이 'Link' 만으로 동작 가능합니다.


</br>

### 6. OpenGraph Image


</br>

OpenGraph Image란 카카오톡 #으로 검색했을 때 제목과 이미지가 함께 미리보기로 나오는 것처럼, 특정 사이트를 링크했을 때 링크걸린 사이트를 어떻게 표시할 지 나타내는 것입니다. 이 미리보기 이미지는 생성이 복잡하고 비용이 비쌌지만, @vercel/og라는 라이브러리를 통해 dynamic한 social cards를 만들 수 있으며 이는 SEO에도 도움이 됩니다.


</br>

### 7. Middleware API


</br>

이전 버전과 달리 Middleware에서 request의 header 값을 더 쉽게 세팅할 수 있어졌고, rewrite나 redirect 없이 response에서 json 형태로 처리할 수 있어졌습니다. 


</br>

# Next.js 단점은 없을까?

</br>

기존 리액트 개발자들이 입문하기 쉽고, 서버 데이터 캐싱도 가능하며, 이미지 최적화 등 성능 면에서 많은 개선이 된 Next.js 13버전입니다. 그렇다면 Next.js의 단점은 없을까요?

</br>


사용자들이 꼽는 단점은 다음과 같습니다.


</br>

- 폴더기반 라우팅(Automatic routing)을 하다보니 예약 파일이 많기에 프로젝트가 커지면 복잡해집니다.

- 페이지 이동 시 새로운 페이지를 요청하기에 이동 시 깜박임이 존재합니다.

- 리액트의 미완성 신기능이 도입되어 종종 에러가 생깁니다. 


</br>



Next.js는 1인 개발이나 프로토타입을 빠르게 개발해야할 때 용이하나, 프로젝트가 커지며 여러 팀원이 백엔드와 프론트엔드를 나누어 작업할 때가 오면 풀스택 프레임워크의 의미가 퇴색될 수 있습니다. 신기술의 성격 상 새로운 버전이 계속 나오고 팔로우업을 지속적으로 해야하는 데, 이러한 러닝커브 또한 고려대상입니다. 하지만 SSR이 가진 장점, SEO 및 다양한 렌더링 패턴을 통한 사용자 경험의 향상은 매우 강력합니다. 기업에서 프로젝트를 React에서 Next.js로 마이그레이션하는 경우도 많아지고 있기에, 충분히 공부해 볼만한 전망이 밝은 프레임워크라 생각됩니다.

