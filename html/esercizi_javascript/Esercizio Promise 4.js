var promise = callback1();

promise.then( (data1) => {
    console.log(data1);
    return callback2();
}).then( (data2) => {
    console.log(data2);
    return callback2();
}).then( (data3) => {
    console.log(data3);
    return callback2();
})

function callback1() {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            resolve("sono nella callback 1");
        }, 2000);
    });
}


function callback2() {
    return new Promise(function(resolve, reject) {
        setTimeout(function() {
            resolve("sono nella callback 2");
        }, 1000);
    });
}