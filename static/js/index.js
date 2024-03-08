console.log('index.js')

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
    // console.log(link);
    window.location.href = link;
}