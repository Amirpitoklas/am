<?php
include 'config.php';

if(isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = md5($_POST['password']); // лучше password_hash в реальном проекте

    $query = "SELECT * FROM user WHERE username='$username' AND password='$password'";
    $result = mysqli_query($conn, $query);
    
    if(mysqli_num_rows($result) > 0) {
        $data = mysqli_fetch_assoc($result);
        $_SESSION['username'] = $data['username'];
        $_SESSION['role'] = $data['role'];
        header("Location: home.php");
    } else {
        echo "<script>alert('Login gagal!');</script>";
    }
}
?>
<!-- HTML форма входа -->
