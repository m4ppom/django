// 1. 선언형
function a(x, y) {
    return x + y
}

// 2. 할당형 는 이있으면 ;
const b = (x, y) => {
    return x + y;
};

const c = function(x, y) {
    return x + y;
};

// shorten 짧게 == 조건이있음 함수 블록에 코드가 return문 한줄이라면 return 도 생략
const d = (x, y) => x + y;
// 짧게 ==> 함수의 인자가 단 하나일 때
const e = () => {
    return false; // 없으면 () 써야함 
}
const f = _ => {  // 없으면 _로 쓰기도함
    return false;
}

const g = x => x ** 2;  // 함수 블록의 return 문 한 줄이면 {}생략가능

//함수 인자가 1개고 return 포함 한 줄 일 때
function square (x){
    return x**2;
};
const square = (x) => {
    return x**2
}
const square = x => x**2;
