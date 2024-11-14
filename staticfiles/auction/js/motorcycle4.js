// Listing Page/ Motorcycle Listing Page
// Sidebar - All bids
// document.addEventListener("DOMContentLoaded", function () {
//   const sidebar = document.getElementById("sidebar");

//   window.addEventListener("scroll", function () {
//     sidebar.style.backgroundColor = 'transparent';
//   });
// });

function openNav() {
  document.getElementById("bid-data").classList.add("active");
}

function closeNav() {
  document.getElementById("bid-data").classList.remove("active");
}


document.addEventListener("DOMContentLoaded", function () {
  // Function to format number with commas in Indian style grouping
  function formatNumber(number) {
    let numStr = number.toString().split("").reverse().join("");
    let parts = [];
    parts.push(numStr.substring(0, 3));
    for (let i = 3; i < numStr.length; i += 2) {
      parts.push(numStr.substring(i, i + 2));
    }
    return parts.join(",").split("").reverse().join("");
  }

  const rangeInput = document.getElementById("bidRange");
  const rangeValueDisplay = document.getElementById("rangeValueDisplay");
  const inputNumber = document.getElementById("bidNumber");
  const initialBidAmountInput = document.getElementById("initialBidAmount");

  // Retrieve initial value from hidden input
  let initialValueStr = initialBidAmountInput.value.trim();
  console.log("Initial Value String from hidden input:", initialValueStr);

  // Parse the initial value as a float
  let initialValue = parseFloat(initialValueStr.replace(",", ""));
  console.log("Parsed Initial Value:", initialValue);

  if (!isNaN(initialValue)) {
    // Set initial values for range and number inputs
    rangeInput.min = initialValue;
    rangeInput.value = initialValue;
    rangeValueDisplay.textContent = formatNumber(initialValue);
    inputNumber.value = initialValue;

    // Update range value display and number input display when range input changes
    rangeInput.addEventListener("input", function () {
      let currentValue = parseFloat(rangeInput.value);
      rangeValueDisplay.textContent = formatNumber(currentValue);
      inputNumber.value = currentValue;
    });

    // Update range input and number input when number input changes
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
});

document.addEventListener('DOMContentLoaded', function () {
  const rangeInput = document.getElementById('bidRange');
  updateBackground(rangeInput);

  rangeInput.addEventListener('input', function () {
    updateBackground(rangeInput);
  });

  function updateBackground(element) {
    const min = element.min;
    const max = element.max;
    const val = element.value;
    const percentage = ((val - min) / (max - min)) * 100;
    // element.style.background = `linear-gradient(to right, #4CAF50 ${percentage}%, #ddd ${percentage}%)`;
    element.style.background = `linear-gradient(to right, #931a25 ${percentage}%, #0d1282 ${percentage}%)`;
  }
});



// Toggle Comments Text

// Comment Toggle
document.addEventListener("DOMContentLoaded", function () {
  const comments = document.querySelectorAll(".comment-message");

  comments.forEach(comment => {
    const commentText = comment.querySelector(".comment-text");
    const commentToggle = comment.querySelector(".comment-toggle");

    // Temporarily set to normal to measure
    commentText.style.whiteSpace = 'normal';
    commentText.style.whiteSpace = 'nowrap';

    console.log("C T Scroll Width: ", commentText.scrollWidth);
    console.log("C T Client Width: ", commentText.clientWidth);
    const isOverflowingWidth = commentText.scrollWidth > commentText.clientWidth;
    console.log("OverflowingWidth :", isOverflowingWidth);

    if (isOverflowingWidth) {
      commentToggle.innerHTML = "See full comment";
      commentToggle.style.display = "block"; // Show the toggle
    }

    // Toggle full text on click
    commentToggle.addEventListener("click", function () {
      if (commentText.style.whiteSpace === "nowrap") {
        commentText.style.whiteSpace = "normal";
        this.textContent = "show less";
        commentText.style.maxHeight = "max-content";
      } else {
        commentText.style.whiteSpace = "nowrap";
        this.textContent = "See full comment";
        commentText.style.maxHeight = "max-content";
      }
    });
  });
});

// Text-Area Full Mode Toggling

document.addEventListener('DOMContentLoaded', (event) => {
  const textarea = document.querySelector('.new-comment');

  // Adjust the height of the textarea on input
  textarea.addEventListener('input', adjustTextareaHeight);

  // Submit the form on Enter key press
  textarea.addEventListener('keypress', function (event) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      document.getElementById('comment-form').submit();
    }
  });

  function adjustTextareaHeight() {
    console.log("TextArea height: ", textarea.style.height);
    console.log("Text Area Scroll Height:", textarea.scrollHeight);
    textarea.style.height = 'auto';  // Reset the height
    textarea.style.height = textarea.scrollHeight + 'px';  // Set it to the scroll height
  }
});

