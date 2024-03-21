const diseasePrecaution = JSON.parse(document.getElementById('disease_precaution').textContent);
const div = document.getElementById('prediction')
for (let i = 0; i < diseasePrecaution.length; i++) {
    if (diseasePrecaution[i]) {
        console.log(diseasePrecaution[i])
        const res = document.createElement("p")
        const img = document.createElement("img");
        img.src = "/static/images/bullet-grey.png";
        img.style.width = "20px"
        res.appendChild(img)
        res.appendChild(document.createTextNode(diseasePrecaution[i]))
        // res.innerText += `${diseasePrecaution[i]}`
        div.appendChild(res)
    }
}

const hide_func = () => {
    const hide_span = document.getElementsById('d-none');
    for (let i = 0; i < hide_span.length; i++) {
        hide_span[i].style.display = "block !important";
    }
}