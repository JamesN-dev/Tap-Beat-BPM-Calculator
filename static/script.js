// Handling keydown event to click the tap button
document.addEventListener('keydown', function(event) {
    if (event.target.id !== 'timeoutInput') {
        document.getElementById("tapButton").click();
    }
});

// Attach the input event listener to the 'timeoutInput' element
document.getElementById('timeoutInput').addEventListener('input', function(event) {
    validateNumberInput(event.target);
});

// Function to validate number input
function validateNumberInput(input) {
    const value = input.value;
    const sanitizedValue = value.replace(/[^0-9]/g, '');
    input.value = sanitizedValue;
    
    // Trigger change event
    input.dispatchEvent(new Event('change'));
}

// Check for 'Enter' key
function checkKey(event) {
    if (event.keyCode === 13) {  // 13 is the keyCode for 'Enter'
        event.preventDefault();  // Prevent the default action
        document.activeElement.blur();  // Remove focus
    }
}

// Attach a keydown event listener to handle 'Enter' specifically
document.getElementById('timeoutInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        // Using a setTimeout to defer the blur action so that it won't conflict with other events.
        setTimeout(() => event.target.blur(), 0);
    }
});
