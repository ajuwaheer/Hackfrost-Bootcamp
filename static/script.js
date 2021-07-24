// For darkmode
const isDark = localStorage.getItem("bootcampDark");
const darkmode = document.querySelector("#darkmode");
const root = document.querySelector(":root");

darkmode.addEventListener("click", (event) => {
    const mode = event.target.innerText;
    if (mode === "dark_mode") {
        localStorage.setItem("bootcampDark", "dark_mode");
        darkmode.innerText = "light_mode";
        setDarkMode();
    } else {
        localStorage.setItem("bootcampDark", "light_mode")
        darkmode.innerText = "dark_mode";
        setLightMode();
    }
    location.reload();
})

// Style properties for dark mode (Light mode contrast colors)
const setDarkMode = () => {
    root.style.setProperty("--accent-color", "#F4A261");
    root.style.setProperty("--light-mode-gray", "#3C4042");
    root.style.setProperty("--light-mode-white", "#212121");
    root.style.setProperty("--light-mode-black", "white");
}

// Style properties for light mode
const setLightMode = () => {
    root.style.setProperty("--accent-color", "#FDC79B");
    root.style.setProperty("--light-mode-gray", "rgb(243,243,243");
    root.style.setProperty("--light-mode-white", "white");
    root.style.setProperty("--light-mode-black", "black");
}

// Set whether dark mode is on or off
if (isDark === "dark_mode") {
    darkmode.innerText = "light_mode";
    setDarkMode();
} else {
    darkmode.innerText = "dark_mode";
    setLightMode(); 
}

// For Navbar in mobile (<650 px)
const menu = document.querySelector("#menu");
const body = document.querySelector("body");
const menuList = document.querySelector("nav ul");

menu.addEventListener("click", () => {
    if (menu.innerText === "menu") {
        body.style.overflow = "hidden";
        menu.innerText = "close";
        menuList.style.display = "flex";
    } else {
        menu.innerText = "menu";
        menuList.style.display = "none";
    }
})

// For create blog page (Image Preview)
const imageLink = document.querySelector(".createblog #imageLink");
const imagePreview = document.querySelector("#imagePreview");

console.log(imageLink)
console.log(imagePreview)
imageLink.addEventListener("keyup", () => {
    console.log(imageLink.value)
    imagePreview.src = imageLink.value
})

