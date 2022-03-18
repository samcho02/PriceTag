const menuBtn = document.querySelector('.navbar_menuBtn');
const menu = document.querySelector('.navbar_menu');
const user = document.querySelector('.navbar_user');

menuBtn.addEventListener('click', () => {
    menu.classList.toggle('active');
    user.classList.toggle('active');
});