<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" type="text/css" href="C:\Users\DELL\Desktop\bot.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
</head>
<style>


 body {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
 
  font-family: Garamond;
  
}

h1 {
  text-align: center;
font-size: 40px;
text-decoration: underline;
margin-left:33%;
margin-top: 5%;
/*color: blue;*/
display: inline-block;
}
h2 {
  text-align: center;
 font-size: 35px;
 }

h3 {
  color: black;
  /*margin-bottom: 0;*/
  margin-top: 80px;
  text-align: center;
  font-size: 35px;
   color: blue;
}
.img{
  display: inline-block;

}

#chatbox {
  margin-left: auto;
  margin-right: auto;
  width: 40%;
  margin-top: 10px;
}

#userInput {
  margin-left: auto;
  margin-right: auto;
  width: 40%;
  margin-top:40px;

}

#textInput {
  width: 87%;
  border: black 40px;
  border-bottom: 3px solid #009688;
  font-family: monospace;
  font-size: 17px;
}

#buttonInput {
  padding: 3px;
  font-family: monospace;
  font-size: 17px;
}

.userText {
  color: white;
  font-family: monospace;
  font-size: 17px;
  text-align: right;
  line-height: 30px;
}

.userText span {
  background-color: #009688;
  padding: 10px;
  border-radius: 2px;
}

.botText {
  color: white;
  font-family: monospace;
  font-size: 17px;
  text-align: left;
  line-height: 40px;
}

.botText span {
  background-color: #ef5350;
  padding: 10px;
  border-radius: 2px;
}

#tidbit {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 300px;
}


.header {
  overflow: hidden;
  background-color: #f1f1f1;
  padding: 20px 10px;
}

.header a {
  float: left;
  color: black;
  text-align: center;
  padding: 12px;
  text-decoration: none;
  font-size: 18px; 
  line-height: 30px;
  border-radius: 4px;
}

.header a.logo {
  font-size: 25px;
  font-weight: bold;
}

.header a:hover {
  background-color: #ddd;
  color: black;
}

.header a.active {
  background-color: dodgerblue;
  color: white;
}

.header-right {
  float: right;
}

@media screen and (max-width: 500px) {
  .header a {
    float: none;
    display: block;
    text-align: left;
  }
  
  .header-right {
    float: none;
  }
}

</style>

<body background="https://images.all-free-download.com/images/graphicthumb/blue_abstract_background_310971.jpg">

  <div class="header">
    <img src="https://lh3.googleusercontent.com/proxy/5WQlEmS9_DoS3QrC5fqYoG7xDstHTIOpPGYvhhx1FzCwTARMDeWXZ6HN9Ud0f5GskYi_tdjwZKlNwcMUXHU3EB8qoh0Bm6ozD6033F0gdw" height="%" width="7%">
  <!-- <a href="#default" class="logo">JSPM</a> -->
  <div class="header-right">
    <a class="active" href="#home">Home</a>
    <a href="#contact">Contact</a>
    <a href="#about">About</a>
  </div>
</div>
<!-- 
<div style="padding-left:20px">
  <h1>Responsive Header</h1>
  <p>Resize the browser window to see the effect.</p>
  <p>Some content..</p>
</div> -->









     
    <img src="https://lh3.googleusercontent.com/proxy/I3pCrKcQWXcA121eHRPFsWj3nOVbXcoDNUhnId9VKEDTXR1d9SWfSAcymDSPyuYEnHo5F9p7Vh8BNMTsXzoTWfFi05Pp4eNKoTfvdoOQOQ" height=12% width=12%>
    
    <h1>JSPM's</h1>
     <img src="https://yt3.ggpht.com/a/AATXAJxpv5KFt1Cq_VJppncmaETnoQtCuDaMbhTFm2Hx=s900-c-k-c0xffffffff-no-rj-mo" height=12% width=12% align=right>

    <h2><u>Rajarshi</u> <u>shau</u> <u>college</u> <u>of</u> <u>engineering</u>,&nbsp;&nbsp;<u>Tathawade</u>,&nbsp;&nbsp;<u>Pune</u></h2>
    <h3>College Enquiry Chatbot</h3>>
    <div>
        <div id="chatbox">
            <p class="botText"><span>HellO!  How Can I Help You....
                    </span></p>
        </div>
        <div id="userInput">
            <input id="textInput" type="text" name="msg" placeholder="Type your query here...">
            <input id="buttonInput" type="submit" value="Send">
        </div>
        <script>
           
            function getBotResponse() {
                var rawText = $("#textInput").val();
                var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
                $("#textInput").val("");
                $("#chatbox").append(userHtml);
                document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
                $.get("/get", { msg: rawText }).done(function (data) {
                    var botHtml = '<p class="botText"><span>' + data + '</span></p>';
                    $("#chatbox").append(botHtml);
                    document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
                });
            }
            $("#textInput").keypress(function (e) {
                if (e.which == 13) {
                    getBotResponse();
                }
            });
            $("#buttonInput").click(function () {
                getBotResponse();
            })
        </script>
    </div>
</body>

</html>