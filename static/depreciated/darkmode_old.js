// Apply saved theme (from local storage) on first load (if applicable, defaults to light).
// If the theme preference exists in local storage, load it to the 'data-theme' attribute.
const savedTheme = localStorage.getItem("theme");
if (savedTheme) document.documentElement.setAttribute("data-theme", savedTheme);

// Check the current saved theme and apply the opposite when the button is clicked
function handleThemeClick() {
    const current = document.documentElement.getAttribute("data-theme");
    const newTheme = current === "dark" ? "light" : "dark";
    // If changing to the Light theme, remove the 'data-theme' DARK flag.
    // If changing to the Dark theme, add the 'data-theme' DARK flag.
    if (newTheme === "light") {
        document.documentElement.removeAttribute("data-theme");
    } else {
        document.documentElement.setAttribute("data-theme", "dark");
    }
    // Regardless, save 'theme' to Local Storage
    localStorage.setItem("theme", newTheme);
}

// Waits until the DOM is fully loaded before trying to initialize the button.
document.addEventListener('DOMContentLoaded', (event) => {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', handleThemeClick);
        console.log('Event listener attached to themeButton.');
    } else {
        console.error('themeButton element not found!');
    }
});