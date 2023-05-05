//sacar precio por cantidad
function updateTotal() {
    // filas de la tabla
    var rows = document.querySelectorAll("table tr");
    // inicializar costo total
    var subtotal = 0;
    // Loop through each row (skipping the first row, which contains the headers)
    for (var i = 1; i < rows.length; i++) {
        // Get the cells in the current row
        var cells = rows[i].cells;
        // Get the price and quantity from the cells
        var price = parseFloat(cells[1].textContent.replace("$", ""));
        var quantity = parseInt(cells[2].querySelector("input").value);
        // Calculate the total cost for this item
        var itemTotal = price * quantity;
        // Update the total cost for this item in the table
        cells[3].textContent = "$" + itemTotal.toFixed(2);
        // Add the total cost for this item to the overall total cost
        subtotal += itemTotal;
    }
    // Update the total cost at the bottom of the page
    document.querySelector("#subtotal").textContent = "Subtotal: $" + subtotal.toFixed(2);
}

/*boton continuar*/
function continuar() {
    window.location.href = "#tab2";
}

/*boton enviar*/
function enviar() {
    document.querySelector('form').onsubmit = e => {
        e.preventDefault()
        window.location.href = "#tab3";
    }
}

/*boton compra final*/
function comprar() {
    document.querySelector('form').onsubmit = e => {
        e.preventDefault()
        alert('Tu pedido ha sido correctamente procesado.\n' + "Sigue navegando en nuestra pagina");
        window.location.href = "#tab1";
    }
}
/*function comprar() {
    alert('Tu pedido ha sido correctamente procesado.\n' + "Sigue navegando en nuestra pagina");
    window.location.href = "#tab1";
}*/
