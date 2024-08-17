function clearDisplay() {
    document.getElementById("result").value = "";
}

function appendNumber(number) {
    document.getElementById("result").value += number;
}

function appendOperator(operator) {
    let display = document.getElementById("result").value;
    if (display !== "") {
        document.getElementById("result").value += operator;
    }
}

function calculateResult() {
    let display = document.getElementById("result").value;
    try {
        document.getElementById("result").value = eval(display);
    } catch (e) {
        document.getElementById("result").value = "Error";
    }
}
