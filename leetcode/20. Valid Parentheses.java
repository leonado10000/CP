public class sol
    {public boolean isValid(String s) {
        if (s.length()==1){
            return false;
        }
        int a=0,b=0,c=0;
        int[] last = new int[s.length()];
        int index=-1;
        for (int i =0; i< s.length(); i++){
            if (s.charAt(i) == '('){
                a++;
                last[++index] = 1;
            }
            else if (s.charAt(i) == '{'){
                b++;
                last[++index] = 2;
            }            
            else if (s.charAt(i) == '['){
                c++;
                last[++index] = 3;
            }
            if (index<0){return false;}
            else if (s.charAt(i) == ')'){
                // System.out.println(index);
                if (last[index] != 1){
                    return false;
                }
                a--;
                index--;
            }            
            else if (s.charAt(i) == '}'){
                if (last[index] != 2){
                    return false;
                }
                b--;
                index--;
            }            
            else if (s.charAt(i) == ']'){
                if (last[index] != 3){
                    return false;
                }
                c--;
                index--;
            }
            // for (int l =0; l <= i; l++)
            // System.out.print(last[l]);
            // System.out.println();

        }
        if (a == 0 && b == 0 && c == 0){
            return true;
        }
        else{
            return false;
        }
    }}