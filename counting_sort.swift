func countSort([Int]) -> [Int] {
    var countDict = [Int:Int]()

    //add numbers to dictionary and count of times the number appears
    for idx in input {
        if countDict[idx] > 0 {
            countDict[idx] = countDict[idx]! + 1
        } else{
            countDict[idx] = 1
        }
    }

    //create output string
    var outputStr = String()
    for num in 0...99 {
        if countDict[num] > 0 {
            for number in 0...countDict[num]! - 1 {
            outputStr = outputStr +  String(num) + " "
            }
        }
    }
    return outputStr
}

countSort()
