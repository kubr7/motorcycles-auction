
// Filter

document.addEventListener('DOMContentLoaded', function () {
     const customSelects = document.querySelectorAll('.custom-select');

     customSelects.forEach(selectBox => {
          const selected = selectBox.querySelector('.select-selected');
          const items = selectBox.querySelector('.select-items');
          const hiddenInput = selectBox.querySelector('input[type="hidden"]');
          const caretSign = selectBox.querySelector('.fa-solid'); // Assuming this selects the caret icon element

          if (selected && items && hiddenInput && caretSign) {
               selected.addEventListener('click', function (event) {
                    event.stopPropagation();

                    if (items.classList.contains('select-hide')) {
                         closeAllSelects(selectBox); // Close all other selects except current one
                         items.classList.remove('select-hide');
                         caretSign.classList.remove('fa-caret-right');
                         caretSign.classList.add('fa-caret-down');
                         caretSign.style.transform = 'scale(1.5)';

                    } else {
                         items.classList.add('select-hide');
                         caretSign.classList.remove('fa-caret-down');
                         caretSign.classList.add('fa-caret-right');
                         caretSign.style.transform = 'scale(1)';
                    }
               });

               items.addEventListener('click', function (e) {
                    if (e.target && e.target.nodeName === "P") {
                         selected.innerHTML = e.target.innerHTML;
                         hiddenInput.value = e.target.getAttribute('data-value');
                         items.classList.add('select-hide');
                         caretSign.classList.remove('fa-caret-down');
                         caretSign.classList.add('fa-caret-right');
                         selected.style.borderBottomColor = '#931A25';
                         caretSign.style.transform = 'scale(1)';
                    }
               });
          } else {
               console.error("One or more required elements not found.");
          }
     });

     document.addEventListener('click', function () {
          closeAllSelects();
     });

     function closeAllSelects(exceptBox) {
          customSelects.forEach(selectBox => {
               const items = selectBox.querySelector('.select-items');
               const caretSign = selectBox.querySelector('.fa-solid');

               if (items) {
                    items.classList.add('select-hide');
               }

               if (caretSign) {
                    caretSign.classList.remove('fa-caret-down');
                    caretSign.classList.add('fa-caret-right');
                    caretSign.style.transform = 'scale(1)';
               }
          });
     }
});





///

// Filter
document.addEventListener('DOMContentLoaded', function () {
     const customSelects = document.querySelectorAll('.custom-select');

     customSelects.forEach(selectBox => {
          const selected = selectBox.querySelector('.select-selected');
          const items = selectBox.querySelector('.select-items');
          const hiddenInput = selectBox.querySelector('input[type="hidden"]');
          const caretSign = selectBox.querySelector('.fa-solid'); // Assuming this selects the caret icon element

          if (selected && items && hiddenInput && caretSign) {
               selected.addEventListener('mouseenter', function (event) {
                    event.stopPropagation();

                    if (items.classList.contains('select-hide')) {
                         closeAllSelects(selectBox); // Close all other selects except current one
                         items.classList.remove('select-hide');
                         caretSign.classList.remove('fa-caret-right');
                         caretSign.classList.add('fa-caret-down');
                         caretSign.style.transform = 'scale(1.5)';

                    }
               });


               items.addEventListener('mouseleave', function (event) {
                    event.stopPropagation();

                    items.classList.add('select-hide');
                    caretSign.classList.remove('fa-caret-down');
                    caretSign.classList.add('fa-caret-right');
                    caretSign.style.transform = 'scale(1)';

               });

               items.addEventListener('click', function (e) {
                    if (e.target && e.target.nodeName === "P") {
                         selected.innerHTML = e.target.innerHTML;
                         hiddenInput.value = e.target.getAttribute('data-value');
                         items.classList.add('select-hide');
                         caretSign.classList.remove('fa-caret-down');
                         caretSign.classList.add('fa-caret-right');
                         selected.style.borderBottomColor = '#931A25';
                         caretSign.style.transform = 'scale(1)';
                    }
               });
          } else {
               console.error("One or more required elements not found.");
          }
     });

     document.addEventListener('click', function () {
          closeAllSelects();
     });

     function closeAllSelects(exceptBox) {
          customSelects.forEach(selectBox => {
               const items = selectBox.querySelector('.select-items');
               const caretSign = selectBox.querySelector('.fa-solid');

               if (items) {
                    items.classList.add('select-hide');
               }

               if (caretSign) {
                    caretSign.classList.remove('fa-caret-down');
                    caretSign.classList.add('fa-caret-right');
                    caretSign.style.transform = 'scale(1)';
               }
          });
     }
});