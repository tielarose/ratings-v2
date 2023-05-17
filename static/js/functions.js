const handleRatingForm = (evt) => {
  evt.preventDefault();

  const rating = { rating: document.querySelector("#user_rating").value };
  const movie_id = fetch(`/rate/${movie_id // window.location.href
    }`); // https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
};

document
  .querySelector("#rating_form")
  .addEventListener("submit", handleRatingForm);
