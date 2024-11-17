<h1>Recicle Fácil</h1> 
<p>Bem-vindo ao repositório do meu primeiro site, um projeto inovador para transformar a gestão de resíduos dedicado a tornar a coleta selecionada mais eficiente, sustentável e homologada aos Objetivos de Desenvolvimento Sustentável (ODS 12). O Recicle Fácil é pensado para cidadãos, empresas de reciclagem e orgãos governamentais.:</p>

## Índice:
- [Funcionalidades](#funcionalidades)
- [Linguagens Utilizadas](#linguagens-utilizadas)
- [Tela de Login](#tela-de-login)
- [Cadastramento de Usuário](#cadastramento-de-usuário)
- [Lembrar a senha do Usuário](#lembrar-a-senha-do-usuário)
- [Recuperar a senha do Usuário](#recuperar-a-senha-do-usuário)
- [Login](#login)
- [Contato](#contato)


## Funcionalidades:
<li>Registrar de resíduos para coleta;</li>
<li>Consultar de cronograma de coleta;</li>
<li>Localizar pontos de descarte próximos;</li>
<li>Notificar e relatar para empresas e governos</li> 
<br></br>

## Linguagens Utilizadas 

O projeto está organizado com as seguintes linguagens:

- 🔧 <strong>HTML</strong>: Estruturação da páginas, organização dos elementos do site e a base principal;</li>
- 🎨 <strong>CSS</strong>: Combinação de cores chamativas como estratégia de marketing e criação de designs atraentes;</li>
- 💡 <strong>JavaScript</strong>: Interatividade direta com o usuário ao logar, criar contas e consultar dinâmicas de cronogramas ou guias de reciclagem;</li>
- 🐍 <strong>Python</strong>: Processamento de dados e automatização das rotinas, notificações e relatórios;</li>
- 🧠 <strong>MySQL</strong>: Armazenamento de todas as informações, desde registros de resíduos, usuários até mesmo status de processamento e eficiência.</li>
  </ul>

## Tela de Login

A tela de Login foi criada com as linguagens em HTML e CSS:

- HTML:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recicle Fácil</title>
    <link rel="icon" href="c:/Users/Rafae/OneDrive/Desktop/Design Logo-Photoroom.png" type="image/png">
    <link href="https://fonts.googleapis.com/css2?family=Ultra&family=Poppins:wght@600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <div class="splash-screen" id="splash-screen">
        <img src="c:/Users/Rafae/OneDrive/Desktop/Design Logo-Photoroom.png" alt="Logo Recicle Fácil" class="splash-logo">
        <div class="site-title">Recicle Fácil</div>
    </div>

    <div class="logo-container" id="login-logo">
        <img src="c:/Users/Rafae/OneDrive/Desktop/Design Logo-Photoroom.png" alt="Logo Recicle Fácil" class="logo">
        <div class="site-title">Recicle Fácil</div>
    </div>

    <div class="container" id="login-container">
        <h2>Login</h2>
        <form id="login-form">
            <input type="text" id="login-username" class="input-field" name="username" placeholder="Usuário" required>
            <input type="password" id="login-password" class="input-field" name="password" placeholder="Senha" required>
            <div class="remember-me">
                <input type="checkbox" id="remember-password">
                <label for="remember-password">Lembrar senha</label>
            </div>
            <button type="button" class="btn-login" onclick="login()">Entrar</button>
            <div class="error-message" id="login-error"></div>
        </form>
        <div class="footer">
            <a href="javascript:void(0)" onclick="showForgotPassword()">Esqueci minha senha</a>
            <br>
            <br> 
            <a href="javascript:void(0)" onclick="showSignUp()">Cadastrar-se</a>
        </div>
    </div>

    <div class="container" id="forgot-password-container">
        <h2>Recuperar Senha</h2>
        <form id="forgot-password-form">
            <input type="email" id="forgot-email" class="input-field" name="email" placeholder="Digite seu e-mail" required>
            <button type="button" class="btn-confirm" onclick="recoverPassword()">Recuperar</button>
        </form>
        <div class="footer">
            <a href="javascript:void(0)" onclick="showLogin()">Voltar ao Login</a>
        </div>
    </div>

    <div class="container" id="signup-container">
        <h2>Cadastrar-se</h2>
        <form id="signup-form">
            <input type="text" id="signup-username" class="input-field" name="username" placeholder="Usuário" required>
            <input type="password" id="signup-password" class="input-field" name="password" placeholder="Senha" required>
            <button type="button" class="btn-confirm" onclick="signUp()">Criar Conta</button>
        </form>
        <div class="footer">
            <a href="javascript:void(0)" onclick="showLogin()">Já tem uma conta? Faça login</a>
        </div>
    </div>

    <script src="script.js"></script>

</body>
</html>
```

- CSS:

```css
.splash-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #247248;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    z-index: 1000;
    transition: opacity 0.5s ease;
}

.splash-logo {
    width: 150px;
    height: auto;
}

body {
    font-family: Arial, sans-serif;
    background-color: #247248;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.logo-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
}

.logo {
    width: 200px;
    height: auto;
    margin-bottom: 10px;
}

.site-title {
    font-family: 'Ultra', sans-serif;
    font-size: 32px;
    color: #fafafa;
    font-weight: bold;
    text-align: center;
}

.container {
    background-color: #D9D9D9;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
    display: none;
}

.input-field {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #247248;
    border-radius: 5px;
    box-sizing: border-box;
}

.input-field:focus {
    border-color: #49504C;
    outline: none;
}

.btn-login, .btn-confirm {
    width: 100%;
    padding: 10px;
    background-color: #49504C;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
}

.btn-login:hover, .btn-confirm:hover {
    background-color: #3a4040;
}

.footer {
    text-align: center;
    margin-top: 20px;
}

.footer a {
    color: #247248;
    cursor: pointer;
    text-decoration: none;
}

.footer a:hover {
    text-decoration: underline;
}

.error-message {
    color: red;
    font-size: 14px;
    margin-top: 10px;
}

.remember-me {
    display: flex;
    align-items: center;
    margin: 10px 0 20px 0;
    font-size: 14px;
}

.remember-me input {
    margin-right: 5px;
}

.forgot-password-container {
    display: none;
}

.signup-container {
    display: none;
}
```

### Cadastramento de Usuário:

Criado com o JavaScript

```JavaScript
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
```

### Lembrar a senha do usuário:

```html
<div class="remember-me">
    <input type="checkbox" id="remember-password">
    <label for="remember-password">Lembrar senha</label>
</div>
```

### Recuperar a senha do usuário:

```html
<div class="container" id="forgot-password-container">
    <h2>Recuperar Senha</h2>
    <form id="forgot-password-form">
        <input type="email" id="forgot-email" class="input-field" name="email" placeholder="Digite seu e-mail" required>
        <button type="button" class="btn-confirm" onclick="recoverPassword()">Recuperar</button>
    </form>
    <div class="footer">
        <a href="javascript:void(0)" onclick="showLogin()">Voltar ao Login</a>
    </div>
</div>
```

```javascript
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
```
### Login:

```html
<div class="container" id="login-container">
    <h2>Login</h2>
    <form id="login-form">
        <input type="text" id="login-username" class="input-field" name="username" placeholder="Usuário" required>
        <input type="password" id="login-password" class="input-field" name="password" placeholder="Senha" required>
        <div class="remember-me">
            <input type="checkbox" id="remember-password">
            <label for="remember-password">Lembrar senha</label>
        </div>
        <button type="button" class="btn-login" onclick="login()">Entrar</button>
        <div class="error-message" id="login-error"></div>
    </form>
    <div class="footer">
        <a href="javascript:void(0)" onclick="showForgotPassword()">Esqueci minha senha</a>
        <br>
        <br> 
        <a href="javascript:void(0)" onclick="showSignUp()">Cadastrar-se</a>
    </div>
</div>
```

```javascript
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
```

### Contato:

Para dúvidas e networking, só entrar em contato comigo:

- **Email:** [rafael.souzadsilva1@gmail.com](rafael.souzadsilva1@gmail.com)
- **LinkedIn:** [Rafael Silva](https://www.linkedin.com/in/rafael-silva-a5a594268/)







