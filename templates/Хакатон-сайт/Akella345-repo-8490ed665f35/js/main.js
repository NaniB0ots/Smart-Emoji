var firstItem = document.getElementsByClassName('item-1')[0];
var lastItem = document.createElement('div');
lastItem.setAttribute('class', 'item-1');
lastItem.innerHTML = firstItem.innerHTML;
document.getElementsByClassName('slider-line-1')[0].append(lastItem);


function slide1(){
	var radios = document.getElementsByName('slide-pick-1');
    for (var i=0; i<radios.length; i++){
        if (radios[i].checked) var slideNum = radios[i].value;
    }

    if(slideNum == 1){
    	slideNum = 4;
    }

    anime({
	targets: '.slider-line-1',
	translateX: '-'+(slideNum-1)*100+'vw',
	easing: 'linear',
	duration: 1000
	});
}



function autoSlide1(){
	var radios = document.getElementsByName('slide-pick-1');
    for (var i=0; i<radios.length; i++){
        if (radios[i].checked) var slideNum = Number(radios[i].value) + 1;
    }

    if (slideNum == 2){
    	document.getElementsByClassName('slider-line-1')[0].style.transform = 'translateX(0)';
    }

    if(slideNum>radios.length){
    	slideNum = 1;
    }   
    document.getElementById('radio-1-'+slideNum).click();
}

setInterval(autoSlide1, 5000);


var firstItem = document.getElementsByClassName('item-2')[0];
var lastItem = document.createElement('div');
lastItem.setAttribute('class', 'item-2');
lastItem.innerHTML = firstItem.innerHTML;
document.getElementsByClassName('slider-line-2')[0].append(lastItem);


function slide2(){
    var radios = document.getElementsByName('slide-pick-2');
    for (var i=0; i<radios.length; i++){
        if (radios[i].checked) var slideNum = radios[i].value;
    }

    if(slideNum == 1){
        slideNum = 4;
    }

    anime({
    targets: '.slider-line-2',
    translateX: '-'+(slideNum-1)*790+'px',
    easing: 'linear',
    duration: 1000
    });
}



function autoSlide2(){
    var radios = document.getElementsByName('slide-pick-2');
    for (var i=0; i<radios.length; i++){
        if (radios[i].checked) var slideNum = Number(radios[i].value) + 1;
    }

    if (slideNum == 2){
        document.getElementsByClassName('slider-line-2')[0].style.transform = 'translateX(0)';
    }

    if(slideNum>radios.length){
        slideNum = 1;
    }   
    document.getElementById('radio-2-'+slideNum).click();
}

setInterval(autoSlide2, 5000);