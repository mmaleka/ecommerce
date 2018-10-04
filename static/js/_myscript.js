productImage = document.getElementsByClassName("container");

function changeClassCheckout() {
   var elementCheckout = document.getElementById("id_payment_method");
   elementCheckout.classList.add("form-control");
}

function changeClassCart() {
   var elementCart = document.getElementById('id_quantity');
   elementCart.classList.add("btn");
   elementCart.classList.add("btn-info");
   elementCart.classList.add("dropdown-toggle");
}

changeClassCheckout()
