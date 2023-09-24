#include <iostream>
#include <vector>

using namespace std;

vector<int> twoSum(vector<int> input, int target){
    vector<int> output;

    bool statusFlag = false;
    int loopCounter = 0;

    for (int i = 0; i < input.size(); i++){
        loopCounter++;
        if (statusFlag == false){
            for (int j = 0; j < input.size(); j++){
                loopCounter++;
                if (input[i] + input[j] == target){
                    output.push_back(i);
                    output.push_back(j);
                    statusFlag = true;
                }
            }
        }     
    }
    cout << loopCounter << endl;
    return output;
}

int main(){

    vector<int> myVector {8, 6, 2, 4, 5, 3, 4, 7    };

    vector<int> myResult;
    myResult = twoSum(myVector, 14);
    
    for (int i: myResult){
        cout << i << ' ' << endl;
    }

}