document.addEventListener("DOMContentLoaded", function() {
    // Анимация заголовка
    const title = document.querySelector('.title');
    title.style.opacity = 0;
    setTimeout(() => {
        title.style.transition = "opacity 2s";
        title.style.opacity = 1;
    }, 500);

    // Анимация кнопки "ВЫБРАТЬ"
    const button = document.querySelector('.select-button');
    button.style.transform = "scale(0)";
    setTimeout(() => {
        button.style.transition = "transform 1s";
        button.style.transform = "scale(1)";
    }, 1000);

    // Анимация надписи "Я люблю Настю"
    const loveText = document.querySelector('.love');
    loveText.style.opacity = 0;
    setTimeout(() => {
        loveText.style.transition = "opacity 2s";
        loveText.style.opacity = 1;
    }, 1500);

    // Показ картинки и конфетти
    const pictureContainer = document.querySelector('.picture-container');
    const confetti = document.querySelector('.confetti');
    pictureContainer.style.opacity = 0;
    confetti.style.opacity = 0;

    setTimeout(() => {
        pictureContainer.style.transition = "opacity 2s";
        pictureContainer.style.opacity = 1;
        confetti.style.transition = "opacity 2s";
        confetti.style.opacity = 1;
    }, 500);
});
