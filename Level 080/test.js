function compose(...funcsArr) {
    funcsArr = funcsArr.reverse()
    function callback (argument) {
        let result;
        for(let i = 0; i < funcsArr.length; i++) {
            if ( i === 0) {
                result = funcsArr[i](argument)
            } else {
                funcsArr[i](result)
            }
        }
        return result;
    }
    
    return callback
}

console.log(compose((x) => x * 2, (x) => x + 1)(5))