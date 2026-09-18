const today = new Date();

document.getElementById("current-date").textContent =
    today.toLocaleDateString();



function changePage(event, link, effect) {
    event.preventDefault();

    document.body.classList.add(effect);

    setTimeout(() => {
        window.location.href = link.href;
    }, 500);
}

window.addEventListener("pageshow", function () {
    document.body.classList.remove(
        "fade-out",
        "slide-left",
        "zoom-out",
        "zoom-in",
        "blur-out"
    );
});




const button = document.getElementById("piButton");
' we check digits of pi. It is handled in the background as text. Therefore value type is string'
button.addEventListener("click", async function () {

    const value = document.getElementById("piInput").value;

    const response = await fetch(`http://127.0.0.1:8000/${value}`);

    const result = await response.json();

    document.getElementById("piResult").textContent = result;
});

async function sendText() {
    const text = document.getElementById("textInput").value;

    const response = await fetch("http://127.0.0.1:8000/process", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            text: text
        })
    });

    const data = await response.json();

    console.log(data);
}