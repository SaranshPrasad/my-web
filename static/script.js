const home = document.getElementById('home');
const aboutme = document.getElementById('aboutme');
const about = document.getElementById('about');
const home2 = document.getElementById('home-2');
aboutme.addEventListener('click', () => {
    home.classList.add('hide');
    about.classList.remove('hide');
});

home2.addEventListener('click', ()=>{
    home.classList.remove('hide')
    about.classList.add('hide')
    
});




