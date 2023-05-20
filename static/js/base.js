console.log("JavaScript here!");
AOS.init({
  duration: 1200,
});
let cart = [];
$(function () {
  if (localStorage.cart) {
    cart = JSON.parse(localStorage.cart);
    showCart();
  }
});
function addToCart(id) {
  let lessons = document.querySelectorAll('[id^="lesson-"]');
  // lessons = Array.from(lessons).map(function (item) {
  //   return item.id;
  // });
  // Array.from(lessons);
  // let lessons = $('[id^=lesson-]');
  cart.push(id)
}
function saveCart() {
  if (window.localStorage) {
    localStorage.cart = JSON.stringify(cart);
  }
}
