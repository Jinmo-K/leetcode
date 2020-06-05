import java.util.LinkedList;

class Solution {
  public String removeKdigits(String num, int k) {
    LinkedList<Character> stack = new LinkedList<>();

    for (char digit : num.toCharArray()) {
      while (k > 0 && stack.size() > 0 && stack.peekLast() > digit) {
        stack.removeLast();
        k--;
      }
      stack.addLast(digit);
  }

    for (int i = 0; i < k; i++) {
      stack.removeLast();
    }
    return getResultString(stack);

  }

  private String getResultString(LinkedList<Character> stack) {
    StringBuilder res = new StringBuilder();
    boolean leadingZero = true;

    for (char digit : stack) {
      if (leadingZero && digit == '0') {
          continue;
      }
      leadingZero = false;
      res.append(digit);
    }

    if (res.length() == 0) {
      return "0";
    }
    return res.toString();
  }
}
