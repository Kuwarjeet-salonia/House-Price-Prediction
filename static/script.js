const card = document.querySelector(".card")
document.addEventListener("mousemove",(e) => {
    if(card instanceof HTMLElement){
    let x = (window.innerWidth/2-e.pageX)/25;
    let y = (window.innerHeight/2-e.pageY)/25;
    card.style.transform = 'rotateY(${x}deg)rotateX(${-y}deg)';
    }    
});
document.addEventListener("mouseleave",()=>{
    if (card instanceof HTMLElement){
        card.style.transform = "rotateY(0deg)rotateX(0deg)";
    }
});