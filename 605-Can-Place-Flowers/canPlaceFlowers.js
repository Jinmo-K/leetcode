/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
  let prev = 0;
  
  for (let i = 0; i < flowerbed.length; i++) {
      if (flowerbed[i] === 0 && prev === 0 && (i === flowerbed.length - 1 || flowerbed[i+1] === 0)) {
          n -= 1;
          if (n === 0) return true;
          prev = 1;
      }
      else {
          prev = flowerbed[i];
      }
  }
  
  return n <= 0;
};