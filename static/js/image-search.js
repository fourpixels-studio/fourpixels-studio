const accessKey = "5DxWXKgd_4whA5Jf4-05zwSO4etpR45cKrcYgZSrulA";
const searchForm = document.getElementById("search-form");
const searchBox = document.getElementById("search-box");
const searchResult = document.getElementById("search-result");
const showMoreBtn = document.getElementById("show-more-btn");
const searchQueryDisplay = document.getElementById("search-query-display");
let keyword = "";
let page = 1;

// Search images async function returns a promise
async function searchImages() {
  // Get the keyword(s) from the user input
  keyword = searchBox.value;
  const url = `https://api.unsplash.com/search/photos?page=${page}&query=${keyword}&client_id=${accessKey}&per_page=12`;
  // Convert the response in json
  const response = await fetch(url);
  const data = await response.json();
  // Condiditon to check if there are already results on the page, if false, setup the first page of results
  if (page === 1) {
    searchResult.innerHTML = "";
  }
  const results = data.results;
  // Return the new array of images and map them accordingly
  results.map((result) => {
    const image = document.createElement("img");
    image.src = result.urls.small;
    // Get the link of the result and open a new page when the user clicks on it
    const imageLink = document.createElement("a");
    imageLink.href = result.links.html;
    imageLink.target = "_blank";
    // Append the image object in the Search Result container
    imageLink.appendChild(image);
    searchResult.appendChild(imageLink);
  });
  // Show button displays after (12) images are retrieved
  showMoreBtn.style.display = "block";
  // Update the content of the search query display element
  searchQueryDisplay.textContent = `Showing "${keyword}" results`;
  // Capitalize the first letter of the keyword
  const capitalizedKeyword = keyword.charAt(0).toUpperCase() + keyword.slice(1);

  // Update meta title and description based on user queries
  const metaTitle = `Four Pixels - ${capitalizedKeyword} images`;
  document.title = metaTitle;
  main.style.height = "100%";
}

// Query search event listener function
searchForm.addEventListener("submit", (e) => {
  e.preventDefault();
  page = 1;
  searchImages();
});

// Show more results function
showMoreBtn.addEventListener("click", () => {
  page++;
  searchImages();
});
