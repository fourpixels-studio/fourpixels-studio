document.addEventListener("DOMContentLoaded", () => {
    const thumbnails = document.querySelectorAll(".project-media-image-thumbnail");
    const modal = new bootstrap.Modal(document.getElementById("imageModal"));
    const modalImage = document.getElementById("modalImage");
    const modalName = document.getElementById("modalImageName");
    const modalDescription = document.getElementById("modalImageDescription");
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    const indicatorContainer = document.getElementById("carouselIndicators");
    let touchStartX = 0;
    let touchEndX = 0;
    let scale = 1;
    let initialDistance = 0;

    let currentIndex = 0;
    const images = Array.from(thumbnails).map(img => ({
        src: img.getAttribute("data-image-url"),
        name: img.getAttribute("data-image-name"),
        description: img.getAttribute("data-image-description")
    }));

    // Open Modal
    thumbnails.forEach((thumbnail, index) => {
        thumbnail.addEventListener("click", () => {
            currentIndex = index;
            updateModalImage();
            modal.show();
        });
    });

    // Navigate Images
    prevButton.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateModalImage();
    });

    nextButton.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateModalImage();
    });

    // Update Modal Image, Name, Description
    function updateModalImage() {
        const current = images[currentIndex];
        modalImage.src = current.src;
        modalName.textContent = current.name || "Untitled";
        modalDescription.textContent = current.description || "";
        renderDots();
    }

    // Swipe Support
    modalImage.addEventListener("touchstart", (e) => {
        touchStartX = e.changedTouches[0].screenX;
    });

    modalImage.addEventListener("touchend", (e) => {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
    });

    function handleSwipe() {
        const swipeThreshold = 100; // minimum swipe distance in px
        const swipeDistance = touchEndX - touchStartX;

        if (swipeDistance > swipeThreshold) {
            prevButton.click();
        } else if (swipeDistance < -swipeThreshold) {
            nextButton.click();
        }
    }

    function renderDots() {
        indicatorContainer.innerHTML = "";
        images.forEach((_, i) => {
            const dot = document.createElement("div");
            dot.classList.add("carousel-dot");
            if (i === currentIndex) dot.classList.add("active");
            indicatorContainer.appendChild(dot);
        });
    }
    
    function updateModalImage() {
        modalImage.src = images[currentIndex];
        renderDots();
    }

    modalImage.addEventListener("touchmove", (e) => {
        if (e.touches.length === 2) {
            e.preventDefault();

            const touch1 = e.touches[0];
            const touch2 = e.touches[1];
            const currentDistance = Math.hypot(
                touch2.pageX - touch1.pageX,
                touch2.pageY - touch1.pageY
            );

            if (!initialDistance) {
                initialDistance = currentDistance;
            } else {
                scale = currentDistance / initialDistance;
                modalImage.style.transform = `scale(${scale})`;
            }
        }
    }, { passive: false });

    modalImage.addEventListener("touchend", () => {
        initialDistance = 0;

        if (scale < 1) {
            scale = 1;
            modalImage.style.transform = `scale(1)`;
        }
    });
});