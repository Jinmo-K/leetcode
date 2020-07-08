var decodeString = function(s) {
  let curr_num = 0;
  let curr_string = '';
  let stack = [];
  
  for (let i = 0; i < s.length; i++) {
      let ch = s.charAt(i);
      if (ch >= '0' && ch <= '9') {
          curr_num = curr_num * 10 + parseInt(ch);
      } else if (ch === '[') {
          stack.push(curr_string);
          stack.push(curr_num);
          curr_num = 0;
          curr_string = '';
      } else if (ch === ']') {
          prev_num = stack.pop();
          prev_string = stack.pop();
          curr_string = prev_string + curr_string.repeat(prev_num);
      } else {
          curr_string += ch;
      }
  }
  
  return curr_string;
};