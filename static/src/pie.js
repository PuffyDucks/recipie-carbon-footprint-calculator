let ingredients = ["Flour", "Bananas", "Apples", "Beef", "Cheese"];
let emissions = [12, 20, 10, 33, 25];
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
}, 300);
