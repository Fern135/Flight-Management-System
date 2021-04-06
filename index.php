<?php 


    // checking the user information
    if(isset($_POST['login-main'])){

    }

    /***********************/
    /* make a default user */
    /***********************/
    function run_once(){
        include_once "./bin/include/conn.include.php"; // db conn


    }

?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Login</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <?php include "./bin/include/front-end-css.include.php"; ?>

    </head>
    <body id="body-login-main-css-js">



    <div class="card">
        <div class="card-header">
            <h1>
                Login
            </h1>
        </div>
        <div class="card-body">
            <form action="#" method="post">
            </form>
        </div>
        <div class="card-footer">
            <div class="footer">
                &copy; <script>document.write(new Date().getFullYear())</script>
            </div>
        </div>
    </div>
        

        <?php include "./bin/include/front-end-js.include.php"; ?>
    </body>
</html>