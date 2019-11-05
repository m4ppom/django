
//ES5 
var colors = ['red', 'blue', 'green'];

// for (var i=0; i < colors.length; i++) {
//     console.log(colors[i]);
// }
//ES6
// function logger(x){
//     console.log(x)
// }
// colors.forEach(logger)

// colors.forEach(function () {
//     console.log(x)
// })

const numbers = [1,2,3];
const doubleNumbers = [];

for (let i=0; i < numbers.length; i++) {
    doubleNumbers.push(numbers[i]*2);
}
console.log(doubleNumbers)
const tripleNumbers = numbers.map(function(number){
    return number * 3;
})
console.log(tripleNumbers)

const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'tomato', type: 'fruit'},
    {name: 'banana', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'},
    {name: 'pear', type: 'fruit'},
];

const fruits =[]
for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    }
}
console.log(fruits);


const vegetables = products.filter((product) => {
    return product.type ==='vegetable';
})
console.log(vegetables);