alert("Hello blog")


function removeElement(elemenetName) {
  console.log(elemenetName);
  elemenetName[0].style.display='none';

}

elemenetName = document.getElementById("div_id_image");

removeElement(elemenetName);
// removeElement(elemenetNameFooter);
