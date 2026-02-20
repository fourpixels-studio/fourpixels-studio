function copyToClipboard() {
    var copyText = document.getElementById("blogShareLink");
    var copyBtn = document.getElementById("copy-btn");
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    document.execCommand("copy");
    copyBtn.innerHTML = "Link Copied";
}
function shareToStory(imageUrl, link) {
    const intentUrl = `https://www.instagram.com/stories/share/` +
        `?backgroundImage=${encodeURIComponent(imageUrl)}&` +
        `deeplink=${encodeURIComponent(link)}`;
    window.location.href = intentUrl;
}