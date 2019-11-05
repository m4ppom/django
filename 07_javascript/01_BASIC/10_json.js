// .json  javascript object notation : JS의 Object처럼 표시하는 방법.
const me = `
    {
        "name": "neo", 
        "job": "teacher"
    }
`
// JSON으로 표현된 데이터의 타입은 무조건string
// parsing = 구문 분석
const parseData = JSON.parsa(rowJson);
// serializing 공용어로 번역 직렬화
const backToJSON = JSON.stringify(parseData);


