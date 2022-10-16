let ingredients = foodsList;
let emissions = emissionsList;
let sliceColor = "#eed11e";

setTimeout(() => {
    new Chart("pieChart", {
        type: "pie",
        data: {
        labels: ingredients,
        datasets: [{
            backgroundColor: sliceColor,
            data: emissions
        }]
        },
        options: {
            plugins: {
                legend: {
                    labels: {
                        color: "#FFFFFF"
                    }
                },
            },
            responsive: false,
            borderColor: "#2d1f61",
            borderWidth: 5
        }
    });
}, 500);
