const API_URL = "https://5jryt6hshh.execute-api.eu-west-1.amazonaws.com/prod/visitors";

async function updateVisitorCount() {
    try {
        const res = await fetch(API_URL, { method: "GET" });
        const data = await res.json();
        document.getElementById("visitor-count").textContent = data.count;
    } catch (err) {
        document.getElementById("visitor-count").textContent = "—";
    }
}

updateVisitorCount();
