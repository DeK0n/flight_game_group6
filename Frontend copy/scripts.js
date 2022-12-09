"use strict";
// console.log(result);

async function asynchronousFunction() {
  console.log("asynchronous download begins");
  try {
    const response = await fetch(
      "http://127.0.0.1:5000/test"
    );
    const jsonData = await response.json();
    console.log("data",jsonData);
  } catch (error) {
    console.log(error.message);
  } finally {
    // finally = this is executed anyway, whether the execution was successful or not
    console.log("asynchronous load complete");
  }
}
asynchronousFunction();

// ,{mode: "no-cors",}