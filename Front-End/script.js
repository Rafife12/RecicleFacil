window.onload = function () {
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
};

function showLogin() {
  document.getElementById('login-container').style.display = 'block';
  document.getElementById('forgot-password-container').style.display = 'none';
  document.getElementById('signup-container').style.display = 'none';
}

function showSignUp() {
  document.getElementById('login-container').style.display = 'none';
  document.getElementById('forgot-password-container').style.display = 'none';
  document.getElementById('signup-container').style.display = 'block';
}

function showForgotPassword() {
  document.getElementById('login-container').style.display = 'none';
  document.getElementById('forgot-password-container').style.display = 'block';
  document.getElementById('signup-container').style.display = 'none';
}

function login() {
  const username = document.getElementById('login-username').value;
  const password = document.getElementById('login-password').value;

  if (username && password) {
    alert('Login realizado com sucesso!');
  } else {
    document.getElementById('login-error').textContent = 'Usuário ou senha incorretos.';
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

function signUp() {
  const username = document.getElementById('signup-username').value;
  const password = document.getElementById('signup-password').value;

  if (username && password) {
    alert('Conta criada com sucesso! Você pode fazer login agora.');
    showLogin();
  } else {
    alert('Por favor, preencha todos os campos.');
  }
}
