const arr = [1,2,3,4,5]

const mM = a => {
    const x = a.sort((a,b)=> a - b)
    let min = 0, max = 0;
    for(let i = 0; i < x.length - 1; i++){
        min += x[i]
    }
    for(let i = 1; i < x.length; i++){
        max += x[i]
    }
    return [min, max]
}

console.log(mM(arr))
