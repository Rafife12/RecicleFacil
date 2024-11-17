function signUp() {
    const username = document.getElementById('signup-username').value
    const password = document.getElementById('signup-password').value

    if (username && password) {
        alert('Conta criada com sucesso! Você pode fazer login agora.')
        showLogin()
    } else {
        alert('Por favor, preencha todos os campos.')
    }
}


function recoverPassword() {
    const email = document.getElementById('forgot-email').value;
    if (email) {
        alert('Se um e-mail estiver cadastrado, um link de recuperação será enviado.');
    } else {
        alert('Por favor, digite um endereço de e-mail válido.');
    }
}

function showForgotPassword() {
    document.getElementById('login-container').style.display = 'none';
    document.getElementById('forgot-password-container').style.display = 'block';
    document.getElementById('signup-container').style.display = 'none';
}


function login() {
    const username = document.getElementById('login-username').value;
    const password = document.getElementById('login-password').value;
    const rememberPassword = document.getElementById('remember-password').checked;

    if (username && password) {
        if (rememberPassword) {
            localStorage.setItem('username', username);
            localStorage.setItem('password', password);
        } else {
            localStorage.removeItem('username');
            localStorage.removeItem('password');
        }
        alert('Login realizado com sucesso!');
    } else {
        document.getElementById('login-error').textContent = 'Usuário ou senha incorretos.';
    }
}

window.onload = function() {
    const savedUsername = localStorage.getItem('username');
    const savedPassword = localStorage.getItem('password');

    if (savedUsername && savedPassword) {
        document.getElementById('login-username').value = savedUsername;
        document.getElementById('login-password').value = savedPassword;
        document.getElementById('remember-password').checked = true;
    }

    const splashScreen = document.getElementById('splash-screen');
    const loginContainer = document.getElementById('login-container');
    const loginLogo = document.getElementById('login-logo');

    setTimeout(() => {
        splashScreen.style.opacity = '0';
        setTimeout(() => {
            splashScreen.style.display = 'none';
            loginLogo.style.display = 'flex';
            loginContainer.style.display = 'block';
        }, 500);
    }, 2000);
}