//  Reply
document.addEventListener("DOMContentLoaded", function () {
  // Function to close all reply forms except the current one
  function closeOtherReplyFormsExceptCurrent(currentForm) {
    document.querySelectorAll(".reply-form").forEach(function (form) {
      if (form !== currentForm) {
        form.remove();
      }
    });
  }

  // Event listener for "Reply" buttons
  document.querySelectorAll(".reply-btn").forEach(function (button) {
    button.addEventListener("click", function () {
      console.log("Drunken Alone");
      const commentId = button.getAttribute("data-comment-id");
      const replyId = button.getAttribute("data-reply-id");
      const listingId = button.getAttribute("data-listing-id");
      const username = button.getAttribute("data-username");
      const listingName = button.getAttribute("data-name");

      console.log("Reply button clicked:", commentId, replyId, listingId, username, listingName); // Log button click details

      const placeholderText = username ? `Reply to @${username}` : "RE";

      // Check if a reply form already exists for this comment or reply
      const existingForm = button.parentElement.querySelector(".reply-form");
      if (existingForm) {
        existingForm.querySelector('input[name="newComment"]').focus();
        return;
      }

      // Close other reply forms before opening the current one
      closeOtherReplyFormsExceptCurrent(null);
      // Create reply form
      const replyForm = document.createElement("form");
      replyForm.method = "POST";
      const listingNameEncoded = encodeURIComponent(listingName);
      replyForm.action = `/add_comment/${listingNameEncoded}/`;
      replyForm.className = "reply-form";

      const csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

      replyForm.innerHTML = `
                 <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                 <input type="text" name="newComment" class="reply-input" placeholder="${placeholderText}" required>
                 <input type="hidden" name="parent_id" value="${replyId || commentId}">
                 <button type="submit" class="reply-btn"><i class="fa-solid fa-paper-plane reply-send-icon"></i></button>
             `;

      // Append the reply form to the parent element
      button.parentElement.appendChild(replyForm);

      // Close reply form if clicked outside or on another "Reply" button
      const closeReplyFormHandler = function (event) {
        if (
          !replyForm.contains(event.target) &&
          !button.contains(event.target)
        ) {
          replyForm.remove();
          document.removeEventListener("click", closeReplyFormHandler);
        }
      };

      document.addEventListener("click", closeReplyFormHandler);
    });
  });
});




