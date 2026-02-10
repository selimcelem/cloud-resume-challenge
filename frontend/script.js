js

const API_URL = ""; // after backend is deployed, add the URL here

async function loadVisitorCount() {
    const el = document.getElementById("visitor-count");
    if (!el) return;

    if (!API_URL) {
        el.textContent = "-";
        return;
    }

    try {
        const res = await fetch(API_URL);
        const data = await res.json();
        el.textContent = data.count || "-";
    } catch {
        el.textContent = "-";
    }
}

docment.addEventListener("DOMContentLoaded", loadVisitorCount);