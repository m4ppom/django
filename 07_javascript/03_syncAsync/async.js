// non-blocking

function sleep_3s(){
    setTimeout(()=>{console.log('wake up')}, 3000)
}

console.log('start sleeping')
sleep_3s()
console.log('end of program')
