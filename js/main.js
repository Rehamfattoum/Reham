document.addEventListener("DOMContentLoaded", function () {
    let counter = 0;
    function count() {
      counter++;
      document.querySelector("#counter").innerHTML = counter;
    }
    document.querySelector("#btnCounter").onclick = count;
    function change() {
      const heading = document.querySelector("#change");
      if (heading.innerHTML === "Hello!") {
        document.querySelector("#change").innerHTML = "GoodBye!";
      } else {
        document.querySelector("#change").innerHTML = "Hello!";
      }
    }
    document.querySelector("#btnChange").onclick = change;
    document.querySelector("select").onchange = function () {
      document.querySelector("#hello").style.color = this.value;
    };
    document.querySelectorAll(".btnColor").forEach(function (button) {
      button.onclick = function () {
        document.querySelector("#helloWorld").style.color =
          button.dataset.color;
      };
    });

    document.querySelector("#enterName").onsubmit = function () {
      let name = document.querySelector("#getName").value;
      document.querySelector("#sayHello").innerHTML = `Hello, ${name}`;
      return false;
    };
    const newTask = document.querySelector("#task");
    const submit = document.querySelector("#submit");
    submit.disabled = true;
    newTask.onkeyup = () => {
      if (newTask.value.length > 0) {
        submit.disabled = false;
      } else {
        submit.disabled = true;
      }
    };

    document.querySelector("#formTask").onsubmit = () => {
      const task = newTask.value;
      newTask.value = "";
      let li = document.createElement("li");
      li.innerHTML = task;
      let ul = document.querySelector("#tasks");
      ul.append(li);
      submit.disabled = true;
      return false;
    };
  });
  let counter01 = 0;
  function interval() {
    counter01++;
    document.querySelector("#setInterval").innerHTML = counter01;
  }
  setInterval(interval, 1000);