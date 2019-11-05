/*
python
def adder(x, y):
    return x+y

*/

function adder(x, y){  // 선언식
    return x + y;
}
// python에서는 안됨
//  adder2 = (x, y): return x + y

const adder2 = function(x, y) {return x + y;};
// 할당식

/*
adder3 = lambda x, y: x + y
*/
// ES6+
const adder3 = function (x, y) { return x + y; };
// 고치기 1. function을 지운다.
// 2. ()와 {} 사이에  =>를 넣는다.
const adder4 = (x, y) => {return x + y;};
// arrow function
