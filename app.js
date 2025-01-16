// Basit bir kullanıcı doğrulama örneği
const users = {
    admin: 'password123'
};

// GET: Login Sayfası
exports.getLogin = (req, res) => {
    res.render('login');
};

// POST: Login İşlemi
exports.postLogin = (req, res) => {
    const { username, password } = req.body;

    if (users[username] && users[username] === password) {
        req.session.user = username;
        res.redirect('/dashboard');
    } else {
        res.redirect('/login');
    }
};

// GET: Dashboard Sayfası
exports.getDashboard = (req, res) => {
    if (req.session.user) {
        res.render('dashboard', { username: req.session.user });
    } else {
        res.redirect('/login');
    }
};

// GET: Logout İşlemi
exports.logout = (req, res) => {
    req.session.destroy(() => {
        res.redirect('/login');
    });
};

