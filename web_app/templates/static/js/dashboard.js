let map = L.map("map").setView([32.37, -86.30], 11);

L.tileLayer(
"https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
{
attribution: "&copy; OpenStreetMap"
}
).addTo(map);

let geoLayer;
let profiles = [];
let scenarios = [];
let chartInstance = null;


// ==========================
// Load Data
// ==========================

fetch("/api/districts")
.then(res => res.json())
.then(data => {

    let geo = data.geojson;
    profiles = data.profiles;
    scenarios = data.scenarios;

    geoLayer = L.geoJSON(geo, {

        style: function(feature){

            return {
                fillColor:"#3498db",
                weight:2,
                color:"black",
                fillOpacity:0.6,
                className:"districtPolygon"
            }

        },

        onEachFeature: function(feature, layer){

            layer.bindTooltip(
                "District " + feature.properties.District,
                {sticky:true}
            );

            layer.on("click", function(){

                let districtName = feature.properties.District;
                let districtId = districtName.split(" ")[1];

                showAnalytics(districtId);

            });

        }

    }).addTo(map);

});


// ==========================
// Show Analytics
// ==========================

function showAnalytics(districtId){

    let profile = profiles.find(p => p.District == districtId);
    let scenario = scenarios.find(s => s.district == districtId);

    let container = document.getElementById("district-info");

    if(!profile){
        container.innerHTML = "<b>No profile found</b>";
        return;
    }

    let html = `
        <h3>District ${districtId}</h3>

        <b>Businesses:</b> ${profile.Business_Count}<br>
        <b>Violations:</b> ${profile.Violations_Count}<br>
        <b>Business Level:</b> ${profile.Business_Level}<br>
        <b>Stress Level:</b> ${profile.Stress_Level}<br>
        <b>Type:</b> ${profile.District_Type}

        <hr>
        <h3>Scenarios</h3>
    `;

    let labels = [];
    let scores = [];

    if(scenario){

        scenario.scenario.forEach(s => {

            html += `
                <div style="background:white;
                padding:10px;
                margin-bottom:10px;
                border-radius:6px">

                <b>${s.scenario_type}</b><br>
                <i>${s.title}</i><br>
                Fit Score: ${s.fit_score}

                <ul>
            `;

            s.actions.forEach(action=>{
                html += `<li>${action}</li>`;
            });

            html += "</ul></div>";

            labels.push(s.scenario_type);
            scores.push(s.fit_score);

        });

    }

    container.innerHTML = html;

    drawChart(labels, scores);
}


// ==========================
// Chart
// ==========================

function drawChart(labels, scores){

    let ctx = document.getElementById("chart");

    if(chartInstance){
        chartInstance.destroy();
    }

    chartInstance = new Chart(ctx, {

        type:"bar",

        data:{
            labels:labels,
            datasets:[{
                label:"Fit Score",
                data:scores,
                backgroundColor:"#2ecc71"
            }]
        },

        options:{
            responsive:true,
            scales:{
                y:{
                    beginAtZero:true,
                    max:100
                }
            }
        }

    });

}


// ==========================
// Policy Slider
// ==========================

let slider = document.getElementById("policySlider");

slider.addEventListener("input", function(){

    document.getElementById("policyValue").innerText = this.value;

});