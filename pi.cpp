*/Question (source -coding ninja)
  Given a string, compute recursively a new string where all appearances of "pi" have been replaced by "3.14".
  example: pippppiepi     => 3.14ppp3.14e3.14 */
    
////Use Recursion Here////
    
#include <iostream>
using namespace std;

void replacePi(char input[]) {
    if(input[1]=='\0')
    {
        return ;
    }

    replacePi(input+1);

    if(input[0]=='p' and input[1]=='i' )
    {
        int i=0;

        while(input[i]!='\0')
        {
            i++;
        }

        while(i>=0)
        {
            input[i+2]=input[i];
            i--;
        }
        input[0]='3';
        input[1]='.';
        input[2]='1';
        input[3]='4';
    }


}
int main() {
    char input[10000];
    cin.getline(input, 10000);
    replacePi(input);
    cout << input << endl;
}
