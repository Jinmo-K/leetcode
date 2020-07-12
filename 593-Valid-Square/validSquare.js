/**
 * @param {number[]} p1
 * @param {number[]} p2
 * @param {number[]} p3
 * @param {number[]} p4
 * @return {boolean}
 */
var validSquare = function(p1, p2, p3, p4) {
  const calculateDist = (a, b) => {
      return Math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2);
  };
  const comparePoints = (a, b) => {
      return a[0] === b[0] && a[1] === b[1];  
  };
  
  if (comparePoints(p1, p2) || comparePoints(p1, p3) || comparePoints(p1, p4) || comparePoints(p2, p3) || comparePoints(p2, p4) || comparePoints(p3, p4)) {
      return false;
  }
  
  let points = [p1, p2, p3, p4];
  let distances = {};
  
  // Calculate distances between each point
  for (let i = 0; i < 3; i++) {
      for (let j = i + 1; j < 4; j++) {
          let distance = calculateDist(points[i], points[j]);
          if (distance in distances) {
              distances[distance]++;
          } 
          else {
              distances[distance] = 1;    
          }
      }
  }

  let values = Object.values(distances);
  
  return values.length === 2
};