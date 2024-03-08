console.log('universal.js')

const themesBtnEl = document.getElementById('themes-button');
const root = document.documentElement;

let theme = 'light';
function newTheme() {
    if (theme == 'light') {
        return 'dark'
    }

    else {
        return 'light'
    }
}

themesBtnEl.addEventListener('click', () => {
    themesBtnFunction()
})

function themesBtnFunction() {
    theme = newTheme();

    root.style.setProperty('--background-main', `var(--background-${theme})`)
    root.style.setProperty('--primary-main', `var(--primary-${theme})`)
    root.style.setProperty('--secondary-main', `var(--secondary-${theme})`)
}








