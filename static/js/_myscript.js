function removeElement(elemenetName) {
  g = document.body
  x = g.clientWidth,
  console.log(x);
  if (x < 576) {
    elemenetName.style.display='none';
  }

}

function changeClassCheckout() {
   var elementCheckout = document.getElementById("id_payment_method");
   elementCheckout.classList.add("form-control");
   elementCheckout.style.display='none';
   var elementShippingMethod = document.getElementById("id_shipping");
   elementShippingMethod.classList.add("form-control");
}

function changeClassCart() {
   var elementCart = document.getElementById('id_quantity');
   elementCart.classList.add("btn");
   elementCart.classList.add("btn-info");
   elementCart.classList.add("dropdown-toggle");
}

function changeProductReviewTextArea() {
   var elementTextArea = document.getElementById("id_content").rows = "3";
   console.log("elementTextArea", elementTextArea);
   elementTextArea.classList.add("form-control");
}



try {
  elemenetNameFooter = document.getElementsByClassName("my-footer");
  removeElement(elemenetNameFooter[0]);
} catch (e) {
  console.log("Error removing footer for small deviced: ", e);
}


try {
  productImage = document.getElementsByClassName("container");
  changeClassCheckout()
} catch (e) {
  console.log("Error changing class checkout");
}

try {
  productReview = document.getElementById('id_content');
  changeProductReviewTextArea(productReview)
} catch (e) {
  console.log("Error changing product review text area", e);
}




function shippingChoices(freeDelivery, payDeliverly) {
  var shipping = document.getElementById('id_shipping');
  var strUser = shipping.options[shipping.selectedIndex].value;
  if (strUser == 'FD') {
    var get_total_price_with_free_shipping = document.getElementById('get_total_price_with_shipping').innerHTML="R "+freeDelivery;
  } else if (strUser == 'PL') {
    var get_total_price_with_pay_shipping = document.getElementById('get_total_price_with_shipping').innerHTML="R "+payDeliverly;
  }
}


































//
