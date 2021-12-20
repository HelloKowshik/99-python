let ar = [12,1,6,8,2,4,4,5]
// let sortedArr = [...new Set(ar)].sort((a, b) => a - b)
// console.log(sortedArr)


grades = [39, 78, 43]

function solve(grades){
    return grades.map(function(grade)  {
        return (grade >= 38 && grade % 5 >= 3) ? grade + 5 - (grade % 5) : grade;
    });
}

console.log(solve(grades))
