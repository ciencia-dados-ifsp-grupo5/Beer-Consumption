const API_URL = '/api/model/predict';

const serializeForm = function (form) {
  const obj = {};
  const formData = new FormData(form);
  for (let key of formData.keys()) {
    obj[key] = formData.get(key);
  }
  return obj;
};

document
  .querySelector('#formParams')
  .addEventListener('submit', function (event) {
    event.preventDefault();

    predResults = document.querySelector('#predResults');
    predValue = document.querySelector('#predValue');
    predLoading = document.querySelector('#predLoading');

    predResults.classList.remove('d-none');
    predValue.classList.add('d-none');
    predLoading.classList.remove('d-none');

    fetch(API_URL, {
      method: 'POST',
      body: JSON.stringify(serializeForm(event.target)),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
      .then((response) => {
        if (response.ok) {
          return response.json();
        }
        return Promise.reject(response);
      })
      .then((predictions) => {
        console.log(predictions);
        predValue.textContent =
          Number.parseFloat(predictions.prediction[0]).toFixed(2) + ' litros';
        predValue.classList.remove('d-none');
        predLoading.classList.add('d-none');
      })
      .catch((error) => {
        console.error(error);
      });
  });
