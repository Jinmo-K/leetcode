public class Solution extends Relation {
  private int num_people;

  public int findCelebrity(int n) {
    num_people = n;
    if (n <= 1) {
      return n - 1;
    }

    int candidate = 0;

    for (int i = 1; i < n; i++) {
      if (knows(candidate, i)) {
        candidate = i;
      }
    }

    if (isCelebrity(candidate)) {
      return candidate;
    }
    return -1;
  }

  private boolean isCelebrity(int candidate) {
    for (int i = 0; i < num_people; i++) {
      if ((knows(candidate, i) || !knows(i, candidate)) && candidate != i) {
        return false;
      }
    }
    return true;
  }
}