document.addEventListener("DOMContentLoaded", function () {
  // Function to update the button text for replies
  function updateRepliesButtonText(commentId) {
    const repliesDiv = document.querySelector(`.replies[data-comment-id="${commentId}"]`);
    if (!repliesDiv) return;  // Check if repliesDiv exists

    const hiddenReplies = repliesDiv.querySelectorAll('.reply-item[style*="display: none"]');
    const allReplies = repliesDiv.querySelectorAll('.reply-item');
    const toggleBtn = document.querySelector(`.toggle-replies-btn[data-comment-id="${commentId}"]`);
    if (!toggleBtn) return;  // Check if toggleBtn exists

    const hiddenCount = hiddenReplies.length;
    const allRepliesCount = allReplies.length;

    if (allRepliesCount <= 2) {
      toggleBtn.textContent = "";
    } else if (hiddenCount > 0) {
      // toggleBtn.textContent = `See ${hiddenCount} more ${hiddenCount > 1 ? 'replies' : 'reply'}`;
      toggleBtn.innerHTML = `${hiddenCount > 1 ? 'Replies' : 'Reply'}<sup>${allRepliesCount}</sup> `;
    } else {
      toggleBtn.textContent = `Hide ${allRepliesCount > 1 ? 'Replies' : 'Reply'}`;
    }
  }

  // Function to toggle replies visibility
  function toggleReplies(event) {
    const commentId = event.target.getAttribute("data-comment-id");
    const repliesDiv = document.querySelector(`.replies[data-comment-id="${commentId}"]`);
    if (!repliesDiv) return;  // Check if repliesDiv exists

    const hiddenReplies = repliesDiv.querySelectorAll('.reply-item[style*="display: none"]');
    const allReplies = repliesDiv.querySelectorAll('.reply-item');

    if (hiddenReplies.length > 0) {
      // Some replies are hidden, show all
      hiddenReplies.forEach(reply => {
        reply.style.display = "flex";
      });
      event.target.textContent = `Hide ${allReplies.length - 2} ${allReplies.length - 2 > 1 ? 'replies' : 'reply'}`;
    } else {
      // All replies are visible, hide beyond the first two
      if (allReplies.length > 2) {
        repliesDiv.querySelectorAll(".reply-item:nth-child(n+3)").forEach(reply => {
          reply.style.display = "none";
        });
      }
      event.target.textContent = `Show ${allReplies.length - 2} more ${allReplies.length - 2 > 1 ? 'replies' : 'reply'}`;
    }

    updateRepliesButtonText(commentId);
  }

  // Add click event listeners to all toggle-replies buttons
  document.querySelectorAll(".toggle-replies-btn").forEach((button) => {
    button.addEventListener("click", toggleReplies);
  });

  // Initially hide replies beyond the first two and update button text
  document.querySelectorAll(".replies").forEach((repliesDiv) => {
    const commentId = repliesDiv.getAttribute("data-comment-id");
    if (!commentId) return;  // Check if commentId exists

    repliesDiv.querySelectorAll(".reply-item:nth-child(n+3)").forEach((reply) => {
      reply.style.display = "none";
    });
    updateRepliesButtonText(commentId);
  });
});

document.addEventListener("DOMContentLoaded", function () {

  // Function to update the text of the load more button based on comment visibility
  function updateButtonText() {
    const allComments = document.querySelectorAll(".comment-item");
    const allCommentsCount = allComments.length;
    const hiddenComments = document.querySelectorAll('.comment-item[style*="display: none"]');
    const hiddenCount = hiddenComments.length;
    const loadMoreBtn = document.getElementById("load-more-btn");

    // Update button text based on the number of comments and their visibility
    if (allCommentsCount === 0) {
      loadMoreBtn.textContent = "No comments";
    } else if (allCommentsCount <= 2) {
      loadMoreBtn.textContent = " ";
    } else if (hiddenCount > 0) {
      loadMoreBtn.textContent = `See ${hiddenCount} more ${hiddenCount > 1 ? 'comments' : 'comment'}`;
    } else {
      loadMoreBtn.textContent = `Hide ${(allCommentsCount - 2) > 1 ? 'comments' : 'comment'}`;
    }
  }

  // Function to toggle visibility of comments
  function toggleComments(event) {
    const allComments = document.querySelectorAll(".comment-item");
    const hiddenComments = document.querySelectorAll('.comment-item[style*="display: none"]');

    // Toggle comments visibility based on current state
    if (hiddenComments.length > 0) {
      // Some comments are hidden, show all
      hiddenComments.forEach(comment => {
        comment.style.display = "flex";
      });
      event.target.textContent = "Hide comments";
    } else {
      // All comments are visible, hide beyond the first two
      if (allComments.length > 2) {
        allComments.forEach((comment, index) => {
          if (index >= 2) {
            comment.style.display = "none";
          }
        });
      }
      event.target.textContent = `See ${allComments.length - 2} more ${allComments.length - 2 > 1 ? 'comments' : 'comment'}`;
    }
    updateButtonText(); // Update button text after toggling comments
  }

  // Function to handle deletion of comments
  function handleDelete() {
    const commentItem = this.closest(".comment-item");
    if (commentItem) {
      commentItem.remove(); // Remove the comment item from DOM
      updateButtonText(); // Update button text after comment deletion
    }
  }

  // Function to add event listeners to delete buttons
  function addDeleteEventListeners() {
    const deleteButtons = document.querySelectorAll(".delete-button");
    deleteButtons.forEach(button => {
      button.addEventListener("click", handleDelete); // Add click event listener for each delete button
    });
  }

  // Initial setup when the DOM content is loaded
  const loadMoreBtn = document.getElementById("load-more-btn");
  if (loadMoreBtn) {
    loadMoreBtn.addEventListener("click", toggleComments); // Add click event listener for load more button
  }

  // Hide comments beyond the first two initially
  const allComments = document.querySelectorAll(".comment-item");
  if (allComments.length > 2) {
    allComments.forEach((comment, index) => {
      if (index >= 2) {
        comment.style.display = "none";
      }
    });
  }

  addDeleteEventListeners(); // Add event listeners to delete buttons
  updateButtonText(); // Initial update of button text based on comment visibility
});

