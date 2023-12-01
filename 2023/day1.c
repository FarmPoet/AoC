#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define R return
typedef unsigned char C, *S;
typedef int I;
typedef void V;
typedef FILE F;

C src[9][10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
C dst[9][10] = {"o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"};

I getVal(S s) {
C c; S p; I r, l;

    l = strlen(s);
    p = s;
    while(c = *(p++)) {
        if(c > 48 && c < 58) {
            r = (c - 48) * 10;
            p = s + l;
            while(l-- > -1) {
                c = *(p--);
                if(c > 48 && c < 58) {
                    r += c - 48;
                    R(r);
                }
            }
        }
    }
    R(-1);
}


void str_replace(S target, S srch, S rplc)
{
C buff[100];
S ins = &buff[0];
S tmp = target;
I srch_len = strlen(srch);
I repl_len = strlen(rplc);

    memset(buff, 0, 100);

    while(1) {
        S p = strstr(tmp, srch);

        if (!p) {
            strcpy(ins, tmp);
            break;
        }

        memcpy(ins, tmp, p - tmp);
        ins += p - tmp;
        memcpy(ins, rplc, repl_len);
        ins += repl_len;
        tmp = p + srch_len;
    }
    strcpy(target, buff);
}

I main() {
F *f;
C s[100]; 
I p1 = 0;
I p2 = 0;
I i;
    
    clock_t begin = clock();
    f = fopen ("i1.txt" , "r");
   
    if (!f) perror ("Error opening file");
    else {
        while(fgets(s, 100, f)) {
            s[strcspn(s, "\n")] = 0;
            p1 += getVal(s);

            for(i = 0; i < 9; i++) str_replace(s, src[i], dst[i]);
            p2 += getVal(s);
        }
     
    fclose(f);
    }

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Elapsed: %lf seconds\n", time_spent);
    
    printf("%d, %d\n", p1, p2);
    R(0);
}
