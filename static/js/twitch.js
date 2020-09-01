import "./vendor/twitch-embed-v1.min.js";
import "./vendor/twitch-embed-v1.min.js";

const player = new Twitch.Embed("twitch-embed", {
    width: "100%",
    height: "100%",
    channel: "Team_Poolside"
});

const setStreamLinkVisible = (visible = true) => () => {
    console.log('setting visibility', visible);
    // document.getElementById("watch-on-twitch").style.visibility = visible ?
    //     "visible" : "hidden";
    document.getElementById("stream-live").innerText = `Currently ${visible ? "ONLINE" : "OFFLINE"}`;
};

player.addEventListener(Twitch.Player.ONLINE, setStreamLinkVisible());
player.addEventListener(Twitch.Player.OFFLINE, setStreamLinkVisible(false));