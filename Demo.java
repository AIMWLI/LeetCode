import java.util.HashSet;
class Solution {
  public static int[] intersection(int[] nums1, int[] nums2) {
    HashSet<Integer> set1 = new HashSet<Integer>();
    for (Integer n : nums1) set1.add(n);
    HashSet<Integer> set2 = new HashSet<Integer>();
    for (Integer n : nums2) set2.add(n);

    set1.retainAll(set2);

    int [] output = new int[set1.size()];
    System.out.println(set1.size());
    int idx = 0;
    for (int s : set1) output[idx++] = s;
    for (int i : output) {
      System.out.println(i);
  }
    return output;
  }
  /**
   * test demo
   * @param args
   */
  public static void main(String[] args) {
    int[] nums1 = {1,1,2};
    int[] nums2 = {1,3,4};
    intersection(nums1,nums2);
  }
}