const form = document.querySelector("#form-habits")
const nlwSetup = new NLWSetup(form)
const button = document.querySelector(".tracker-button")

button.addEventListener("click", add)
form.addEventListener("change", save)

function add() {
  const today = new Date().toLocaleDateString("pt-br").slice(0, -5)
  const dayExists = nlwSetup.dayExists(today)

  if (dayExists) {
    alert("Dia já incluso ¯\_(ツ)_/¯")
    return
  }

  alert("Dia adicionado (〜￣▽￣)〜")
  nlwSetup.addDay(today)
}


function getCookie(name) {
  const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
  return cookieValue ? cookieValue.pop() : '';
}

function save() {
  const trackerData = JSON.stringify(nlwSetup.data);

  fetch('save_tracker_data/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-CSRFToken': getCookie('csrftoken'),  // assuming you're using Django's CSRF protection
    },
    body: `tracker_data=${encodeURIComponent(trackerData)}`,
  })
    .then(response => response.json())
    .then(data => {
      console.log(data.message);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}
/** 
 * Função  save() antiga, salvava no localstorage.

function save() {
  localStorage.setItem("HabitsApp@habits", JSON.stringify(nlwSetup.data))
}
*/

fetch('load_tracker_data/')
  .then(response => response.json())
  .then(data => {
    const trackerdata = JSON.parse(data) || {};  // Assuming the response JSON has a property 'tracker_data'

    nlwSetup.setData(trackerdata);
    nlwSetup.load();
  })
  .catch(error => {
    console.error('Error:', error);
  });



/**função load antiga, carregava do localstorage 
const data = JSON.parse(localStorage.getItem("HabitsApp@habits")) || {}
nlwSetup.setData(data)
nlwSetup.load()
*/