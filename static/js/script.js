$(document).ready(function () {

    let rgb = [1, 1, 1]
    let freq = 1;

    var slider_red = document.getElementById("red");
    var output_red = document.getElementById("value-red");
    output_red.innerHTML = slider_red.value; // Display the default slider_red value

    // Update the current slider_red value (each time you drag the slider_red handle)
    slider_red.oninput = function () {
        output_red.innerHTML = this.value;
        rgb[0] = this.value
        // console.log(rgb)
        // changeColor(rgb)
        style.innerHTML = keyFrames.replace(/A_DYNAMIC_VALUE/g, 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')');
    }

    var slider_green = document.getElementById("green");
    var output_green = document.getElementById("value-green");
    output_green.innerHTML = slider_green.value; // Display the default slider_green value

    // Update the current slider_green value (each time you drag the slider_green handle)
    slider_green.oninput = function () {
        output_green.innerHTML = this.value;
        rgb[1] = this.value
        // console.log(rgb)
        // changeColor(rgb)
        style.innerHTML = keyFrames.replace(/A_DYNAMIC_VALUE/g, 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')');
    }

    var slider_blue = document.getElementById("blue");
    var output_blue = document.getElementById("value-blue");
    output_blue.innerHTML = slider_blue.value; // Display the default slider_blue value

    // Update the current slider_blue value (each time you drag the slider_blue handle)
    slider_blue.oninput = function () {
        output_blue.innerHTML = this.value;
        rgb[2] = this.value
        // console.log(rgb)
        // changeColor(rgb)
        style.innerHTML = keyFrames.replace(/A_DYNAMIC_VALUE/g, 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')');
    }

    var slider_freq = document.getElementById("freq");
    var output_freq = document.getElementById("value-freq");
    output_freq.innerHTML = slider_freq.value; // Display the default slider_freq value

    // Update the current slider_freq value (each time you drag the slider_freq handle)
    slider_freq.oninput = function () {
        output_freq.innerHTML = this.value;
        freq = parseInt(1000/this.value)
        pulse(freq)
    }

    $("button.check-pulse").click(function () {
        console.log("freq on btn:", freq)
    //     pulse(freq)
    })

    var style = document.createElement('style');
    style.type = 'text/css';
    var keyFrames = '\
@-webkit-keyframes pulse {\
    0% {\
        background-color: white;\
    }\
    50% {\
        background-color: A_DYNAMIC_VALUE;\
    }\
    100% {\
        background-color: white;\
    }\
}\
@-moz-keyframes pulse {\
    0% {\
        background-color: white;\
    }\
    50% {\
        background-color: A_DYNAMIC_VALUE;\
    }\
    100% {\
        background-color: white;\
    }\
}';
style.innerHTML = keyFrames.replace(/A_DYNAMIC_VALUE/g, 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')');
    document.getElementsByTagName('head')[0].appendChild(style);

})

function changeColor(rgb) {
    $(".testingCard .card-body").css({ "background": 'rgb(' + rgb[0] + ',' + rgb[1] + ',' + rgb[2] + ')' })
}

function pulse(freq) {
    if (freq == 0) {
        // return console.warn("do something")
        $('.pulsate').css({
            transition: 'all 1s ease-in-out',
            opacity: '0'
        })
    }
    else {

        // setInterval(function () {
        //     console.log("setinterval")
        //     // $('.pulsate').animate({
        //     //     transition: 'all 1s ease-in-out',
        //     //     opacity: '0'
        //     // }, 100, function () {
        //     //     $('.pulsate').animate({
        //     //         transition: 'all 1s ease-in-out',
        //     //         opacity: '1'
        //     //     }, 100, function () {
        //     //         console.log("pulse callback")
        //     //     });
        //     // });

        // }, freq);
        console.log(freq)
        $(".pulsate-active").css({"animation":"pulse "+freq+"ms infinite"})

    }

}

