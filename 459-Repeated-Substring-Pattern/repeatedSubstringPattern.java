class Solution {
  public boolean repeatedSubstringPattern(String s) {
    int[] fail_table = new int[s.length()];
    int left = 0;

    for (int right = 1; right < s.length(); right++) {
      while ((s.charAt(left) != s.charAt(right)) && (left > 0)) {
        left = fail_table[left-1];
      }
      if (s.charAt(left) == s.charAt(right)) {
        left++;
        fail_table[right] = left;
      }
    }

    int length_repeated = fail_table[s.length()-1];
    int length_substring = s.length() - length_repeated;

    return (length_repeated != 0) && (length_repeated % length_substring == 0);
  }
}