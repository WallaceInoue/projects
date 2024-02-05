const questions = [
    {
        question: "Which is the largest animal in world",
        answers:[
            {text: "Shark", correct:false},
            {text: "Elephant", correct:false},
            {text: "Blue whale", correct:true},
            {text: "Giraffe", correct:false},
        ]
    },
    {
        question: "Which is the smallest country in world",
        answers:[
            {text: "Vatican City", correct:true},
            {text: "Bhutan", correct:false},
            {text: "Nepal", correct:false},
            {text: "Shri Lanka", correct:false},
        ]
    },
    {
        question: "Which is the largest desert in world",
        answers:[
            {text: "Kalahari", correct:false},
            {text: "Gobi", correct:false},
            {text: "Sahara", correct:false},
            {text: "Giraffe", correct:true},
        ]
    },
    {
        question: "Which is the smallest continent in world",
        answers:[
            {text: "Asia", correct:false},
            {text: "Australia", correct:true},
            {text: "Arctic", correct:false},
            {text: "Africa", correct:false},
        ]
    },
];

const questionElement = document.getElementById("question");
const answerButtons = document.getElementById("answer-buttons");
const nextButton = document.getElementById("next-btn");

let currentQuestionIndex = 0;
let score = 0;

function startQuiz(){
     currentQuestionIndex = 0;
     score = 0;
     nextButton.innerHTML = "Next";
     showQuestion();

}
function showQuestion(){
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex + 1;
    questionElement.innerHTML = questionNo + ". " + currentQuestion.question;

    currentQuestion.answers.forEach(answer => {
        const button = document.createElement("button");
        button.innerHTML = answer.text;
        button.classList.add("btn");
        answerButtons.appendChild(button);
    });
}
function resetState(){
    nextButton.style.display = "none";
    while(answerButtons.firstChild){
        answerButtons.removeChild(answerButtons.firstChild);
    }
}
startQuiz();