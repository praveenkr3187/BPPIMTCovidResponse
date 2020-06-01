const hamburger = document.querySelector(".hamburger");
const navlinks = document.querySelector(".navlinks");
const links = document.querySelectorAll(".navlinks li");

hamburger.addEventListener("click",()=>{
    navlinks.classList.toggle("open");
    links.forEach(link =>{
        link.classList.toggle("fade");
    });
});
