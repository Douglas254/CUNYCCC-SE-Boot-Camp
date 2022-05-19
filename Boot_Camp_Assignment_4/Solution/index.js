// **********Part A Solution**********

const personA = "Lucas";
const personB = "Peter";
let personAmass = 78;
let personAheight = 1.69;

let personBmass = 92;
let personBheight = 1.95;

const lucasBodyMassIndexBMI = Math.round(
  personAmass / (personAheight * personAheight)
).toFixed(1);
const peterBodyMassIndexBMI = Math.round(
  personBmass / (personBheight * personBheight)
).toFixed(1);
const higherBMI = Boolean(lucasBodyMassIndexBMI > peterBodyMassIndexBMI);

if (lucasBodyMassIndexBMI > peterBodyMassIndexBMI) {
  console.log("***Part A Quiz Output***");
  console.log(
    `The BMI of ${personB} is ${peterBodyMassIndexBMI} The BMI of ${personA} is ${lucasBodyMassIndexBMI} ${personA}' BMI is higher than ${personB}'s BMI that is ${higherBMI}`
  );
}

// **********Part B Solution**********
let celsiusTemperature = 100;
let fahrenheitTemperature = 200;
const deg = "\xB0";
const fahrenheitFormula = Math.round(celsiusTemperature * 1.8 + 32).toFixed(1);
const celsiusFormula = Math.round((fahrenheitTemperature - 32) / 1.8).toFixed(
  1
);

console.log("***Part B Quiz Output***");
console.log(
  `${celsiusTemperature}${deg}C is ${fahrenheitFormula}${deg}F and ${fahrenheitTemperature}${deg}F is ${celsiusFormula}${deg}C`
);

// **********Part C Solution**********
// 1st part using ternary operator
var higherBodyMassIndex =
  lucasBodyMassIndexBMI > peterBodyMassIndexBMI
    ? "Lucas BMI is higher than Peter's!"
    : "peter's BMI is higher than Lucas'!";
console.log("***Part C Quiz Output***");

console.log(higherBodyMassIndex);

// 2nd part using if else statement
if (lucasBodyMassIndexBMI > peterBodyMassIndexBMI) {
  console.log("***Part C Quiz Output***");
  console.log(
    `Lucas BMI (${lucasBodyMassIndexBMI}) is higher than Peter's (${peterBodyMassIndexBMI})!`
  );
} else {
  console.log("***Part C Quiz Output***");
  console.log("peter's BMI is higher than Lucas'!");
}

// **********Part D Solution**********
var ConvertCelsiusToFahrenheit = (celsiusTemperature) => {
  result = Math.round(celsiusTemperature * 1.8 + 32).toFixed(1);
  console.log("***Part D Quiz Output***");
  console.log(`${celsiusTemperature}${deg}C is ${result}${deg}F`);
};

// calling the function
ConvertCelsiusToFahrenheit(100);

var ConvertFahrenheitToCelsius = (fahrenheitTemperature) => {
  result = Math.round((fahrenheitTemperature - 32) / 1.8).toFixed(1);
  console.log(`${fahrenheitTemperature}${deg}F is ${result}${deg}C`);
};

// calling the function
ConvertFahrenheitToCelsius(32);
ConvertFahrenheitToCelsius(10);
ConvertFahrenheitToCelsius(102);
