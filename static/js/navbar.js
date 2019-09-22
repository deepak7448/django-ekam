var yAxis, xs, ys, count = false;

var scollAnimation = function (event) {
    xAxis = scrollX;
    yAxis = scrollY;
    if (yAxis < 40) {
        document.querySelector("nav").classList.remove("activeNav");
        document.querySelector(".navbar").classList.remove("activeNavbar");
    } else if (yAxis > 40) {
        document.querySelector("nav").classList.add("activeNav");
        document.querySelector(".navbar").classList.add("activeNavbar");
   }
}
var stopScroll = function () {
    if (count) {
        window.scroll(xs, ys);
    }
}
document.querySelector(".menu").addEventListener("click", function () {
    this.classList.toggle("activeMenu");
    document.querySelector("nav").classList.toggle("navOnOff");
    count = !count;
    xs = scrollX;
    ys = scrollY;
    window.addEventListener("scroll", stopScroll);
});

window.addEventListener("scroll", scollAnimation);