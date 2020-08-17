int shortestSolutionLength(String[] source) {
                StringBuilder result = new StringBuilder();
                for(String str : source){
                        result.append(str);
                        result.append('\n');
                }
                String res = result.toString();
                String p = "(?<!:)\\/\\/.*|\\/\\*(\\s|.)*?\\*\\/";
                String hehe = res.replaceAll(p,"");
                int num = 0;
                char[] ai = hehe.toCharArray();
                for(int i = 0; i < ai.length; i++){
                        char temp = ai[i];
                        if(temp == ' ' || temp == '\n'){
                                continue;
                        }
                        num++;
                }
                return num;
               
        }

