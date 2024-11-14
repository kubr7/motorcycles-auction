// Filter Form Stick to top When Scroll
document.addEventListener("DOMContentLoaded", function () {
     const stickyForm = document.getElementById("sticky-form");
     const filterForm = document.getElementById('filter-form-id');

     window.addEventListener("scroll", function () {
          if (window.scrollY > 0) {
               stickyForm.classList.add("sticky-filter-form");
               stickyForm.classList.add("bg");
          } else {
               stickyForm.classList.remove("sticky-filter-form");
               stickyForm.classList.remove("bg");
          }
     });
});




// Filter - Search - Caret - Logic 

document.addEventListener('DOMContentLoaded', function () {
     const customSelects = document.querySelectorAll('.dropdown');

     customSelects.forEach(selectBox => {
          const selected = selectBox.querySelector('.dropbtn');
          const items = selectBox.querySelector('.dropdown-content');
          const hiddenInput = selectBox.querySelector('input[type="hidden"]');
          const caretSign = selectBox.querySelector('.fa-solid'); // Assuming this selects the caret icon element

          if (selected && items && hiddenInput && caretSign) {
               selectBox.addEventListener('mouseenter', function () {
                    openSelect(selectBox);
               });

               selectBox.addEventListener('mouseleave', function () {
                    closeSelect(selectBox);
               });

               items.addEventListener('click', function (e) {
                    if (e.target && e.target.nodeName === "P") {
                         selected.innerHTML = e.target.innerHTML;
                         hiddenInput.value = e.target.getAttribute('data-value');
                         selected.style.borderBottomColor = '#931A25';
                         closeSelect(selectBox);
                    }
               });
          } else {
               console.error("One or more required elements not found.");
          }
     });

     function openSelect(selectBox) {
          const items = selectBox.querySelector('.dropdown-content');
          const caretSign = selectBox.querySelector('.fa-solid');

          if (items && caretSign) {
               caretSign.classList.remove('fa-caret-right');
               caretSign.classList.add('fa-caret-down');
               caretSign.style.transform = 'scale(1.5)';
          }
     }

     function closeSelect(selectBox) {
          const items = selectBox.querySelector('.dropdown-content');
          const caretSign = selectBox.querySelector('.fa-solid');

          if (items && caretSign) {
               caretSign.classList.remove('fa-caret-down');
               caretSign.classList.add('fa-caret-right');
               caretSign.style.transform = 'scale(1)';
          }
     }
});

// Search Input Label Hide
document.addEventListener('DOMContentLoaded', function () {
     let searchInput = document.getElementById('search-input');
     let searchLabel = document.getElementById('search-label');

     if (searchInput && searchLabel) {
          searchInput.addEventListener('focus', function () {
               searchLabel.classList.add('hidden');
          });

          searchInput.addEventListener('blur', function () {
               if (!searchInput.value) {
                    searchLabel.classList.remove('hidden');
               }
          });
     } else {
          console.error("Search input or label not found.");
     }
});


document.addEventListener("DOMContentLoaded", function () {
     let endTime = new Date("{{ motorcycle.end_time|date:'c' }}").getTime();
     let now = new Date().getTime();
     let timeRemaining = endTime - now;

     function formatNumber(number) {
          let numStr = number.toString().split("").reverse().join("");
          let parts = [];
          parts.push(numStr.substring(0, 3));
          for (let i = 3; i < numStr.length; i += 2) {
               parts.push(numStr.substring(i, i + 2));
          }
          return parts.join(",").split("").reverse().join("");
     }

     if (timeRemaining <= 0) {
          return;
     } else {
          const rangeInput = document.getElementById("bidRange");
          const inputNumber = document.getElementById("bidNumber");
          const rangeValueDisplay = document.getElementById("rangeValueDisplay");

          if (rangeInput && inputNumber && rangeValueDisplay) {
               let initialValueStr = "{{ motorcycle.current_bid.bid_amount|default:motorcycle.start_price }}";
               console.log("Initial Value String:", initialValueStr);

               // Strip any potential whitespace or non-numeric characters
               initialValueStr = initialValueStr.replace(/[^0-9.]/g, '');
               let initialValue = parseFloat(initialValueStr);
               console.log("Parsed Initial Value:", initialValue);

               if (!isNaN(initialValue)) {
                    rangeInput.min = initialValue;
                    rangeInput.value = initialValue;
                    rangeValueDisplay.textContent = formatNumber(initialValue);
                    inputNumber.value = initialValue;

                    rangeInput.addEventListener("input", function () {
                         let currentValue = parseFloat(rangeInput.value);
                         rangeValueDisplay.textContent = formatNumber(currentValue);
                         inputNumber.value = currentValue;
                    });

                    inputNumber.addEventListener("input", function () {
                         let currentValue = parseFloat(inputNumber.value);
                         if (!isNaN(currentValue) && currentValue >= parseFloat(rangeInput.min)) {
                              rangeInput.value = currentValue;
                              rangeValueDisplay.textContent = formatNumber(currentValue);
                         }
                    });
               } else {
                    console.error("Initial value is not a valid number:", initialValueStr);
               }
          } else {
               console.error("One or more elements are not found in the DOM");
          }
     }
});


// Carousel
document.addEventListener('DOMContentLoaded', () => {
     const container = document.querySelector('.carousel-container');
     const cards = document.querySelectorAll('.carousel-container .card');
     let currentIndex = 0;
     const cardWidth = cards[0].offsetWidth;
     const cardMargin = 10; // Adjust based on your card's margin/padding

     // Adjust these base values as needed
     const baseSlideInterval = 5000;
     const baseTransitionTime = 2000;

     // Configurable factor to adjust timing based on the number of cards
     const timingFactor = 1.5; // Adjust this factor to suit your needs

     // Calculate slideInterval and transitionTime based on the number of cards
     const slideInterval = baseSlideInterval * (cards.length / timingFactor);
     const transitionTime = baseTransitionTime * (cards.length / timingFactor);

     // Center the first card initially
     container.style.transform = `translateX(calc(50% - ${(cardWidth + cardMargin * 2) / 2}px))`;

     function slide() {
          currentIndex++;
          if (currentIndex >= cards.length) {
               // Move to the first slide with transition disabled
               container.style.transition = 'none';
               container.style.transform = `translateX(100%)`;
               currentIndex = 0;
               console.log("Hi if");
               setTimeout(() => {
                    console.log("Hi if setTimeout");
                    container.style.transition = `transform ${transitionTime}ms linear`;
                    container.style.transform = `translateX(calc(50% - ${(cardWidth + cardMargin * 2) / 2}px - ${(cardWidth + cardMargin * 2) * currentIndex}px))`;
               }, 50); // Small delay to ensure transition re-enables
          } else {
               console.log("Hi else");
               container.style.transition = `transform ${transitionTime}ms linear`;
               container.style.transform = `translateX(calc(50% - ${(cardWidth + cardMargin * 2) / 2}px - ${(cardWidth + cardMargin * 2) * currentIndex}px))`;
          }
     }

     setTimeout(slide, 2000);

     setInterval(slide, slideInterval);
});