// Like Logic
// Add click event listeners to all like icons
document.addEventListener("DOMContentLoaded", function () {
  const likeIcons = document.querySelectorAll('.like-icon');

  // Handle like icon click
  if (likeIcons) {
    likeIcons.forEach((icon) => {
      icon.addEventListener("click", function () {
        if (icon.classList.contains('fa-regular')) {
          console.log("hi");
          icon.classList.remove("fa-regular");
          icon.classList.add("fa-solid");
        } else if (icon.classList.contains('fa-solid')) {
          icon.classList.remove("fa-solid");
          icon.classList.add("fa-regular");
          console.log("bye");
        }
      });
    });
  } else {
    console.error("Element with id 'like-icon' not found");
  }
});


// Update the timer every second
document.addEventListener("DOMContentLoaded", function () {
  function updateTimer() {
    let timerElement = document.getElementById("timer");
    let endTimeString = timerElement.getAttribute("data-end-time");
    let endTime = new Date(endTimeString).getTime();
    let now = new Date().getTime();
    let timeRemaining = endTime - now;

    if (timeRemaining <= 0) {
      timerElement.innerHTML = "Auction Closed";
      clearInterval(timerInterval);
      return;
    }

    // Calculate time components
    let days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    let hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);

    // Construct the countdown message based on the remaining time components
    if (days > 0) {
      timerElement.innerHTML = `Auction Ends In: ${days} d ${hours} h ${minutes} m ${seconds} s`;
    } else if (hours > 0) {
      timerElement.innerHTML = `Auction Ends In: ${hours} h ${minutes} m ${seconds} s`;
    } else if (minutes > 0) {
      timerElement.innerHTML = `Auction Ends In: ${minutes} m ${seconds} s`;
    } else {
      timerElement.innerHTML = `Auction Ends In: ${seconds} s`;
    }
  }

  let timerInterval = setInterval(updateTimer, 1000);
  updateTimer();
});

// Toggle To See Full Bid Details
document.addEventListener("DOMContentLoaded", function () {
  const toggleButtons = document.querySelectorAll('.toggle-details');

  toggleButtons.forEach(button => {
    button.addEventListener('click', function () {
      const bidDetails = this.nextElementSibling;

      if (bidDetails.style.display === "none" || bidDetails.style.display === "") {
        bidDetails.style.display = "block"; // Show the details
      } else {
        bidDetails.style.display = "none"; // Hide the details
      }
    });
  });
});