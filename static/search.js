/**
 * Implement these two search algorithms.
 */

/**
 * Search for the number in the sorted list with the linear search algorithm
 * and return the index of the element.
 *
 * Optional: print out how many comparision was needed to find the number
 *
 * @param {number} number The number to search for
 * @param {array} list Ascending list of numbers
 * @returns {number|null} Index of the element or null
 */
function linear_search(number, list) {

    let steps = 1
    for (let i=0; i< list.length; i++){
        if (list[i] === number){
            return [i,steps];
        }  else {
            steps ++;
        }
    }

    return null;
}

/**
 * Search for the number in the sorted list with the binary search algorithm
 * and return the index of the element.
 *
 * Optional: print out how many comparision was needed to find the number
 *
 * @param {number} number The number to search for
 * @param {array} list Ascending list of numbers
 * @returns {number|null} Index of the element or null
 */
function binary_search(number, list) {

    let left = 0;
    let right = list.length-1;
    let steps = 1;
    while (left <= right){
        mid = Math.floor((left + right)/2);

        if (number === list[mid]){
            return [mid, steps];
        } else if (number === list[left]) {
            return [left,steps];
        } else if (number === list[right]) {
            return [right, steps];
        } else {
            if (number > list[mid]) {
                left = mid + 1;
                steps ++;
            } else if (number < list[mid]) {
                right = mid - 1;
                steps ++;
            }
        }
    }
    return null;
}

function print_result(search, index) {
    let result = search + ' search ';

    if (index === null) {
        result += 'did not find it.'
    } else {
        result += `found it on index ${index[0]} in ${index[1]} steps.`
    }

    console.log(result);
}


function main() {
    let numbers = [3, 6, 8, 11, 18, 23, 24, 33, 36, 45, 46, 51, 56, 60, 69, 72, 83, 90, 93, 97];
    console.log(numbers)

    let searched_number = Number(prompt('What is the number you are looking for? (0-100)'));

    print_result('Linear', linear_search(searched_number, numbers));
    print_result('Binary', binary_search(searched_number, numbers));
}

main();

