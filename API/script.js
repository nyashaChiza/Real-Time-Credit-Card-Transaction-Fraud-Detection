let counter = 1;
setInterval(() =>{
    document.querySelector('h3').innerText = counter;
    counter++;
}, 50);