$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    })
    // siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });
    //siri message amimation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync:true,
        },
        out: {
            effect:"fadeOutUp",
            sync:true,
        },
    })
    //mic button click event
    $("#mic_but").click(function () { 
        eel.playAssistantSound()
        $("#oval").attr("hidden",true);
        $("#SiriWave").attr("hidden",false); 

        eel.all_Commands()()
        
    });
    function doc_keyUp(e){
        //this would test whichever key is 40(down arrow) and  the  ctrl key at the same time
        if (e.key=='j' && e.metaKey){
            eel.playAssistantSound()
            $("#oval").attr("hidden",true)
            $("#SiriWave").attr("hidden",false)
            eel.all_Commands()

        }
    }
    document.addEventListener("keyup",doc_keyUp,false)

    });