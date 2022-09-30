const other_amount = document.querySelector('.other')
const other_amount_field = document.querySelector('.other-amount')

function displayOther () {
    if (other_amount.checked == true) {
        console.log("Checked")
        other_amount_field.style.display = 'block'
    }
    else {
        other_amount_field.style.display = 'none'
    }
}

displayOther()