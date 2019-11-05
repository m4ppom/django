// 1. input 태그 안의 값을 잡는다.
// const input = document.querySelector('#js-userinput').value;
// console.log(input);

// 2. 버튼 태그에는 'click'이 일어났을 때, input에 ENTER키를 쳤을 때 이벤트리스너를 단다.
//    1에서 잡은 값을 요청으로 보낸다.
// 무엇을 .addEventListener([언제], [어떻게])
//                          스트링    함수
// const button = document.querySelector('#js-go');
// const inputArea = document.querySelector('#js-userinput');
// const resultArea = document.querySelector('#js-reault-area')
// // const whenClicked = function(){
// //     console.log('클릭!');
// // }
// // const whenPressed = function() {
// //     console.log('꾸우.');
// // }
// const pushToDom = (data) => {
//     // 요청 => 응답을 받아서

//     //화면에 보여준다.
//     resultArea.innerHTML += data;
// };

// button.addEventListener('click', () => {
//     const inputValue = inputArea.value;
//     pushToDom(inputValue);

// });

// inputArea.addEventListener('keypress', (event) => {
//     if (event.which === 13) {
//         const inputValue = inputArea.value
//         pushToDom(inputValue);
//         // 인풋벨류로 지피아이 에이피아이에 요청보내서 받기
//     }
//     // console.log('꾸우.');
//     // console.log(event)
// });
// // 3. Giphy API에서 넘겨준 Data를 index.html에서 보여준다.

// 1. input 태그 안의 값(value)을 잡는다.
// 2. button 에 'click' 이 일어났을 때, input 에 ENTER키를 쳤을 때 1에서 잡은 값을 요청으로 보낸다.
// [무엇].addEventListener([언제], [어떻게: function])
const button = document.querySelector('#js-go');
const inputArea = document.querySelector('#js-userinput');
const resultArea = document.querySelector('#js-result-area');
const prevButton = document.querySelector('#js-prev-button');
const nextButton = document.querySelector('#js-next-button');


const API_KEY = 'sdEVL3ki0BsQO2ga0RmfhNCH2HV9BwSY'
const testWord = 'dog'
const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${testWord}&limit=3&offset=0&rating=G&lang=en`

prevButton.addEventListener('click', () => {
    const inputValue = inputArea.value; 
    
})


button.addEventListener('click', () => {
    const inputValue = inputArea.value;
    searchAndPush(inputValue);

});

inputArea.addEventListener('keypress', (event) => {
    if (event.which === 13) {
        const inputValue = inputArea.value
        searchAndPush(inputValue);
    }
});

const searchAndPush = (keyword) => {
    const inputCount = document.querySelector('#js-image-count').value;
    const API_KEY = 'sdEVL3ki0BsQO2ga0RmfhNCH2HV9BwSY'
    const url = `https://api.giphy.com/v1/gifs/search?api_key=${API_KEY}&q=${keyword}&limit=${inputCount}&offset=0&rating=G&lang=en`

    const AJAX = new XMLHttpRequest();  // 요청준비
    AJAX.open('GET', url);  // 요청 세팅
    AJAX.send();    //요청보내기
    AJAX.addEventListener('load', function (answer) {
        const res = answer.target.response;
        const giphyData = JSON.parse(res);
        
        const dataSet = giphyData.data;
        inputArea.value = null;
        resultArea.innerHTML = null;

        for (const data of dataSet) {
            pushToDOM(data.images.fixed_height.url);
        }
        // resultArea.innerHTML += giphyData.data[0].images.downsized.url;

    });

    const pushToDOM = (imageUrl) => {
        const imageTag = document.createElement('img')
        imageTag.src = imageUrl;
        imageTag.alt = 'giphy-image';
        imageTag.classList.add('container-image');

        resultArea.appendChild(imageTag);
    }
};

// 3. Giphy API 에서 넘겨준 Data 를 index.html 에서 보여준다.
// const pushToDOM = (data) => {
//     // 요청 => 응답을 받아서.

//     // 화면에 보여준다
//     resultArea.innerHTML += data;
// };

// const sendAjaxReq = () => {
//     // console.log('시작');
//     const AJAX = new XMLHttpRequest();  // 요청준비
//     AJAX.open('GET', url);  // 요청 세팅

//     // console.log('보낸닷');
//     AJAX.send();    //요청보내기
    
//     AJAX.addEventListener('load', function (answer) {
//         // console.log(answer);
//         // console.log(answer.target);
//         const res = answer.target.response;
//         const giphyData = JSON.parse(res);
//         console.log(giphyData);
//     });
//     // console.log('끝');

//     // const response = AJAX.response;
//     // console.log('응답'+ response)
//     // const giphyData = JSON.parse(response);
//     // console.log(giphyData);
// };

