function solve() {
  let correctAnswers = 0;
  let correctQuestionsAndAnswers = {
    0: 0,
    1: 1,
    2: 0,
  };

  let allQuestionsSectionHTML = Array.from(
    document.querySelectorAll("#quizzie > section")
  );
  // console.log(allQuestionsSectionHTML);

  let resultHTML = document.querySelector("#results h1");
  // console.log(resultHTML);

  let allAnswersHTML = Array.from(document.querySelectorAll(".answer-text"));
  // console.log(allAnswersHTML);

  for (const answer of allAnswersHTML) {
    answer.addEventListener("click", answerHandler);
  }

  function answerHandler(e) {
    let answerParagraph = e.currentTarget;
    // console.log(answerParagraph);

    let questionSectionHTML =
      answerParagraph.parentElement.parentElement.parentElement.parentElement;
    // console.log(questionSectionHTML);

    let answersParagraphs = Array.from(
      questionSectionHTML.querySelectorAll("p")
    );

    let sectionIndex = allQuestionsSectionHTML.indexOf(questionSectionHTML);
    let answerIndex = answersParagraphs.indexOf(answerParagraph);

    if (correctQuestionsAndAnswers[sectionIndex] === answerIndex) {
      correctAnswers += 1;
    }
    if (sectionIndex === allQuestionsSectionHTML.length - 1) {
      allQuestionsSectionHTML[sectionIndex].style.display = "none";
      if (correctAnswers === 3) {
        resultHTML.textContent = "You are recognized as top JavaScript fan!";
      } else {
        resultHTML.textContent = `You have ${correctAnswers} right answers`;
      }
      let result = document.getElementById("results");
      result.style.display = "block";
    } else {
      allQuestionsSectionHTML[sectionIndex].style.display = "none";
      allQuestionsSectionHTML[sectionIndex + 1].style.display = "block";
    }
  }
}
