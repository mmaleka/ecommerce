
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
  images_href = [];
  var time = 4000;

  // Image list
  images[0] = ImageSliderList[0].src;
  images[1] = ImageSliderList[1].src;
  images[2] = ImageSliderList[2].src;

  // Image href
  images_href[0] = ImageSliderList[0].getAttribute("href");
  images_href[1] = ImageSliderList[1].getAttribute("href");
  images_href[2] = ImageSliderList[2].getAttribute("href");

  console.log("href: ", ImageSliderList[1].getAttribute("href"));

} catch (e) {
  console.log("Error", e);
}

// Change Image

function changeImg() {

  document.slide.src = images[i_image];
  // document.slideHref.href = '/10/headsets/';
  var x = document.getElementById("slideHref");
  console.log(images_href[i_image]);
  x.href = images_href[i_image]

  if (i_image < images.length - 1) {
    i_image++;
  } else {
    i_image = 0;
  }
  t = setTimeout("changeImg()", time);
}

function startCount() {
    if (!timer_is_on) {
        timer_is_on = 1;
        changeImg();
    }
}

function stopCount() {
    clearTimeout(t);
    timer_is_on = 0;
}

// Chnage Image with button

function changeImgWithButtonForward(x) {
  stopCount()
  document.slide.src = images[i_image];

  var x = document.getElementById("slideHref");
  console.log(images_href[i_image]);
  x.href = images_href[i_image]

  if (i_image < images.length - 1) {
    i_image++;
  } else {
    i_image = 0;
  }
}

// Chnage Image with button

function changeImgWithButtonPrev(x) {
  stopCount()
  document.slide.src = images[i_image];

  var x = document.getElementById("slideHref");
  console.log(images_href[i_image]);
  x.href = images_href[i_image]

  if (i_image < 1) {
    i_image = images.length - 1;

  }else if (i_image > images.length - 1) {
    i_image = 0;

  } else {
    i_image--;
  }

}


function changeImage(image_id) {

  // Change images on the detail page
  ImageDetailList = document.ImageDetailList;
  var images_detailList1ID = document.getElementById(image_id)
  document.getElementById("mainImage").src = images_detailList1ID.src;

  }

window.onload = changeImg;

function removeElement(elemenetName) {
  g = document.body
  x = g.clientWidth,
  console.log(x);
  if (x < 576) {
    elemenetName[0].style.display='none';
  }

}

try {
  elemenetName = document.getElementsByClassName("my-Catergory");
  removeElement(elemenetName);
} catch (e) {
  console.log("Error");
}


function openAdd() {
  console.log("Redirect user to another page");
}























//
