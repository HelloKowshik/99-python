// const potato_price = [1, 3, 2, 8, 4, 10];
// const fee = 2;
const potato_price = [2, 4, 6, 10, 3, 12, 15, -1, 0, 4];
const fee = 10;
const maxProfit1 = (priceArr) => {
    let profitArr = [];
    let min_price = priceArr[0];
    let max_profit = priceArr[1] - priceArr[0] - fee;
    for(let i = 0; i < priceArr.length; i++){
        let current_price = priceArr[i];
        let profit = current_price - min_price - fee;
        max_profit = Math.max(max_profit, profit);
        min_price = Math.min(min_price, current_price);
        profitArr.push(max_profit);
    }
    // return max_profit;
    let x = [...new Set(profitArr)];
    return x;
}

// console.log(maxProfit(potato_price));

const findMaxProfit = (priceArr, fee) =>
{
     
    // const profit_arr = new Array(priceArr.length).fill(0);
    const profit_arr = Array.from(priceArr).fill(0);
    // console.log(profit_arr);
    let len = priceArr.length;
    let max_price = priceArr[len - 1];
    for(let i = len - 2; i >= 0; i--)
    {
        if (priceArr[i] > max_price)
            max_price = priceArr[i];
        // console.log( i,':',max_price, profit_arr[i + 1],profit_arr[i], priceArr[i]);
        profit_arr[i] = Math.max(profit_arr[i + 1],
                            max_price - priceArr[i] - fee);
        // console.log(i,':',profit_arr[i], priceArr[i]);
    }
    // console.log(profit_arr)
    // console.log('R To L:', profit_arr);

    let min_price = priceArr[0];
    for(let i = 1; i < len; i++)
    {
        if (priceArr[i] < min_price)
            min_price = priceArr[i];
        profit_arr[i] = Math.max(profit_arr[i - 1],
                profit_arr[i] + (priceArr[i] - min_price - fee));
    }

    // console.log('L To R:', profit_arr);
    // let result = profit_arr[len - 1];
    return Math.max(...profit_arr);
}

console.log(findMaxProfit(potato_price, fee))
