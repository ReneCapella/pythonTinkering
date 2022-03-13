( function(win, doc) {
    var audioPlayer = doc.getElementById("audiofile");
    var subtitles_1 = doc.getElementById("subtitles1");
    var subtitles_2 = doc.getElementById("subtitles2");
    var body = doc.body;
    var syncData = createSubtitle();

    function createSubtitle()
    {
        var element;
        for (var i = 0; i < doc.syncData1.length; i++) {
            element = doc.createElement('span');
            element.setAttribute("id", "c_" + i);
            element.innerText = doc.syncData1[i].text + " ";
            subtitles_1.appendChild(element);
        }
        for (var i = 0; i < doc.syncData2.length; i++) {
            element = doc.createElement('span');
            element.setAttribute("id", "c_" + i);
            element.innerText = doc.syncData2[i].text + " ";
            subtitles_2.appendChild(element);
        }
    }

    audioPlayer.addEventListener("timeupdate", function(e){
      if(audioPlayer.currentTime <= "6.353") {
        doc.syncData1.forEach(function(element, index, array){
            if( audioPlayer.currentTime >= element.start && audioPlayer.currentTime <= element.end )
                subtitles_1.children[index].style.color = '#cfdfdc';
        });
      } else {
        doc.syncData2.forEach(function(element, index, array){
            if( audioPlayer.currentTime >= element.start && audioPlayer.currentTime <= element.end )
                subtitles_2.children[index].style.color = '#cfdfdc';
        });
      }

    });
}(window, document));
