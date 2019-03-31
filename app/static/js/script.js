function gameRefresh() {
    $.getJSON('/status',{})
    .done(json => {
        let gameName = json["name"];
        let player = json["player"];
        let turn = json["turn"];
        let turnTime = json["turn_time"];
        let currentTime = json["current_time"];
        $('#gameInfo').empty();
        $('#gameInfo').append(`
                               <h1>It is ${player}'s turn</h1>
                               <p>in ${gameName} turn: #${turn}</p>
                               <p>turn taken at ${turnTime}</p>
                               <p>current time: ${currentTime}</p>
                              `);
    });
};

$(document).ready(function () {
    gameRefresh();
});
