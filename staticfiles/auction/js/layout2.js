document.addEventListener('DOMContentLoaded', function () {
     // Debouncing mechanism for the scroll event
     let debounceTimer;
     window.onscroll = function () {
          clearTimeout(debounceTimer);
          debounceTimer = setTimeout(handleScroll, 20); // Adjust debounce delay as needed
     };

     // Get the navbar, nav links, sign-in element, and sticky form
     let header = document.getElementById("header");
     let navLinks = document.getElementsByClassName("nav-link");
     let signIn = document.getElementById("sign-in");

     // Get the offset position of the navbar
     let sticky = header.offsetTop;
     console.log("sticky:", sticky);



     // Add or remove the sticky class and update styles based on scroll position
     function handleScroll() {
          if (window.scrollY > 82.2) {
               header.classList.add("sticky");
               header.classList.add("bg");
               signIn.classList.add("white-color");
               updateNavLinksColor("#931a25");
               console.log(window.scrollY);
          } else {
               header.classList.remove("sticky");
               header.classList.remove("bg");
               signIn.classList.remove("white-color");
               updateNavLinksColor("black");
          }
     }

     // Helper function to update the color of nav links
     function updateNavLinksColor(color) {
          for (let i = 0; i < navLinks.length; i++) {
               navLinks[i].style.color = color;
          }
     }
});

// Remove Letter Spacing Last Letter ButtonOne
document.addEventListener('DOMContentLoaded', function () {
     const elements = document.querySelectorAll('.buttonOne');
     const letters = document.querySelectorAll('.dropbtn span');



     elements.forEach(function (element) {
          const text = element.textContent;
          const lastLetter = text.slice(-1);
          const newText = text.slice(0, -1) + '<span class="no-letter-spacing">' + lastLetter + '</span>';
          element.innerHTML = newText;
     });

     letters.forEach(function (letter) {
          const text = letter.textContent;
          const lastLetter = text.slice(-1);
          const newText = text.slice(0, -1) + '<span class="no-letter-spacing">' + lastLetter + '</span>';
          letter.innerHTML = newText;
     });
});