
try{
  productImage = document.getElementsByClassName("productImage");
  image = productImage[0].getElementsByTagName("img")
  console.log(image.length);
  for (i = 0; i < productImage.length; i++) {
    image = productImage[i].getElementsByTagName("img");

    for (ii = 0; ii < image.length; ii++) {
      image[ii].style.display='none';
      image[ii].style.display='none';
    };

    console.log(image);
    image[0].style.display='block';
  }
}
catch(err){
  console.log("Error", err);
}



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

window.onload = changeImg;
