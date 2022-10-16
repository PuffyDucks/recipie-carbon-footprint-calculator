var ingredients = ["Flour", "Bananas", "Apples", "Beef", "Cheese"];
var emissions = [12, 20, 10, 33, 25];
var sliceColors = [
    "#eed11e",
    "#eed11e",
    "#eed11e",
    "#eed11e",
    "#eed11e"
];
        
new Chart("pieChart", {
    type: "pie",
    data: {
    labels: ingredients,
    datasets: [{
        backgroundColor: sliceColors,
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