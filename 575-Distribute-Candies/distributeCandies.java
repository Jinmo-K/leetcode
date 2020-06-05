import java.util.HashSet;

class Solution {
  public int distributeCandies(int[] candies) {
    HashSet<Integer> unique = new HashSet<>();
    for (int candy: candies) {
      unique.add(candy);
      if (unique.size() == candies.length / 2) {
        return unique.size();
      }
    }
    return Math.min(unique.size(), candies.length / 2);
  }
}