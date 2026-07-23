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