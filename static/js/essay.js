console.log('essay.js');

// navigation buttons
let navigationBtnEl = document.getElementsByClassName("navigation-button");
let navigationBtnElArray = Array.from(navigationBtnEl);

navigationBtnElArray.forEach(el => {
    let link = el.getAttribute('link');
    
    if (link) {
        el.addEventListener('click', () => {
            navigationFunction(link);
        });
    }
    
    else{
        el.style.color = 'grey';
    }
});

function navigationFunction(link) {
    console.log(link);
    window.location.href = link;
}

// other hyperlinks (if any)
let hyperlinkBtnEl = document.getElementsByClassName("hyperlink");
let hyperlinkBtnElArray = Array.from(hyperlinkBtnEl);

hyperlinkBtnElArray.forEach(el => {
    let link = el.getAttribute('link');

    if (link) {
        el.addEventListener('click', () => {
            hyperlinkFunction(link);
        });
    }
});

function hyperlinkFunction(link) {
    console.log(link);
    // window.location.href = link;
}