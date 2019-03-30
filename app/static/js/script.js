function gameRefresh() {
    $.getJSON('/status',{})
    .done(json => {
        let gameName = json["name"];
        let player = json["player"];
        let turn = json["turn"];
        $('#gameInfo').empty();
        $('#gameInfo').append(`
                               <h1>It is ${player}'s turn</h1>
                               <p>in ${gameName} turn: #${turn}</p>
                              `);
    });
};

$(document).ready(function () {
    //console.log("scripts.js loaded");
    gameRefresh();
});
