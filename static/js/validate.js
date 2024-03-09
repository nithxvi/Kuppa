document.getElementById('credentialForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting

    const email = document.getElementById('email').value;
    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;


    if (password1.value !== password2.value) {
        alert('Passwords do not match.');
        return;
    }
    // Email validatione
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Password validation
    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passwordRegex.test(password1)) {
        alert('Please enter a strong password. It should contain at least 8 characters, one uppercase letter, one lowercase letter, one number, and one special character.');
        return;
    }

    // If both validations pass, you can proceed with form submission or further processing
    alert('Credentials are valid!');
    // this.submit();
});
