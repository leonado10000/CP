    public int[] twoSum(int[] nums, int target) {
        int land;
        for(int i = 0 ; i < nums.length; i++){
            land = target - nums[i];

            for(int j = i+1 ; j < nums.length; j++){
//                System.out.println(i+" "+j+" "+land);
                if ( nums[j] == land ){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }