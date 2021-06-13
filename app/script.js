// we fetch our box
const box = document.body.querySelector("div.box")

// on animation complete we tint the box red
box.addEventListener("transitionend", () => box.style.backgroundColor = "red")

// and start our animation
requestAnimationFrame(() => box.style.transform = "translate(0px, 100px)")