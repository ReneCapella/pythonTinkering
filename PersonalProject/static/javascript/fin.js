( function(win, doc) {
    var audioPlayer = doc.getElementById("audiofile");
    var subtitles = doc.getElementById("subtitles");
    var body = doc.body;
    body.style.backgroundColor = '#005bbc';

    var syncData =
    createSubtitle();

    function createSubtitle()
    {
        var element;
        for (var i = 0; i < doc.syncData.length; i++) {
            element = doc.createElement('span');
            element.setAttribute("id", "c_" + i);
            element.innerText = doc.syncData[i].text + " ";
            subtitles.appendChild(element);
        }
    }

    audioPlayer.addEventListener("timeupdate", function(e){
        doc.syncData.forEach(function(element, index, array){
            // subtitles.children[index].style.color = '#005bbc';
            if( audioPlayer.currentTime >= element.start && audioPlayer.currentTime <= element.end )
                subtitles.children[index].style.color = '#ffd600';
        });
    });
}(window, document));
