// Loader

window.addEventListener("load",()=>{

setTimeout(()=>{

document.getElementById("loader").style.display="none";

},3000);

});

// Typing Animation

new Typed("#typing",{

strings:[
"Python Developer",
"AI Enthusiast",
"Web Developer",
"Hackathon Winner",
"Future Software Engineer"
],

typeSpeed:60,
backSpeed:40,
loop:true

});

// Resume Dropdown

const resumeDropdown = document.getElementById("resumeDropdown");
const resumeBtn = document.getElementById("resumeBtn");

resumeBtn.addEventListener("click",(e)=>{

e.preventDefault();

resumeDropdown.classList.toggle("open");

});

document.addEventListener("click",(e)=>{

if(resumeDropdown && !resumeDropdown.contains(e.target)){

resumeDropdown.classList.remove("open");

}

});