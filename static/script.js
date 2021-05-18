const PRE = "DELTA"
const SUF = "MEET"
var room_id;
function createRoom(){
    console.log("Creating Room")
    let room = document.getElementById("room-input").value;
    if(room == " " || room == "")   {
        alert("Please enter room number")
        return;
    }
    room_id = PRE+room+SUF;
    hideModal();
    ifrm = document.getElementById("myframe");
    ifrm.setAttribute('src', 'https://nodevideocalljs.herokuapp.com/'+room_id);
}


function hideModal(){

    document.getElementById("enter").hidden = true
    document.getElementById("room-input").hidden = true
    document.getElementById("button1").hidden = true
    document.getElementById("button2").hidden = true
    document.getElementById("myframe").hidden = false
}


function joinRoom(){
    console.log("Joining Room")
    let room = document.getElementById("room-input").value;
    if(room == " " || room == "")   {
        alert("Please enter room number")
        return;
    }
    room_id = PRE+room+SUF;
    hideModal();
    ifrm = document.getElementById("myframe");
    ifrm.setAttribute('src', 'https://nodevideocalljs.herokuapp.com/'+room_id);

}