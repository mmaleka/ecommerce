console.log("egfsdfg");

try{
  productImage = document.getElementsByClassName("productImage");
  image = productImage[0].getElementsByTagName("img")
  for (i = 0; i < productImage.length; i++) {
    image = productImage[i].getElementsByTagName("img");

    for (ii = 0; ii < image.length; ii++) {
      image[ii].style.display='none';
      image[ii].style.display='none';
    };
    image[0].style.display='block';
  }
}
catch(err){
  console.log("Error", err);
}



try {
  ImageSliderList = document.ImageSliderList;
  for (var i_ImageSliderList = 0; i_ImageSliderList < ImageSliderList.length; i_ImageSliderList++) {
    ImageSliderList[i_ImageSliderList].style.display = 'none';
  }

  var i_image = 0;
  var images = [];
  var time = 3000;

  // Image list
  images[0] = ImageSliderList[0].src;
  images[1] = ImageSliderList[1].src;
  images[2] = ImageSliderList[2].src;
} catch (e) {
  console.log("Error", e);
}

// Change Image

function changeImg() {
  document.slide.src = images[i_image];

  if (i_image < images.length - 1) {
    i_image++;
  } else {
    i_image = 0;
  }
  setTimeout("changeImg()", time);
}


function changeImage(image_id) {

  // Change images on the detail page
  ImageDetailList = document.ImageDetailList;
  var images_detailList1ID = document.getElementById(image_id)
  document.getElementById("mainImage").src = images_detailList1ID.src;

  }

window.onload = changeImg;













//
