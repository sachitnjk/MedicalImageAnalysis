//get necessary elements
//Sign IN
const signincontainer = document.querySelector(".signin-container");
const loginSubmitButton = document.querySelector(".login-submit");
const userNameInput = document.querySelector("#username");
const passwordInput = document.querySelector("#password");
const cancelButton = document.querySelector(".cancelbtn");
const signin = document.querySelector(".signin");



//Sign UP
const signupcontainer = document.querySelector(".signup-container");
const signupSubmitButton = document.querySelector(".submitbtn");
const signupCancel = document.querySelector(".signupcancel");

//BloodAnalysis
const bloodAnalysisContainer = document.querySelector(".BloodAnalysis-container");
const bloodAnalysisButton = document.querySelector(".Blood-Analysis-btn");
const closePopupBloodAnalysis = document.querySelector(".closePopup-BloodAnalysis");

//BreastAnalysis
const breastAnalysisContainer = document.querySelector(".BreastAnalysis-container");
const breastAnalysisButton = document.querySelector(".Breast-Analysis-btn");
const closePopupBreastAnalysis = document.querySelector(".closePopup-BreastAnalysis");

function breastAnalysisBoxHandler(event)
{
    breastAnalysisContainer.style.display = "block";
}

function bloodAnalysisBoxHandler(event)
{
    bloodAnalysisContainer.style.display = "block";
}

function closePopupHandlerBloodAnalysis(event)
{
    bloodAnalysisContainer.style.display = "none";
}

function closePopupHandlerBreastAnalysis(event)
{
    breastAnalysisContainer.style.display = "none";
}

function signinHandler(event){
    signincontainer.style.display = "block";
}

function signupHandler(event){
    signupcontainer.style.display = "block";
}


function loginSubmitHandler(event) {
    let userid = userNameInput.value;
    let password = passwordInput.value;
    console.log("user " + userid + " has logged in");
    signincontainer.style.display = "none";
}


function cancelHandler(event) {
    signincontainer.style.display = "none";
    
}


function signupCancelHandler(event) {
    signupcontainer.style.display = "none";
    
}


function signupSubmitHandler(event) {
    signupcontainer.style.display = "none";
}




bloodAnalysisButton.addEventListener("click", bloodAnalysisBoxHandler);
closePopupBloodAnalysis.addEventListener("click", closePopupHandlerBloodAnalysis);
breastAnalysisButton.addEventListener("click", breastAnalysisBoxHandler);
closePopupBreastAnalysis.addEventListener("click", closePopupHandlerBreastAnalysis);


signin.addEventListener("click",signinHandler);

const signup=document.querySelector(".signup");
signup.addEventListener("click",signupHandler);

signupSubmitButton.addEventListener("click",signupSubmitHandler);

loginSubmitButton.addEventListener("click",loginSubmitHandler);

cancelButton.addEventListener("click",cancelHandler);

signupCancel.addEventListener("click",signupCancelHandler);





